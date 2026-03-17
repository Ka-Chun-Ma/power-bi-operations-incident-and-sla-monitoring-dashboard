# Star Schema Recommendation (MVP)

**Purpose:** One fact table of incidents, one date dimension for time intelligence. Other attributes stay on the fact as columns (degenerate dimensions) to keep the model simple and portfolio-friendly.

---

## Diagram

```
                    ┌─────────────────┐
                    │    DimDate      │
                    │  (date column   │
                    │   + Year, Qtr,  │
                    │   Month, etc.)  │
                    └────────┬────────┘
                             │
         CreatedDate ────────┤
         (and optionally     │
          ResolvedDate)      │
                             ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                         FactIncidents (or Incidents)                      │
│  IncidentID │ CreatedDate │ ResolvedDate │ Status │ Priority │ Severity   │
│  Environment │ Category │ Team │ SLA_Target_Hours │ Resolution_Hours     │
│  Breach_Flag │ Reopened_Flag │ Review_Needed_Flag │ Age_Days │ ...       │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Tables

### 1. FactIncidents (fact)

- **Source:** `data/sample/incidents_sample.csv` (load as table **Incidents** in Power BI; you can rename to **FactIncidents** in the model if you prefer).
- **Grain:** One row per incident.
- **Key columns:** IncidentID (unique), CreatedDate, ResolvedDate, Status, Priority, Severity, Environment, Category, Subcategory, Team, Owner, SLA_Target_Hours, Resolution_Hours, Breach_Flag, Reopened_Flag, Review_Needed_Flag, Age_Days.
- **Role:** All measures are defined on this table. Slicers use its columns (Priority, Severity, Environment, Category, Team, Status).

**Why no separate dimension tables in MVP:** Priority, Severity, Environment, Category, Team, and Status have few distinct values and are used mainly for filtering. Keeping them as columns on the fact avoids extra relationships and is easier to explain in a portfolio. You can split them into DimPriority, DimSeverity, etc. later if the model grows.

### 2. DimDate (dimension)

- **Source:** Build in Power BI (e.g. **New table** from a date range, or **Calendar** from CreatedDate/ResolvedDate).
- **Suggested columns:** Date (PK), Year, Quarter, Month, MonthName, WeekNumber, DayOfWeek, IsWeekday. Optional: FiscalYear, FiscalQuarter if your org uses them.
- **Relationship:** DimDate[Date] → FactIncidents[CreatedDate] (many-to-one, single active relationship). Use **CreatedDate** for “when did we get the ticket” reporting.
- **Optional second relationship:** DimDate[Date] → FactIncidents[ResolvedDate] for “when was it resolved” (mark as inactive; use USERELATIONSHIP in measures when needed).

**Why a date dimension:** Enables time intelligence (same period last year, month-over-month, running totals) and clean drill-down by Year → Quarter → Month. One active relationship from CreatedDate is enough for the core KPIs.

---

## Relationships Summary

| From (Dimension) | To (Fact)    | Cardinality | Active | Use for |
|------------------|--------------|-------------|--------|---------|
| DimDate[Date]    | Incidents[CreatedDate] | Many to one | Yes | Trends, backlog at a point in time (with filter) |

No other dimensions in MVP; all other slicing is via columns on the fact table.

---

## Naming Conventions (portfolio-friendly)

- **Fact:** Incidents or FactIncidents.
- **Dimension:** DimDate.
- **Measures:** Plain English (Total Incidents, Open Incidents, SLA Breach Rate, etc.) — see `docs/dax_measures.md`.
- **Columns:** Keep CSV names (PascalCase or as imported); avoid abbreviations in labels (e.g. “Priority” not “Pty”).

---

## Optional Later Additions

- **DimDate → ResolvedDate** (inactive) for resolution trends.
- **DimPriority**, **DimCategory**, etc. if you add surrogate keys and need to track history or many attributes per dimension.

This structure supports the three dashboard pages (Executive Overview, SLA & Backlog, Root Cause & Explorer) without overengineering.
