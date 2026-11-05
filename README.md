# Sales Explorer

Streamlit dashboard for Activity 1 of the Web Implementation module.

## Run locally

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe make_data.py
.\.venv\Scripts\python.exe -m streamlit run session1\activity1_starter\app.py
```

The dashboard includes region and category filters, KPI cards, daily units,
the top 10 SKUs by revenue, and an expandable table of filtered rows.

## Activity 2

The refactored version is in `session1/activity2_solution/` and can be run with:

```powershell
.\.venv\Scripts\python.exe -m streamlit run session1\activity2_solution\app.py
```

Compared with the kit's `session1/activity2_solution`, this version keeps
`sales_daily.csv` at the repository root instead of inside `data/`. This
preserves the CSV placement used by Activity 1 and makes the deployed app
work without copying another dataset. The loader therefore uses a repository
relative default path rather than the kit's `data/sales_daily.csv` path.

The kit uses an environment variable fallback (`SALES_CSV`) for the CSV path;
this version omits it because the public app has one fixed dataset and no
deployment secret or alternate data source is needed. The cleaning, cache,
chart-builder, filter-key, and empty-selection behavior otherwise follows the
kit's solution.
