# 🏏 Cricbuzz LiveStats: Real-Time Cricket Insights & SQL-Based Analytics

**Real-time cricket insights and SQL-based analytics.**
A multi-page Streamlit dashboard that combines live data from the Cricbuzz API (via RapidAPI) with a SQL database: live scorecards, top player stats, 27 analytical queries covering 25 SQL questions, and full CRUD management.

> **Author:** [Ananya](https://github.com/ananya39836-blip)
> **Repository:** [GitHub Repository](https://github.com/ananya39836-blip/cricbuzz-livestats)
> **Live Demo:** [Streamlit App](https://cricbuzz-livestats-ananya.streamlit.app)
> **Walkthrough Video:** [Project Demo Recording](https://drive.google.com/file/d/YOUR_RECORDING_LINK/view?usp=sharing)

---

## Table of Contents
1. [Features](#features)
2. [Screenshots](#screenshots)
3. [Tech Stack](#tech-stack)
4. [Installation Guide](#installation-guide)
5. [API Setup](#api-setup)
6. [Database Setup](#database-setup)
7. [Running the App](#running-the-app)
8. [Folder Structure](#folder-structure)
9. [Architecture](#architecture)
10. [The 25 SQL Questions](#the-25-sql-questions)
11. [Testing](#testing)
12. [Deployment](#deployment)
13. [Troubleshooting](#troubleshooting)
14. [Project Status](#project-status)
15. [Future Improvements](#future-improvements)

---

## Features

| Page | What it does |
|---|---|
| **Home** (`app.py`) | Project overview, architecture summary, system status diagnostics (API key, DB connectivity), row counts, and quick navigation |
| **Live Matches** | Ongoing international and domestic fixtures fetched via Cricbuzz API, complete with live scores, match status, venues, and detailed scorecards |
| **Top Stats** | Batting and bowling leaderboards from Cricbuzz API (most runs, highest scores, wickets, averages), visualized via interactive tables and Plotly charts |
| **SQL Analytics** | Comprehensive analytics solving all 25 problem statements with formatted SQL queries, tabular data views, Plotly visualizations, CSV download, and a safe read-only custom SQL execution console |
| **CRUD Operations** | Form-based interface enabling Create, Read, Update, and Delete operations for players (with career stats) and matches (with match results) |
| **Settings** | API connection diagnostics, pipeline data loaders, venue-capacity CSV importer, cache clearing, and database reset |

**Engineering Highlights:**
- **Layered Architecture:** Strict separation between Presentation (`pages/`), Business Logic (`services/`), API (`api/`), and Persistence (`database/`).
- **SQL Security:** Strict parameterized queries, transactions with automated rollbacks, and a dedicated read-only connection capped at 1,000 rows for custom SQL queries.
- **Resilience & Rate Limits:** Requests with exponential backoff and jitter for transient RapidAPI errors, paired with multi-tier TTL caching.
- **Robust Error Handling:** Centralized logging to `logs/app.log` and user-friendly error boundaries in the UI.

---

## Screenshots

> *Screenshots located in the `images/` directory.*

| Home Dashboard | Live Matches & Scorecards |
|:---:|:---:|
| ![Home](images/home.png) | ![Live Matches](images/live_matches.png) |

| Top Player Stats | SQL Analytics & Visualisations |
|:---:|:---:|
| ![Top Stats](images/top_stats.png) | ![SQL Analytics](images/sql_analytics.png) |

| CRUD Data Management | System Settings & Ingestion |
|:---:|:---:|
| ![CRUD](images/crud.png) | ![Settings](images/settings.png) |

---

## Tech Stack

- **Language:** Python 3.10+
- **Frontend / Dashboard:** Streamlit, Streamlit Extras
- **Database:** SQLite 3.25+ (supports Window Functions; agnostic design portable to PostgreSQL/MySQL)
- **Data & ORM:** SQLAlchemy, pandas, NumPy
- **Visualisations:** Plotly Express & Plotly Graph Objects
- **HTTP / Ingestion:** `requests` with custom retry adapter
- **Testing:** pytest, pytest-cov
- **Containerization:** Docker

---

## Installation Guide

### Prerequisites
- Python 3.10 or newer
- Git
- RapidAPI account subscribed to the **Cricbuzz Cricket** API
- SQLite version 3.25 or newer (bundled with Python 3.10+). Check via:
  ```bash
  python -c "import sqlite3; print(sqlite3.sqlite_version)"
  ```

### Quickstart

```bash
# 1. Clone repository
git clone https://github.com/ananya39836-blip/cricbuzz-livestats.git
cd cricbuzz-livestats

# 2. Setup virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env              # Windows: copy .env.example .env
# Open .env and insert your RapidAPI credentials

# 5. Initialize Database (Schema, Indexes, Views, Seed Data)
python init_database.py

# 6. Run the application
streamlit run app.py
```

Access the dashboard at: `http://localhost:8501`

---

## API Setup

1. Sign up or log in at [RapidAPI](https://rapidapi.com).
2. Subscribe to the [Cricbuzz Cricket API](https://rapidapi.com/cricketapilive/api/cricbuzz-cricket).
3. Copy your API Key (`x-rapidapi-key`).
4. Configure `.env`:
   ```env
   RAPIDAPI_KEY=your_actual_rapidapi_key_here
   RAPIDAPI_HOST=cricbuzz-cricket.p.rapidapi.com
   DATABASE_URL=sqlite:///data/cricket.db
   ```
5. Test the connection inside **Settings → Test API Connection**.

---

## Database Setup

Initialize the entire schema and seed tables in one command:
```bash
python init_database.py
```

### Relational Schema (3NF)

```
TEAMS ──< MATCHES >── VENUES
  │          │  ▲
  │          │  └── SERIES
  │          └──< INNINGS ──< BATTING_PERFORMANCES >── PLAYERS
  │                    └─────< BOWLING_PERFORMANCES >── PLAYERS
  └──< PLAYERS ──< PLAYER_CAREER_STATS (one row per format)
```

- **Integrity Constraints:** Foreign keys strictly enforced (`PRAGMA foreign_keys = ON`), with domain check constraints on formats, toss decisions, and non-negative stats.
- **Optimization:** Indexes configured on `matches(match_date)`, `matches(winner_id)`, `venues(venue_id)`, and performance tables.
- **Analytical Views:** Pre-compiled views including `v_match_results`, `v_team_wins`, `v_player_summary`, and `v_player_quarterly`.

---

## Running the App

```bash
streamlit run app.py
```

Use the multi-page sidebar to navigate across the modules:
1. `app.py`: Overview & KPI Metrics
2. `pages/1_Live_Matches.py`: Cricbuzz Live Feed & Scorecards
3. `pages/2_Top_Stats.py`: Batting & Bowling Leaderboards
4. `pages/3_SQL_Analytics.py`: 25 Analytical Questions & Custom SQL
5. `pages/4_CRUD_Operations.py`: Player & Match Record Forms
6. `pages/5_Settings.py`: Pipeline Controls, Import Venue CSV, Reset DB

---

## Folder Structure

```
cricbuzz_livestats/
├── app.py                    # Streamlit application entry point & Home page
├── config.py                 # Configuration loader (reads .env / secrets)
├── init_database.py          # Database initializer (DDL + views + seed)
├── run_ingest.py             # CLI pipeline for Cricbuzz API ingestion
├── requirements.txt          # Python dependencies
├── pytest.ini                # Pytest configuration
├── Dockerfile / .dockerignore
├── .env.example              # Environment variable template
├── README.md
│
├── api/
│   ├── cricbuzz_client.py    # HTTP client (retries, rate-limits, headers)
│   └── parsers.py            # JSON responses -> relational dictionaries
│
├── database/
│   ├── connection.py         # SQLAlchemy engines (RW & safe Read-Only)
│   └── repositories.py       # CRUD data access layer
│
├── services/
│   ├── match_service.py      # Live match feeds and scorecard service
│   ├── stats_service.py      # Top leaderboards service
│   ├── ingestion_service.py  # Ingestion ETL pipelines into SQLite
│   ├── analytics_service.py  # SQL analytics executor and query loader
│   ├── admin_service.py      # CSV capacity importer and maintenance
│   └── query_catalog.py      # Metadata & definitions for 25 questions
│
├── models/
│   └── schemas.py            # Dataclasses and Pydantic validation schemas
│
├── pages/
│   ├── 1_Live_Matches.py
│   ├── 2_Top_Stats.py
│   ├── 3_SQL_Analytics.py
│   ├── 4_CRUD_Operations.py
│   └── 5_Settings.py
│
├── utils/
│   ├── db_connection.py      # Database helper wrapper
│   ├── charts.py             # Plotly graph generators
│   ├── logger.py             # Rotating file and console logger
│   └── error_handling.py     # Custom exceptions and error handlers
│
├── sql/
│   ├── schema.sql            # Table definitions
│   ├── indexes.sql           # Query optimization indexes
│   ├── views.sql             # Materialized logic views
│   ├── seed.sql              # Initial bootstrap data
│   └── queries/              # q01.sql to q25.sql (all 27 query files)
│
├── data/                     # SQLite database file and cache (git-ignored)
├── tests/                    # Unit and integration test suite
└── images/                   # UI screenshots for documentation
```

---

## The 25 SQL Questions

All 25 analytical queries are fully solved with `.sql` implementations inside `sql/queries/`:

### Beginner Level (1–8)
- **Q1:** Indian Squad Roster (Full name, playing role, batting & bowling styles)
- **Q2:** Matches Played in Last 30 Days (Match description, teams, venue, date)
- **Q3:** Top 10 ODI Run Scorers (Runs, batting average, centuries)
- **Q4:** Venues with Seating Capacity > 50,000 (Ordered by size)
- **Q5:** Total Match Wins per Team (Descending by victories)
- **Q6:** Player Count by Playing Role (Batsman, Bowler, All-rounder, Wicket-keeper)
- **Q7:** Highest Individual Batting Score per Cricket Format (Test, ODI, T20I)
- **Q8:** Cricket Series Commencing in 2024 (Host nation, match types, total fixtures)

### Intermediate Level (9–16)
- **Q9:** Premier All-Rounders (>1,000 runs AND >50 wickets across career formats)
- **Q10:** Last 20 Completed Matches (Margin, victory type, teams, winner, venue)
- **Q11:** Multi-Format Performance Matrix (Runs across Test, ODI, T20I, overall average)
- **Q12:** Home vs. Away Win Analysis (Venue country matching team country)
- **Q13:** Century Batting Partnerships (Consecutive positions with 100+ combined runs)
- **Q14:** Bowling Performance by Venue (Avg economy, total wickets, min 3 matches)
- **Q15:** Close-Match Performers (<50 runs or <5 wickets margin)
- **Q16:** Year-on-Year Batting Form Since 2020 (Average runs & strike rate per year)

### Advanced Level (17–25)
- **Q17:** Toss Advantage Analysis (% win rate broken down by Bat/Bowl first)
- **Q18:** Most Economical Limited-Overs Bowlers (ODI + T20I, min 10 matches)
- **Q19:** Batsman Consistency Scoring (Average runs and standard deviation since 2022)
- **Q20:** Multi-Format Batting Averages (Format match distribution for players with 20+ caps)
- **Q21:** Weighted Player Ranking Index:
  $$\text{Batting} = (\text{Runs} \times 0.01) + (\text{Avg} \times 0.5) + (\text{SR} \times 0.3)$$
  $$\text{Bowling} = (\text{Wickets} \times 2) + ((50 - \text{Avg}) \times 0.5) + ((6 - \text{Econ}) \times 2)$$
  $$\text{Fielding} = (\text{Catches} \times 3) + (\text{Stumpings} \times 5)$$
- **Q22:** Head-to-Head Team Prediction Matrix (Win percentages, margins, toss dynamics)
- **Q23:** Player Form & Momentum (Last 5 vs. 10 match comparison, categorical labels)
- **Q24:** Partnership Synergy Analysis (Success rate, 50+ stands, average runs)
- **Q25:** Quarterly Performance Trajectory (Rolling quarterly time-series career phase analysis)

---

## Testing

Run the test suite using `pytest`:

```bash
# Run all tests
pytest

# Run CRUD-specific tests with verbose output
pytest tests/test_crud.py -v

# Run with test coverage report
pytest --cov=. --cov-report=term-missing
```

Tests run against an in-memory or temporary database fixture, ensuring test runs never consume your RapidAPI quota or modify local data.

---

## Deployment

### Streamlit Community Cloud
1. Push this repository to GitHub.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Create a new app pointing to your repository and `app.py`.
4. In **App Settings → Secrets**, add your RapidAPI credentials:
   ```toml
   RAPIDAPI_KEY = "your_actual_key"
   RAPIDAPI_HOST = "cricbuzz-cricket.p.rapidapi.com"
   ```

### Docker
```bash
docker build -t cricbuzz-livestats .
docker run -p 8501:8501 --env-file .env cricbuzz-livestats
```

---

## Troubleshooting

| Issue | Root Cause | Solution |
|---|---|---|
| `Database not ready` | DB file uninitialized | Execute `python init_database.py` |
| `Invalid API key` | Missing / wrong RapidAPI header | Check `RAPIDAPI_KEY` in `.env` or Streamlit Secrets |
| `no such function: SQRT` | SQLite lacks native math functions | Registered automatically via `connection.py` math extension |
| `Syntax error near OVER` | SQLite version `< 3.25` | Upgrade Python/SQLite to support Window Functions |
| Empty Live Matches table | Cricbuzz API response format update | Check the *Raw API Response* expander on the Live page |

---

## Project Status

- [x] Complete Relational 3NF Database Schema, Indexes, Views, and Seed Data
- [x] Cricbuzz API Client with Exponential Backoff Retries & Rate Limiting
- [x] Full CRUD Module for Players, Career Statistics, Matches, and Results
- [x] All 25 SQL Analytical Queries fully tested and verified
- [x] Multi-Page Interactive Streamlit Dashboard with Plotly Visualizations
- [x] CSV Data Importers and Safe Read-Only Custom SQL Sandbox
- [x] Comprehensive Automated Test Suite (`pytest`)
- [x] Production Deployment Configuration (Docker & Streamlit Cloud)

---

## Future Improvements

- Automated background cron workers for continuous match score syncing.
- Multi-user authentication and role-based access control (RBAC) on the CRUD management portal.
- Machine learning match-winner prediction model incorporating live pitch conditions and real-time form.
- Automated PDF report exporter for post-match executive summaries.

---

## Acknowledgements

- Match feeds and player career data provided by the Cricbuzz Cricket API via RapidAPI.
- Built for educational, sports analytics, and database engineering purposes.
