# Scope and Priorities

This document defines how the project is scoped. Use it to avoid overbuilding and to keep the repo recruiter-friendly.

**North star:** *What would make a hiring manager understand my capability within 30–60 seconds?*

---

## Prioritise

- **Business clarity** — Clear business questions, plain-English KPIs, and a story (overview → SLA/backlog → root cause). No jargon for its own sake.
- **Clean data model** — One fact table, one date dimension, simple relationships. Schema and assumptions documented.
- **Strong KPI logic** — Each measure has a defined meaning and answers a specific question. DAX is readable and correct, not clever.
- **Practical dashboard structure** — Three pages with distinct purposes; filters and layouts that match how the audience would use the report.
- **Recruiter readability** — README, data dictionary, wireframes, and portfolio summary are easy to scan. A hiring manager can assess the approach without running Power BI.

---

## Deprioritise

- **Advanced AI features** — No LLM-driven insights, auto-narrative, or AI-specific automation in the dashboard or docs. The repo may contain dev tools (e.g. in `tools/`); they are not part of the portfolio story.
- **Unnecessary automation** — Only the data-generation script is needed to reproduce the sample data. No pipelines, schedulers, or extra tooling unless clearly justified.
- **Complex scripting** — Python script is minimal (stdlib, one CSV). No heavy ETL, ML, or framework bloat.
- **Excessive visual gimmicks** — No custom themes, animations, or decorative elements that distract from the message. Standard Power BI visuals used sensibly.
- **Unrealistic business claims** — No “reduced incidents by X%” or “saved Y hours.” Data is synthetic; outcomes are described as portfolio deliverables only.

---

## In practice

- When adding something, ask: *Does this help a hiring manager see my capability quickly?* If not, skip it or move it out of the main narrative.
- When in doubt, choose the simpler option: one table over many, clear labels over abbreviations, fewer pages over more.
- Keep documentation truthful. If something is simulated or assumed, say so.

This keeps the project **portfolio-sized** and **recruiter-optimised** without turning it into an enterprise or AI showcase.
