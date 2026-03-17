# Page 3: Root Cause and Ticket Explorer

## Purpose

Let the operations team explore incidents by category, team, and other dimensions to spot patterns and recurring issues. Support drill-down and ad-hoc filtering. Answer: *Where are incidents concentrated, and which categories or teams need focus?*

---

## Filters

- **Environment**, **Priority**, **Severity** (slicers).
- **Category**, **Team** (slicers or in visuals).
- **Status** (optional: All, Open only, Resolved only).
- **Date range** (CreatedDate).

---

## Visuals

| # | Visual | Data / measure | Notes |
|---|--------|-----------------|--------|
| 1 | **KPI cards** | Total Incidents, Open Incidents, Reopened Incident Rate (%), Critical Incident Count | Context for the current filter selection. |
| 2 | **Bar or treemap** | Incidents by Category (Access, Performance, Data, Integration) | Category concentration; root-cause view. |
| 3 | **Bar chart** | Incidents by Team (Platform, Data, Support, Infrastructure) | Ownership and workload. |
| 4 | **Matrix or table** | Rows: Category (or Subcategory); Columns: Environment or Priority; Value: count or % | Cross-tab to see category × environment or category × priority. |
| 5 | **Table** | Ticket list: IncidentID, CreatedDate, Status, Priority, Severity, Environment, Category, Team, Age_Days (optional: Resolution_Hours, Breach_Flag) | Explorer: click a segment to see underlying tickets. |

---

## Layout Suggestion

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Root Cause and Ticket Explorer                                              │
│  [Env ▼] [Priority ▼] [Severity ▼] [Category ▼] [Team ▼] [Status ▼] [Date ▼] │
├─────────────────────────────────────────────────────────────────────────────┤
│  [Total]   [Open]   [Reopened %]   [Critical]                                │
├──────────────────────────────┬──────────────────────────────────────────────┤
│                              │                                              │
│  By Category (bar/treemap)   │  By Team (bar)                               │
│                              │                                              │
├──────────────────────────────┴──────────────────────────────────────────────┤
│  Matrix: Category × Environment (or Category × Priority) — count or %        │
├──────────────────────────────────────────────────────────────────────────────┤
│  Table: IncidentID | CreatedDate | Status | Priority | Severity | Env |      │
│         Category | Team | Age_Days (… optional columns)                      │
└──────────────────────────────────────────────────────────────────────────────┘
```

- **Top:** Title + multiple slicers for deep filtering.
- **Row 2:** Few KPIs to reflect the current selection.
- **Row 3:** Category and Team charts side by side.
- **Row 4:** Matrix for cross-tab (e.g. category vs environment).
- **Row 5:** Full-width table for ticket-level exploration.

---

## What the Hiring Manager Should Understand

- You **frame root-cause analysis**: category and team views plus a matrix show where incidents concentrate and how they vary by environment or priority.
- You support **exploration**: many filters and a ticket-level table let the user slice and see underlying records (good for “recurring issue” and “which team is overloaded?”).
- You include **reopened rate** as a quality signal (reopened tickets suggest incomplete fix or recurring issues).
- The page is **analyst-friendly**: suitable for operations and support to answer “why?” and “where?” without leaving the report.
- Together with Page 1 (overview) and Page 2 (SLA/backlog), the report tells a clear story: state of play → SLA and backlog → root cause and drill-down.
