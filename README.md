# Python Job Listings Scraper

A beginner-friendly Python web scraper that collects job listings from the
[Fake Python Jobs](https://realpython.github.io/fake-jobs/) website and exports
the results to a CSV file.

This project is based on the
[Job Listings Scraper project from roadmap.sh](https://roadmap.sh/projects/job-listings-scraper).

## Data collected

For every job posting, the scraper extracts:

- Job title
- Company name
- Location
- Job detail page URL

Missing fields are stored as `N/A` so that one incomplete listing does not stop
the scraper.

## Requirements

- Python 3.9 or newer
- `requests`
- `beautifulsoup4`

## Installation

Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows, activate it with:

```powershell
.venv\Scripts\activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the scraper from the project directory:

```bash
python scraper.py
```

The script creates `jobs.csv` in the same directory. Existing output is
replaced each time the scraper runs.

Example output:

```csv
job_title,company_name,location,job_link
Senior Python Developer,"Payne, Roberts and Davis","Stewartbury, AA",https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html
```

## Project structure

```text
.
├── README.md
├── requirements.txt
├── scraper.py
└── jobs.csv
```

The code is separated into functions for downloading HTML, parsing listings,
and writing CSV data, making each step easier to read, reuse, and test.
