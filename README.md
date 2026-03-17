# Power BI Operations Incident and SLA Monitoring Dashboard

A portfolio project demonstrating operations reporting and SLA monitoring for Data Analyst and reporting roles. The dashboard simulates a scenario where an operations or support team tracks incident volume, SLA risk, backlog ageing, and root-cause patterns.

---

## What This Project Is

- **Purpose:** A recruiter-friendly Power BI portfolio piece showing analytical thinking, KPI design, business-question framing, and stakeholder-ready reporting.
- **Scope:** One dataset (incident-level), one star-style model, three report pages: Executive Overview, SLA & Backlog Analysis, and Root Cause & Ticket Explorer.
- **Data:** Synthetic sample data (300–500 rows) with realistic patterns in breach rates, environment risk, backlog ageing, and category concentration. Suitable for building the report without access to production systems.

**Primary business questions the dashboard addresses:**

1. Where are incidents concentrated?
2. Which categories, environments, or priorities drive SLA breaches and unresolved backlog?
3. What should the team prioritise first?

---

## Scope & priorities

This is a **Data Analyst portfolio project**, not an enterprise system. Design choices optimise for: *What would let a hiring manager understand my capability in 30–60 seconds?*

| Prioritise | Deprioritise |
|------------|--------------|
| Business clarity, clean data model, strong KPI logic | Advanced AI, unnecessary automation |
| Practical dashboard structure, recruiter readability | Complex scripting (unless needed), visual gimmicks |
| Truthful, professional documentation | Unrealistic business impact claims |

Full principles: [docs/SCOPE_AND_PRIORITIES.md](docs/SCOPE_AND_PRIORITIES.md).

---

## Repository Structure

| Path | Description |
|------|-------------|
| **data/sample/** | Sample CSV used in Power BI (`incidents_sample.csv`). |
| **data/raw/** | Placeholder for raw source files (optional). |
| **docs/** | Schema, star schema, DAX measures, wireframes, data dictionary. |
| **scripts/** | Python script to regenerate the sample dataset. |

**Key documents:**

- [Dataset schema & assumptions](docs/dataset_schema.md)
- [Data dictionary](docs/data_dictionary.md)
- [Star schema recommendation](docs/star_schema.md)
- [DAX measures](docs/dax_measures.md)
- [Wireframes (3 pages)](docs/wireframes/)
- [Portfolio summary, resume bullets & interview notes](docs/PORTFOLIO_SUMMARY.md)

---

## How to Use This Repo

### Option 1: Build the report in Power BI

1. Open Power BI Desktop.
2. Get data → Text/CSV → select `data/sample/incidents_sample.csv`.
3. Optionally create a date dimension and relate it to `CreatedDate` (see [Star schema](docs/star_schema.md)).
4. Add the measures from [DAX measures](docs/dax_measures.md).
5. Build the three pages using the [wireframes](docs/wireframes/) as a guide.

### Option 2: Regenerate the sample data

Requires Python 3.

```bash
# From the repo root (Windows)
venv\Scripts\activate
python scripts/generate_sample_data.py --rows 420

# Optional: different row count or seed
python scripts/generate_sample_data.py --rows 400 --seed 123
```

Output: `data/sample/incidents_sample.csv` (overwrites existing).

---

## Dashboard Pages (Summary)

| Page | Purpose |
|------|---------|
| **1. Executive Overview** | High-level KPIs (total, open, resolved, SLA breach %, critical), trend over time, breakdown by status, environment, and priority. |
| **2. SLA and Backlog Analysis** | SLA breach rate and resolution hours (avg/median), backlog count, backlog over 7 days, ageing buckets, and a table of ageing open tickets. |
| **3. Root Cause and Ticket Explorer** | Incidents by category and team, cross-tabs (e.g. category × environment), reopened rate, and a ticket-level table for drill-down. |

Detailed layouts and visuals are in `docs/wireframes/`.

---

## Technologies & Assumptions

- **Power BI Desktop** for the report and data model.
- **Sample data:** Generated with Python (stdlib only: `csv`, `random`, `datetime`). No production or confidential data.
- **Australian spelling** used in documentation where applicable (e.g. prioritise, organisation).

---

## Licence

This project is for portfolio and learning purposes. Feel free to adapt the structure, schema, and DAX for your own work; no warranty is provided.

---

For **resume bullet points**, **case study summary**, and **interview talking points** tailored to Data Analyst roles in Australia, see **[docs/PORTFOLIO_SUMMARY.md](docs/PORTFOLIO_SUMMARY.md)**.
