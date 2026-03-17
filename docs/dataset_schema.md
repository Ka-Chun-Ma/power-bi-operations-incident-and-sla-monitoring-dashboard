# Dataset Schema (MVP)

**Scope:** One table, incident-level grain. Enough to drive the 3-page dashboard (Executive Overview, SLA & Backlog, Root Cause & Explorer).

---

## Table: Incidents (flat)

| Column | Type | Description / assumptions |
|--------|------|---------------------------|
| **IncidentID** | Text | Unique ticket id (e.g. INC001234). Primary key. |
| **CreatedDate** | Date | When the incident was logged. Used for trends and ageing. |
| **ResolvedDate** | Date | When the incident was closed. Blank if Status is not Resolved/Closed. |
| **Status** | Text | e.g. New, In Progress, Pending, Resolved, Closed. Drives Open vs Resolved counts. |
| **Priority** | Text | Business priority: P1, P2, P3, P4 (or High, Medium, Low). Used for prioritisation views. |
| **Severity** | Text | Technical impact: Critical, High, Medium, Low. Used for severity distribution and critical count. |
| **Environment** | Text | Production, UAT, Test, Dev. For environment risk and filtering. |
| **Category** | Text | Top-level category (e.g. Access, Performance, Data, Integration). For root-cause views. |
| **Subcategory** | Text | Optional finer bucket. Can be blank in MVP. |
| **Team** | Text | Owning team or queue (e.g. Platform, Data, Support). For ownership analysis. |
| **Owner** | Text | Optional assignee name. Can be blank. |
| **SLA_Target_Hours** | Number | Contracted resolution time in hours (e.g. 4, 8, 24). Used for breach logic. |
| **Resolution_Hours** | Number | Actual hours from Created to Resolved. Blank if not resolved. |
| **Breach_Flag** | Integer | 1 = SLA breached, 0 = not breached. Derived: 1 if Resolution_Hours > SLA_Target_Hours (for resolved tickets). |
| **Reopened_Flag** | Integer | 1 = ticket was reopened, 0 = never reopened. For reopened rate KPI. |
| **Review_Needed_Flag** | Integer | 1 = needs review, 0 = no. Optional; can be 0 for all in MVP. |
| **Age_Days** | Integer | Days from CreatedDate to today (open) or to ResolvedDate (resolved). For backlog ageing. |

---

## MVP assumptions

- **Single table:** No separate dimension tables at this stage. Dimensions (Priority, Severity, Environment, Category, Team, Status) are columns; Power BI can still use them for slicing.
- **Dates:** Date only (no time). Resolution_Hours is numeric; for MVP it can be rounded or calculated from dates.
- **Breach:** Only for resolved incidents. Open incidents are “at risk” but not “breached” until resolved late.
- **Age_Days:** Calculated at export/sample generation time. In Power BI you can replace with a calculated column or measure if you prefer.
- **Subcategory / Owner:** Optional; allow blank for smaller sample data.

---

## CSV format for Power BI

- File: `data/sample/incidents_sample.csv`
- Encoding: UTF-8
- Delimiter: comma
- Header row: yes
- Date format: YYYY-MM-DD (e.g. 2025-01-15)

This schema supports: Total/Open/Resolved counts, SLA breach rate, resolution hours (avg/median), critical count, backlog count, backlog over 7 days, reopened rate, and slicing by Date, Priority, Severity, Environment, Category, Team, Status.
