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
