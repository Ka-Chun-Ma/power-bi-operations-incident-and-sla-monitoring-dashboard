# Data Dictionary: incidents_sample.csv

Short reference for the sample incident dataset used in the Power BI Operations Incident and SLA Monitoring Dashboard.

| Column | Type | Values / rules |
|--------|------|----------------|
| **IncidentID** | Text | Unique id, format INC000001–INC000420. Primary key. |
| **CreatedDate** | Date | Log date (YYYY-MM-DD). Range in sample: ~90 days before reference date. |
| **ResolvedDate** | Date | Close date (YYYY-MM-DD). Blank when Status is New / In Progress / Pending. |
| **Status** | Text | New, In Progress, Pending, Resolved, Closed. |
| **Priority** | Text | P1, P2, P3, P4. Drives SLA target. |
| **Severity** | Text | Critical, High, Medium, Low. |
| **Environment** | Text | Production, UAT, Test, Dev. |
| **Category** | Text | Access, Performance, Data, Integration. |
| **Subcategory** | Text | Optional; e.g. Login, Permissions, Timeout, Sync, Quality. Often blank. |
| **Team** | Text | Platform, Data, Support, Infrastructure. |
| **Owner** | Text | Assignee name or blank. |
| **SLA_Target_Hours** | Number | 4 (P1), 8 (P2), 24 (P3), 48 (P4). |
| **Resolution_Hours** | Number | Actual hours to resolve. Blank if not resolved. |
| **Breach_Flag** | 0 | 1 | 1 = resolved past SLA (Resolution_Hours > SLA_Target_Hours); 0 otherwise. |
| **Reopened_Flag** | 0 | 1 | 1 = ticket reopened at least once; 0 = never reopened. |
| **Review_Needed_Flag** | 0 | 1 | 1 = flagged for review; 0 = no. |
| **Age_Days** | Integer | For open: days from CreatedDate to reference date. For resolved: days from Created to Resolved. |

**Reference date for ageing:** 2025-03-10 (used when generating the sample).

**File:** `data/sample/incidents_sample.csv` · UTF-8 · Comma-delimited · Header row.
