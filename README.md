# Grazioso Salvare Animal Rescue Analytics Dashboard

Interactive analytics dashboard for an animal-rescue organization. The project connects MongoDB shelter records to filtering, visualization, and mapping so users can identify animals suited to specific rescue scenarios (water, mountain/wilderness, disaster/individual tracking).

Built for CS 340 (Client/Server Development) as a practical data-analytics and full-stack data project.

---

## Problem

Rescue teams need a fast way to find animals that match training and mission criteria (breed, age, outcome history, location). Manual review of large shelter datasets is slow and error-prone. This project turns structured animal-shelter data into an interactive dashboard with filters, a sortable data table, breed distribution charts, and a map centered on selected animals.

---

## What this project demonstrates

- MongoDB data access and full CRUD operations via a reusable Python module
- Query design for filtering structured animal-shelter records
- Data loading and transformation with Pandas
- Interactive Dash data tables with sorting and row selection
- Plotly visualizations (breed distribution pie charts)
- Geospatial mapping with latitude/longitude and leaflet markers
- Translating business requirements (rescue-type profiles) into dashboard behavior
- Jupyter-based development and presentation of an interactive app

---

## Tech stack

| Category | Tools |
| --- | --- |
| Language | Python 3 |
| Database | MongoDB, PyMongo |
| Dashboard | Dash / JupyterDash, dash_table, dash-leaflet |
| Visualization | Plotly Express |
| Data | Pandas, NumPy |
| Environment | JupyterLab / Jupyter Notebook |

---

## Key files

| File | Purpose |
| --- | --- |
| `crud-python-module.py` | Base MongoDB CRUD class (`AnimalShelter`) — create and read |
| `crud-python-module6.py` | Extended CRUD (create, read, update, delete) used by later milestones |
| `project-two-dashboard.ipynb` | Main interactive dashboard (filters, table, pie chart, map) |
| `module-6-milestone.ipynb` | Milestone notebook for dashboard work |
| `penguins.csv`, `repair.csv`, `weight.csv` | Supporting datasets used in earlier modules |
| `dashboard-specifications.pdf` | Project requirements and dashboard specifications |
| Assignment `.docx` files | Course documentation and milestones |

> Credentials are not stored in the repository. The CRUD modules read the MongoDB password from the `MONGO_PASSWORD` environment variable.

---

## How the dashboard works

1. Connects to a local MongoDB instance (`aac` database, `animals` collection) using the `AnimalShelter` class.
2. Loads records into a Pandas DataFrame and displays them in a Dash data table (sortable, selectable).
3. Provides a dropdown filter for rescue type:
   - Water Rescue
   - Mountain or Wilderness Rescue
   - Disaster or Individual Tracking
   - Reset (all records)
4. Updates the table and a Plotly pie chart of breed distribution based on the active filter.
5. When a row is selected, centers a leaflet map on that animal’s latitude/longitude and shows breed and name in a popup.

---

## Setup (local)

### Prerequisites

- Python 3.8+
- MongoDB running locally (default port 27017)
- A populated `aac.animals` collection (or equivalent)

### Install dependencies

```bash
pip install pymongo pandas numpy plotly dash jupyter-dash dash-leaflet
```

### Configure connection

Set the MongoDB password (and adjust host/user/db in the CRUD module if needed):

```bash
export MONGO_PASSWORD="your_password_here"
```

### Run the dashboard

Open `project-two-dashboard.ipynb` in JupyterLab or Jupyter Notebook and run the cells in order. The app starts a local Dash server (proxy URL may vary by environment).

**Note:** The notebook imports `AnimalShelter` from a module named `CRUD_Python_Module`. Ensure the import path matches your local filename (e.g. rename or adjust the import to match `crud-python-module.py` / `crud-python-module6.py`).

---

## Project structure

```
cs340-data-analytics/
├── README.md
├── .gitignore
├── crud-python-module.py          # Base CRUD
├── crud-python-module6.py         # Extended CRUD (C/R/U/D)
├── project-two-dashboard.ipynb    # Main dashboard
├── module-6-milestone.ipynb
├── penguins.csv / repair.csv / weight.csv
├── dashboard-specifications.pdf
└── module-*-assignment.docx / milestones
```

---

## Insights and outcomes

- Demonstrates end-to-end flow from database → query layer → interactive UI.
- Shows how rescue-type criteria can be encoded as filters and reflected immediately in tables, charts, and maps.
- Emphasizes readable data presentation for non-technical stakeholders (clear table, simple chart, location context).

---

## Future improvements

- Add dedicated query methods (`water_rescue`, `mountain_rescue`, etc.) in the CRUD module so filters are fully encapsulated in the data layer.
- Align notebook import names with repository file names for out-of-the-box cloning.
- Export static screenshots or a recorded demo for portfolio viewers who cannot run MongoDB locally.
- Optional: containerize MongoDB + app for one-command setup.

---

## Author

**Ahmed Ahmed**  
Computer Science · Data Analytics · Southern New Hampshire University  

- Portfolio: [ahmed306758-droid.github.io/ahmedporfolio](https://ahmed306758-droid.github.io/ahmedporfolio/)  
- GitHub: [github.com/ahmed306758-droid](https://github.com/ahmed306758-droid)  
- Email: asquared.alist@gmail.com  

---

*Coursework project. Credentials and sensitive connection details were removed before publication.*
