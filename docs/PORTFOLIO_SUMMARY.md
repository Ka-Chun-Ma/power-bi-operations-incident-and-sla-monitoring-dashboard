Use this document for job applications and interviews for Data Analyst, Reporting, and Operations Support roles in Australia. The wording is kept truthful, practical, and professional, with no inflated impact claims.

---

## 1. Portfolio case study summary

**Project:** Power BI Operations Incident and SLA Monitoring Dashboard

**Context:**  
I built this portfolio project to demonstrate how I approach operations reporting: defining business questions, selecting practical KPIs, designing a simple data model, and structuring a multi-page dashboard so that both leadership and operations teams can quickly understand performance and identify what to prioritise.

**What I did:**

- Defined an incident-level dataset structure covering created and resolved dates, status, priority, severity, environment, category, team, SLA target, resolution hours, breach flags, reopened flags, and backlog ageing fields, then documented it with a data dictionary.
- Generated a reproducible synthetic dataset in Python with realistic operational patterns, including higher breach rates in Production and selected categories, a spread of backlog ageing, and a sensible priority mix. The script is included in the repository so the sample data can be regenerated with different row counts or seeds.
- Designed a minimal star-style model using one fact table and a date dimension, then created DAX measures for core KPIs including total, open, and resolved incidents, SLA breach rate, average and median resolution hours, critical incidents, backlog count, backlog over 7 days, and reopened incident rate.
- Structured the report into three pages with distinct purposes:
  - **Executive Overview** for high-level KPIs and trends
  - **SLA and Backlog Analysis** for breach concentration, resolution time, and backlog ageing
  - **Root Cause and Ticket Explorer** for category and team breakdowns, matrix views, and ticket-level exploration
- Documented the project so it is easy to review in a hiring or interview context, including schema notes, a star-schema recommendation, DAX measure definitions, and page wireframes.

**Outcome:**  
The result is a self-contained, recruiter-friendly Power BI portfolio project with sample data, documentation, DAX logic, and a working dashboard design. It is intended as a demonstration of reporting and analytical capability rather than a production deployment. No confidential or production data was used.

**Skills demonstrated:**  
Business question framing, KPI design, data modelling, DAX measure development, dashboard structuring, documentation, stakeholder-focused reporting, and reproducible sample-data generation in Python.

---

## 2. Resume bullet points (use 1-2)

Choose the version that best fits the role and available space.

- **Built a three-page Power BI operations incident and SLA monitoring dashboard** using a documented incident-level schema, reproducible synthetic data in Python, a star-style model, and DAX measures for incident volume, breach rate, resolution time, backlog ageing, and ticket-level exploration.

- **Designed and documented an operations reporting portfolio project end to end**, including schema definition, data dictionary, star-schema recommendation, KPI logic, DAX measures, and page-level dashboard structure for executive overview, SLA and backlog analysis, and root-cause exploration.

- **Developed a Power BI reporting solution for operational monitoring** that demonstrates practical analyst capability in KPI design, data modelling, dashboard storytelling, and translating incident data into stakeholder-friendly reporting views.

Use one bullet if space is tight. Use two if you want to emphasise both technical delivery and documentation quality.

---

## 3. Interview explanation of the project

**Suggested script (about 60-90 seconds):**

“This is a portfolio project I built to demonstrate how I approach operations reporting and SLA monitoring. The core problem I wanted to simulate was how an operations or support team can quickly see where incidents are concentrated, where SLA risk is building up, and what is ageing in the backlog so they can prioritise effectively.

I started by defining the business questions first, then designed an incident-level dataset and documented it with a data dictionary. Because I did not have access to real ticketing data, I wrote a Python script to generate a few hundred rows of realistic sample data with patterns such as higher breach rates in Production and variation across categories and priority levels.

In Power BI, I used a simple star-style model with one fact table and a date dimension, then created DAX measures for the main KPIs, including total, open, and resolved incidents, SLA breach rate, average and median resolution hours, critical incidents, backlog over 7 days, and reopened rate.

The dashboard is structured into three pages. The first gives an executive overview, the second focuses on SLA and backlog risk, and the third supports root-cause and ticket-level exploration. I wanted the project to be easy to review, so the repository also includes the schema, DAX, wireframes, and data-generation script.”

**If they ask, “What was the impact?” or “What was the outcome?”**

“This was a portfolio project rather than a production deployment, so I would not claim business impact. The outcome was a complete, documented reporting solution on synthetic data that shows how I would approach this type of dashboard in a real role: clear business questions, practical KPIs, a simple model, and a report structure that supports both high-level monitoring and deeper analysis.”

**If they ask, “Why did you structure it into three pages?”**

“I wanted the report to follow a clear analytical flow. The first page answers how things are performing overall. The second looks at SLA pressure and backlog risk in more detail. The third supports exploration of category, team, and ticket-level patterns. So the structure moves from overview, to diagnosis, to deeper exploration and prioritisation.”

---

## Notes for Australian applications

- **Spelling:** This summary uses Australian spelling where it appears in prose, such as prioritise, organisation, and modelling.
- **Tone:** The wording is factual and professional. It does not claim production outcomes or quantified business improvements because the project uses synthetic data for demonstration.
- **Tailoring:**  
  - For **Reporting / BI roles**, emphasise KPI design, DAX, dashboard structure, and stakeholder presentation.  
  - For **Data Quality / Governance roles**, emphasise schema design, data dictionary, documentation, and reproducibility.  
  - For **Operations Support roles**, emphasise incident concentration, SLA monitoring, backlog ageing, and prioritisation logic.