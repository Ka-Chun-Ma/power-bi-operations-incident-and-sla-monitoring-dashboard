# Page 2: SLA and Backlog Analysis

## Purpose

Focus on SLA performance and backlog health so operations can see where we breach, how long we take to resolve, and which open tickets are ageing. Answer: *Where are we missing SLA, and where is the backlog at risk?*

---

## Filters

- **Environment** (slicer).
- **Priority** (slicer: P1, P2, P3, P4).
- **Date range** (CreatedDate or ResolvedDate, depending on chart).

---

## Visuals

| # | Visual | Data / measure | Notes |
|---|--------|-----------------|--------|
| 1 | **KPI cards** | SLA Breach Rate (%), Average Resolution Hours, Median Resolution Hours, Backlog Count, Backlog Over 7 Days | Core SLA and backlog metrics. |
| 2 | **Clustered bar or table** | Breach count or breach rate by Environment, or by Priority | Where breaches concentrate. |
| 3 | **Clustered bar or column** | Average (or median) Resolution Hours by Priority, or by Category | Resolution time by dimension. |
| 4 | **Bar chart or histogram** | Open incidents by Age_Days (buckets: 0–7, 8–14, 15–30, 31+) | Backlog ageing distribution. |
| 5 | **Table** | List of open incidents with Age_Days > 7: IncidentID, Priority, Environment, Category, Team, Age_Days | Actionable backlog list; optional drill-through. |

---

## Layout Suggestion

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  SLA and Backlog Analysis         [Environment ▼] [Priority ▼] [Date ▼]    │
├─────────────────────────────────────────────────────────────────────────────┤
│  [SLA Breach %]  [Avg Res Hours]  [Median Res H]  [Backlog]  [Backlog >7d]   │
├──────────────────────────────┬──────────────────────────────────────────────┤
│                              │                                              │
│  Breach rate/count by        │  Avg Resolution Hours by Priority/Category    │
│  Environment or Priority     │  (clustered bar)                              │
│  (bar chart)                 │                                              │
├──────────────────────────────┼──────────────────────────────────────────────┤
│  Backlog ageing              │  Table: Open incidents > 7 days               │
│  (Age_Days buckets:          │  (IncidentID, Priority, Env, Category,       │
│   0–7, 8–14, 15–30, 31+)     │  Team, Age_Days)                              │
└──────────────────────────────┴──────────────────────────────────────────────┘
```

- **Top:** Title + slicers (Environment, Priority, Date).
- **Row 2:** SLA and backlog KPI cards.
- **Row 3:** Left — where we breach; right — resolution time by priority/category.
- **Row 4:** Left — ageing buckets; right — table of ageing open tickets.

---

## What the Hiring Manager Should Understand

- You **separate SLA from backlog**: one page dedicated to “did we meet SLA?” and “how old is our backlog?”
- You use **both average and median** resolution time (shows you know median is better for skewed data).
- You **segment by environment and priority** so the team can see which areas drive breaches and slow resolution.
- You make **backlog actionable**: ageing buckets plus a table of tickets over 7 days so the viewer knows what to prioritise.
- The page supports the business question: *What should we prioritise first?* (breaches and oldest open tickets).
