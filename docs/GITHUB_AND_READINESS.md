# GitHub Setup & Portfolio Readiness

Use this page to configure the repo for recruiters and to track what’s still missing before the project feels portfolio-ready.

---

## 1. GitHub About description

Paste into the repo **About** field (short description, right of the repo name). GitHub allows a short description; the first line below fits typical limits.

**Option A (short):**
```
Power BI portfolio: operations incident & SLA monitoring. Schema, sample data, DAX, 3-page wireframes. Data Analyst / reporting focus.
```

**Option B (one line):**
```
Operations incident and SLA monitoring dashboard (Power BI). Schema, DAX, wireframes, sample data. Data Analyst portfolio.
```

**Option C (explicit recruiter angle):**
```
Recruiter-friendly Power BI portfolio: incident/SLA dashboard with documented schema, DAX, wireframes. Built for Data Analyst roles.
```

Pick one; adjust if you add a live report link or screenshot later.

---

## 2. Suggested GitHub topics (8–10)

Add these in **About → Topics** so the repo is discoverable and signals role fit:

| Topic | Why |
|-------|-----|
| `power-bi` | Primary tool. |
| `powerbi` | Alternate spelling; some people search this. |
| `data-analytics` | Role alignment. |
| `dashboard` | Deliverable type. |
| `kpi` | Shows KPI design focus. |
| `sla` or `sla-monitoring` | Domain. |
| `reporting` | Role alignment. |
| `data-modelling` | Schema/star schema. |
| `dax` | Measure logic. |
| `portfolio` | Sets expectation: not production. |

**Suggested set (8–10):** `power-bi`, `powerbi`, `data-analytics`, `dashboard`, `kpi`, `sla`, `reporting`, `data-modelling`, `portfolio`.

Drop one or two if the UI limits topics; keep `power-bi`, `data-analytics`, `dashboard`, `portfolio`.

---

## 3. Checklist: what’s still missing for portfolio-ready

Use this to decide what to do before sharing the repo with recruiters or in applications.

| # | Item | Status / note |
|---|------|----------------|
| 1 | **Screenshot(s) of the built report** | Not in repo. At least one screenshot (e.g. Executive Overview) strongly helps 30–60 second understanding. |
| 2 | **README is recruiter-scannable** | Done. At-a-glance, what’s inside, and recruiter link near the top. |
| 3 | **Schema and data dictionary** | Done. |
| 4 | **Sample data and regeneration script** | Done. |
| 5 | **DAX and star schema documented** | Done. |
| 6 | **Wireframes for all three pages** | Done. |
| 7 | **Portfolio summary / resume / interview notes** | Done. |
| 8 | **Built .pbix or live report link** | Optional. Improves credibility if you share a link or “report available on request.” |
| 9 | **Formal KPI definitions doc** | Optional. KPIs are defined in DAX and data dictionary; a standalone `kpi_definitions.md` would be redundant for MVP. |
| 10 | **Website URL in GitHub About** | Optional. If you host the report or a one-pager, add the URL in About. |

---

## 4. Prioritised: impact vs effort

Prioritise missing or optional work by **impact** (how much it helps a hiring manager) and **effort** (time to do it). Focus on high impact, low effort first.

| Priority | Item | Impact | Effort | Action |
|----------|------|--------|--------|--------|
| **P1** | Add 1–2 screenshots of the built report to README or `docs/screenshots/` | High | Low | Build the report in PBI, export PNG of Executive Overview (and optionally SLA page). Add to README or link from README. |
| **P2** | Set GitHub About description and topics | High | Low | Copy from sections 1 and 2 above; paste in repo About and Topics. |
| **P3** | Add “Report available on request” or link if you host it | Medium | Low | One line in README or About. Only if you’re happy to share the .pbix or a link. |
| **P4** | Optional: `docs/screenshots/` folder with 3 page captures | Medium | Low | If you already have the report built, capture all three pages for consistency. |
| **P5** | Optional: `kpi_definitions.md` | Low | Low | Only if you want a single “definition of each KPI” doc; current docs already cover this. |
| **P6** | Optional: Publish report (e.g. PBI Service) and add URL | Medium | Medium | Best for “live” portfolio; not required for portfolio-ready. |
| **P7** | Optional: Add .pbix to repo or `powerbi/` folder | Low | Low | Large binary; many prefer “on request” or link. |

**Summary:** To feel portfolio-ready, do **P1** (screenshots) and **P2** (About + topics). The rest is optional polish.

---

**North star:** A hiring manager can understand what you built and how you think within 30–60 seconds. Screenshots and a clear About/topics get you most of the way there without overbuilding.
