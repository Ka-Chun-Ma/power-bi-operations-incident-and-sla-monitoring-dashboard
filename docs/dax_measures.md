# Core DAX Measures

**Table name:** Assume the incident table is named **Incidents** in Power BI. If you renamed it to **FactIncidents**, replace `Incidents` with `FactIncidents` in each measure.

For each measure: **name**, **DAX**, and **business question it answers**. Naming is kept clean and portfolio-friendly.

---

## 1. Total Incidents

**DAX:**
```dax
Total Incidents = COUNTROWS( Incidents )
```

**Business question:** How many incidents do we have in total (for the current filters)?

---

## 2. Open Incidents

**DAX:**
```dax
Open Incidents =
COUNTROWS(
    FILTER( Incidents, NOT( Incidents[Status] IN { "Resolved", "Closed" } ) )
)
```

**Business question:** How many incidents are currently open (not yet resolved or closed)?

---

## 3. Resolved Incidents

**DAX:**
```dax
Resolved Incidents =
COUNTROWS(
    FILTER( Incidents, Incidents[Status] IN { "Resolved", "Closed" } )
)
```

**Business question:** How many incidents have been resolved or closed?

---

## 4. SLA Breach Rate

**DAX:**
```dax
SLA Breach Rate =
DIVIDE(
    CALCULATE( COUNTROWS( Incidents ), Incidents[Breach_Flag] = 1 ),
    CALCULATE( COUNTROWS( Incidents ), NOT( ISBLANK( Incidents[Resolution_Hours] ) ) ),
    0
)
```
Format as **Percentage** (e.g. 0.15 → 15%).

**Business question:** Of all resolved incidents, what share breached the SLA?

---

## 5. Average Resolution Hours

**DAX:**
```dax
Average Resolution Hours =
AVERAGE( Incidents[Resolution_Hours] )
```
Consider wrapping in `CALCULATE( ..., Incidents[Status] IN { "Resolved", "Closed" } )` if you have rows with blank Resolution_Hours and want to exclude them explicitly.

**Business question:** On average, how many hours did it take to resolve incidents (for the current filters)?

---

## 6. Median Resolution Hours

**DAX:**
```dax
Median Resolution Hours =
MEDIAN( Incidents[Resolution_Hours] )
```
Again, filter to resolved/closed only if your data has blanks in Resolution_Hours.

**Business question:** What is the typical (median) resolution time in hours? (Less influenced by outliers than average.)

---

## 7. Critical Incident Count

**DAX:**
```dax
Critical Incident Count =
CALCULATE( COUNTROWS( Incidents ), Incidents[Severity] = "Critical" )
```

**Business question:** How many critical-severity incidents are there?

---

## 8. Backlog Count

**DAX:**
```dax
Backlog Count = [Open Incidents]
```
Or define once and reuse: backlog is the same as open incidents.

**Business question:** How many tickets are in the backlog (open)?

---

## 9. Backlog Over 7 Days

**DAX:**
```dax
Backlog Over 7 Days =
COUNTROWS(
    FILTER(
        Incidents,
        NOT( Incidents[Status] IN { "Resolved", "Closed" } )
            && Incidents[Age_Days] > 7
    )
)
```

**Business question:** How many open incidents have been open for more than 7 days?

---

## 10. Reopened Incident Rate

**DAX:**
```dax
Reopened Incident Rate =
DIVIDE(
    CALCULATE( COUNTROWS( Incidents ), Incidents[Reopened_Flag] = 1 ),
    [Total Incidents],
    0
)
```
Format as **Percentage**.

**Business question:** What proportion of incidents were reopened at least once?

---

## Optional: Explicit Resolved Count for Rates

If you want **SLA Breach Rate** and resolution-time measures to consider only resolved/closed rows without relying on blank Resolution_Hours, use a base measure and reference it:

**DAX:**
```dax
Resolved Count =
CALCULATE( COUNTROWS( Incidents ), Incidents[Status] IN { "Resolved", "Closed" } )
```

Then:

```dax
SLA Breach Rate =
DIVIDE(
    CALCULATE( [Resolved Count], Incidents[Breach_Flag] = 1 ),
    [Resolved Count],
    0
)
```

**Average Resolution Hours** (resolved only):

```dax
Average Resolution Hours =
CALCULATE( AVERAGE( Incidents[Resolution_Hours] ), Incidents[Status] IN { "Resolved", "Closed" } )
```

---

## Quick Reference

| Measure | Purpose |
|---------|---------|
| Total Incidents | Count of all incidents |
| Open Incidents | Count not Resolved/Closed |
| Resolved Incidents | Count Resolved or Closed |
| SLA Breach Rate | % of resolved that breached SLA |
| Average Resolution Hours | Mean resolution time (hours) |
| Median Resolution Hours | Median resolution time (hours) |
| Critical Incident Count | Count where Severity = Critical |
| Backlog Count | Same as Open Incidents |
| Backlog Over 7 Days | Open incidents with Age_Days > 7 |
| Reopened Incident Rate | % of incidents with Reopened_Flag = 1 |

These measures support the three dashboard pages (Executive Overview, SLA & Backlog, Root Cause & Explorer) and answer: *Where are incidents concentrated? Which categories, environments, or priorities drive SLA breaches and backlog? What should the team prioritise first?*
