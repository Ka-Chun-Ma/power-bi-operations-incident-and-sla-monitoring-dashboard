#!/usr/bin/env python3
"""
Generate a realistic sample incident dataset for the Power BI Operations
Incident and SLA Monitoring Dashboard. Output: data/sample/incidents_sample.csv

Patterns baked in:
- Breach rates: higher for Production, P1, and Integration/Performance
- Environment risk: Production > UAT > Test > Dev (volume and breach)
- Backlog ageing: ~20% open; of those, meaningful share 7+ and 14+ days old
- Category concentration: Access & Performance most common, then Data, Integration
- Priority mix: P2/P3 dominant, some P1, fewer P4

Usage: python scripts/generate_sample_data.py [--rows N] [--seed N]
"""

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

# Defaults
DEFAULT_ROWS = 420
REFERENCE_TODAY = datetime(2025, 3, 10).date()  # "Today" for Age_Days
CREATED_START_DAYS_AGO = 90

# Weights for meaningful patterns (relative weights)
ENV_WEIGHTS = {"Production": 45, "UAT": 25, "Test": 20, "Dev": 10}
CATEGORY_WEIGHTS = {"Access": 28, "Performance": 26, "Data": 24, "Integration": 22}
PRIORITY_WEIGHTS = {"P1": 8, "P2": 42, "P3": 38, "P4": 12}
SEVERITY_BY_PRIORITY = {"P1": ["Critical", "High"], "P2": ["High", "Medium"], "P3": ["Medium", "Low"], "P4": ["Low", "Medium"]}
TEAMS = ["Platform", "Data", "Support", "Infrastructure"]
STATUS_RESOLVED = ["Resolved", "Closed"]
STATUS_OPEN = ["New", "In Progress", "Pending"]
# Breach propensity by environment (probability of breach if resolved)
BREACH_RATE_BY_ENV = {"Production": 0.28, "UAT": 0.18, "Test": 0.12, "Dev": 0.08}
# Category tends to push resolution time up (extra hours multiplier)
CATEGORY_SLOW = {"Integration": 1.4, "Performance": 1.25, "Data": 1.1, "Access": 1.0}
SLA_HOURS_BY_PRIORITY = {"P1": 4, "P2": 8, "P3": 24, "P4": 48}


def weighted_choice(weights_dict):
    items = list(weights_dict.keys())
    weights = [weights_dict[k] for k in items]
    return random.choices(items, weights=weights, k=1)[0]


def main():
    import argparse
    p = argparse.ArgumentParser(description="Generate sample incident CSV")
    p.add_argument("--rows", type=int, default=DEFAULT_ROWS, help="Approximate number of rows")
    p.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility")
    args = p.parse_args()
    random.seed(args.seed)

    repo_root = Path(__file__).resolve().parent.parent
    out_path = repo_root / "data" / "sample" / "incidents_sample.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    n = max(300, min(500, args.rows))
    created_start = REFERENCE_TODAY - timedelta(days=CREATED_START_DAYS_AGO)

    rows = []
    for i in range(1, n + 1):
        incident_id = f"INC{i:06d}"
        created = created_start + timedelta(days=random.randint(0, CREATED_START_DAYS_AGO - 1))
        environment = weighted_choice(ENV_WEIGHTS)
        category = weighted_choice(CATEGORY_WEIGHTS)
        priority = weighted_choice(PRIORITY_WEIGHTS)
        severity = random.choice(SEVERITY_BY_PRIORITY[priority])
        team = random.choice(TEAMS)
        sla_hours = SLA_HOURS_BY_PRIORITY[priority]

        # ~80% resolved/closed, ~20% open
        is_resolved = random.random() < 0.80
        if is_resolved:
            status = random.choice(STATUS_RESOLVED)
            # Breach probability: higher for Production, Integration, Performance
            breach_prob = BREACH_RATE_BY_ENV[environment]
            if category in ("Integration", "Performance"):
                breach_prob += 0.12
            breach = 1 if random.random() < breach_prob else 0
            if breach:
                resolution_hours = round(sla_hours * random.uniform(1.05, 1.7), 1)
            else:
                resolution_hours = round(sla_hours * random.uniform(0.25, 0.98), 1)
            # Resolved date from created + resolution_hours (as fractional days)
            resolved_date = created + timedelta(days=resolution_hours / 24.0)
            age_days = max(0, (resolved_date - created).days)
        else:
            status = random.choice(STATUS_OPEN)
            resolution_hours = ""
            resolved_date = ""
            breach = 0
            age_days = (REFERENCE_TODAY - created).days

        reopened = 1 if random.random() < 0.07 else 0
        review_needed = 1 if random.random() < 0.12 else 0
        subcategory = random.choice(["", "", "Login", "Permissions", "Timeout", "Sync", "Quality", ""])
        owner = random.choice(["Alex Chen", "Sam Jones", "Jordan Lee", "Casey Brown", "Riley Davis", ""])

        rows.append({
            "IncidentID": incident_id,
            "CreatedDate": created.isoformat(),
            "ResolvedDate": resolved_date.isoformat() if resolved_date else "",
            "Status": status,
            "Priority": priority,
            "Severity": severity,
            "Environment": environment,
            "Category": category,
            "Subcategory": subcategory.strip() if subcategory else "",
            "Team": team,
            "Owner": owner,
            "SLA_Target_Hours": sla_hours,
            "Resolution_Hours": resolution_hours if is_resolved else "",
            "Breach_Flag": breach,
            "Reopened_Flag": reopened,
            "Review_Needed_Flag": review_needed,
            "Age_Days": age_days,
        })

    fieldnames = list(rows[0].keys())
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {len(rows)} rows to {out_path}", file=__import__("sys").stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
