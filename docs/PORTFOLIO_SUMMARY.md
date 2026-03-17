# Portfolio Summary: Power BI Operations Incident and SLA Monitoring Dashboard

Use this document for job applications and interviews (Data Analyst / Reporting / Operations Support roles in Australia). Wording is kept truthful and professional; no inflated impact claims.

---

## 1. Portfolio case study summary

**Project:** Power BI Operations Incident and SLA Monitoring Dashboard  

**Context:** I built this as a portfolio project to demonstrate how I approach operations reporting: defining KPIs, designing a simple data model, and structuring a multi-page dashboard so that both leadership and operations teams can answer “How are we doing?” and “What should we prioritise?”

**What I did:**

- Defined a single-table incident schema (created/resolved dates, status, priority, severity, environment, category, team, SLA target, resolution hours, breach and ageing flags) and documented it with a data dictionary.
- Generated a reproducible sample dataset (300–500 rows) in Python with realistic patterns: higher breach rates in Production and in certain categories, spread of backlog ageing, and a sensible priority mix. The script is in the repo so the data can be regenerated with different parameters.
- Recommended a minimal star-style model (one fact table plus a date dimension) and wrote DAX measures for core KPIs: total/open/resolved incidents, SLA breach rate, average and median resolution hours, critical count, backlog count, backlog over 7 days, and reopened rate.
- Designed three report pages: (1) Executive Overview—high-level KPIs and trends; (2) SLA and Backlog Analysis—breach and resolution metrics plus ageing; (3) Root Cause and Ticket Explorer—category and team breakdowns plus ticket-level detail. Each page has a clear purpose and documented wireframes.

**Outcome:** A self-contained, recruiter-friendly repo with schema docs, sample data, DAX, and wireframes. The report is built in Power BI using the provided CSV and can be shown in a portfolio or interview. I did not use production data; all figures are from synthetic data for demonstration only.

**Skills demonstrated:** Requirements framing (business questions), data modelling (schema and star-style design), KPI definition, DAX (aggregations and rates), report structure and stakeholder-level storytelling, documentation and reproducibility (Python script, data dictionary, wireframes).

---

## 2. Resume bullet points (use 2)

Choose two that best fit the role. Adjust the first line if you use a different job title.

- **Designed and documented an operations incident and SLA monitoring dashboard (Power BI)**—defined incident-level schema and data dictionary, built a reproducible sample dataset in Python, implemented a star-style model and DAX measures for volume, breach rate, resolution time, and backlog ageing, and structured three report pages (executive overview, SLA/backlog analysis, root-cause explorer) with clear KPIs and wireframes for stakeholder and operations use.

- **Delivered end-to-end reporting documentation for a portfolio operations dashboard**—from schema and star-schema recommendation through DAX measure definitions (with business-question framing) to page-level wireframes and a data dictionary, enabling a recruiter or hiring manager to understand the approach without running the report.

Use one bullet if space is limited; both together emphasise design + documentation and technical delivery.

---

## 3. Interview explanation of the project

**Suggested script (about 60–90 seconds):**

*“This is a portfolio project I built to show how I approach operations reporting and SLA monitoring. The idea is: an operations or support team needs to see where incidents are concentrated, where we’re breaching SLA, and what’s ageing in the backlog so they know what to prioritise.*

*I started by defining the business questions—volume, breach rate, resolution time, backlog, and root cause by category and team—then designed a single incident-level schema and documented it with a data dictionary. Because I didn’t have access to real ticketing data, I wrote a Python script that generates a few hundred rows of realistic sample data: for example, higher breach rates in Production and in certain categories, and a spread of open tickets by age. That way the dashboard can be built and demoed without any confidential data.*

*In Power BI I used a simple star-style model—one fact table and a date dimension—and wrote DAX for the main KPIs: total, open, and resolved incidents, SLA breach rate, average and median resolution hours, critical count, backlog and backlog over seven days, and reopened rate. The report has three pages: an executive overview with high-level KPIs and trends, an SLA and backlog page with breach and ageing detail, and a root-cause explorer with category and team breakdowns and a ticket-level table.*

*The repo has the schema, star-schema note, DAX, wireframes, and the data-generation script, so the approach is reproducible and easy to walk through in an interview. I’d be happy to show the report or the documentation and talk through any part in more detail.”*

**If they ask “What was the impact?” or “What was the outcome?”**

*“This was a portfolio piece, so there’s no production deployment or business impact to cite. The outcome was a complete, documented design and a working report on sample data that demonstrates how I’d approach this kind of dashboard in a real role: clear business questions, a simple data model, defined KPIs, and a structure that works for both leadership and operations teams.”*

**If they ask “Why these three pages?”**

*“The first page answers ‘How are we doing overall?’—volume, backlog, SLA health. The second focuses on ‘Where are we missing SLA and where is the backlog at risk?’—breach rate, resolution time, ageing. The third supports ‘Where are incidents concentrated and what should we look at?’—category, team, and ticket-level exploration. So it’s a story: state of play, then SLA and backlog, then root cause and prioritisation.”*

---

## Notes for Australian applications

- **Spelling:** Documentation and this summary use Australian spelling (e.g. prioritise, organisation, analyse) where it appears in prose.
- **Tone:** Factual and professional; no claims about “reducing incidents by X%” or “saving Y hours”—the project uses synthetic data and is presented as a portfolio demonstration.
- **Tailoring:** For governance or data quality roles, emphasise schema design, data dictionary, and reproducibility. For reporting/BI roles, emphasise DAX, KPI design, and the three-page structure. For operations support, emphasise the business questions (volume, breach, backlog, prioritisation) and the SLA/backlog page.
