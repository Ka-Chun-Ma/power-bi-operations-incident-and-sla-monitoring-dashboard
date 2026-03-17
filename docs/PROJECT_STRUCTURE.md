# Repository Folder Structure

**Project:** Power BI Operations Incident and SLA Monitoring Dashboard  
**Purpose:** Recruiter-friendly portfolio; MVP scope; clear separation of data, design, and docs.

---

## Proposed Structure

```
power-bi-operations-incident-and-sla-monitoring-dashboard/
├── data/
│   ├── raw/                    # Unchanged source files (if you add real exports later)
│   └── sample/                 # Generated sample CSV for the dashboard
├── docs/
│   ├── PROJECT_STRUCTURE.md    # This file
│   ├── dataset_schema.md       # Column definitions and assumptions
│   ├── star_schema.md          # Fact/dimension model for Power BI
│   ├── kpi_definitions.md      # Business definitions of each KPI
│   ├── dax_measures.md         # Suggested DAX with short explanations
│   └── wireframes/             # Page-by-page layout (e.g. Mermaid or text mockups)
│       ├── page1_executive_overview.md
│       ├── page2_sla_backlog.md
│       └── page3_root_cause_explorer.md
├── scripts/
│   └── generate_sample_data.py # Regenerates data/sample/ incident CSV
├── tools/                      # Existing Cursor/utility scripts (unchanged)
├── .devcontainer/              # Existing (unchanged)
├── .github/                    # Existing (unchanged)
├── .cursorrules                # Existing (unchanged)
├── .env                        # Existing (unchanged)
├── requirements.txt            # Existing (unchanged)
└── README.md                   # Main project README for GitHub
```

**Note:** The `.pbix` file is not stored in the repo by default (binary, large, merge-unfriendly). You can add a `powerbi/` folder and commit a `.pbix` if you want recruiters to open it; otherwise, README + screenshots + live report link are enough.

---

## Why Each Folder Exists

| Folder / file | Reason |
|---------------|--------|
| **`data/raw/`** | Holds original source files (e.g. CSV exports from a ticketing system). Keeps a single source of truth before any transformation. For the portfolio, it can stay empty or hold a copy of the sample data you treat as “raw.” |
| **`data/sample/`** | Holds the **implementation-ready sample CSV** used in Power BI. Naming it “sample” makes it obvious this is synthetic data for the portfolio. One file (e.g. `incidents_sample.csv`) keeps the project simple. |
| **`docs/`** | Central place for design and definitions: schema, star model, KPIs, DAX notes, wireframes. Recruiters and you can find everything without opening the report. |
| **`docs/wireframes/`** | One file per dashboard page (Executive Overview, SLA & Backlog, Root Cause & Explorer). Supports a consistent 3-page story and clear interview narrative. |
| **`scripts/`** | A single script (e.g. `generate_sample_data.py`) that rebuilds the sample CSV from the schema. Shows reproducibility and makes it easy to change row count or logic later. |
| **`tools/`** | Left as-is for Cursor/LLM/web/scraper utilities. Not part of the Power BI deliverable. |
| **Root config files** | `.cursorrules`, `.env`, `requirements.txt`, `.github`, `.devcontainer` stay at root; no need to move them for this portfolio. |

---

## Optional Additions (if you want them later)

- **`powerbi/`** – Store the `.pbix` and optionally export PBI template (PBIT) or dataset definition if you want versioned “structure” without the full binary.
- **`docs/screenshots/`** – Export PNGs of each dashboard page for README and LinkedIn.
- **`data/processed/`** – Only if you introduce a separate ETL step (e.g. Python cleans raw → processed, then Power BI uses processed). Not required for MVP.

---

## What Goes Where (Quick Reference)

| Deliverable | Location |
|-------------|----------|
| Sample incident CSV | `data/sample/incidents_sample.csv` |
| Schema & assumptions | `docs/dataset_schema.md` |
| Star schema (fact/dim) | `docs/star_schema.md` |
| KPI definitions | `docs/kpi_definitions.md` |
| DAX measures | `docs/dax_measures.md` |
| Page layouts | `docs/wireframes/page1_*.md`, `page2_*.md`, `page3_*.md` |
| Data generation | `scripts/generate_sample_data.py` |
| How to run / what the project is | `README.md` |

This structure keeps the repo **flat enough** for recruiters to navigate and **organized enough** to demonstrate data structure, documentation, and reproducibility in 1–2 weeks.
