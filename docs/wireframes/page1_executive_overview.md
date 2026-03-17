# Page 1: Executive Overview

## Purpose

Give leadership a single-screen snapshot of incident volume, current backlog, SLA health, and where attention is needed. Answer: *What is the overall state of operations?*

---

## Filters

- **Environment** (slicer: Production, UAT, Test, Dev) — optional; default “All”.
- **Date range** (slicer or relative date filter on CreatedDate) — e.g. Last 90 days.

Keep filters minimal so the page stays high-level.

---

## Visuals

| # | Visual | Data / measure | Notes |
|---|--------|-----------------|--------|
| 1 | **KPI cards (row of 4–5)** | Total Incidents, Open Incidents, Resolved Incidents, SLA Breach Rate (%), Critical Incident Count | Large numbers; use conditional formatting on breach rate (e.g. red if > 15%). |
| 2 | **Line or area chart** | Incidents over time (CreatedDate) — count by day or week | Trend: volume going up or down. |
| 3 | **Stacked bar or pie** | Incidents by Status (New, In Progress, Pending, Resolved, Closed) | Where work sits in the funnel. |
| 4 | **Bar chart** | Incidents by Environment (Production, UAT, Test, Dev) | Where volume is concentrated; environment risk. |
| 5 | **Bar or column chart** | Incidents by Priority (P1–P4) or by Severity | Priority mix at a glance. |

---

## Layout Suggestion

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Executive Overview                    [Environment ▼]  [Date range ▼]      │
├─────────────────────────────────────────────────────────────────────────────┤
│  [Total]   [Open]   [Resolved]   [SLA Breach %]   [Critical]                 │
│   KPI 1    KPI 2      KPI 3          KPI 4           KPI 5                    │
├──────────────────────────────┬──────────────────────────────────────────────┤
│                              │                                              │
│  Incidents over time         │  By Status (stacked bar or pie)               │
│  (line/area chart)            │                                              │
│                              │                                              │
├──────────────────────────────┼──────────────────────────────────────────────┤
│  By Environment (bar)        │  By Priority or Severity (bar)                │
│                              │                                              │
└──────────────────────────────┴──────────────────────────────────────────────┘
```

- **Top:** Title + 1–2 slicers on the right.
- **Row 2:** KPI cards in a single row.
- **Row 3:** Two panels — left: trend; right: status mix.
- **Row 4:** Two panels — environment and priority/severity.

---

## What the Hiring Manager Should Understand

- You can **frame an executive story**: one page that answers “How are we doing?” with volume, backlog, SLA, and critical count.
- You use **clear KPIs** (total, open, resolved, breach rate, critical) and **simple filters** (environment, date).
- You **balance trend and breakdown**: time trend plus breakdowns by status, environment, and priority so the viewer sees both “over time” and “where it sits now.”
- The page is **stakeholder-friendly**: no clutter, obvious takeaways, suitable for leadership review.
