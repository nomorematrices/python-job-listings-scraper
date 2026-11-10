"""Scrape job listings from the Fake Python Jobs website."""

import csv
from pathlib import Path

import requests
from bs4 import BeautifulSoup


URL = "https://realpython.github.io/fake-jobs/"
OUTPUT_FILE = Path(__file__).with_name("jobs.csv")
FIELDNAMES = ["job_title", "company_name", "location", "job_link"]


def get_text(element) -> str:
    """Return cleaned element text, or N/A when the element is missing."""
    return element.get_text(strip=True) if element else "N/A"


def fetch_page(url: str = URL) -> str:
    """Download a page and return its HTML."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text


def parse_jobs(html: str) -> list[dict[str, str]]:
    """Extract job information from the supplied HTML."""
    soup = BeautifulSoup(html, "html.parser")
    jobs_data = []

    for job in soup.select("div.card"):
        title_element = job.select_one("h2.title.is-5")
        company_element = job.select_one("h3.subtitle.is-6.company")
        location_element = job.select_one("p.location")
        link_element = job.find("a", string=lambda text: text and text.strip() == "Apply")

        jobs_data.append(
            {
                "job_title": get_text(title_element),
                "company_name": get_text(company_element),
                "location": get_text(location_element),
                "job_link": link_element.get("href", "N/A") if link_element else "N/A",
            }
        )

    return jobs_data


def save_to_csv(jobs: list[dict[str, str]], output_file: Path = OUTPUT_FILE) -> None:
    """Write all job listings to a UTF-8 CSV file."""
    with output_file.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(jobs)


def main() -> None:
    """Run the scraper and save its results."""
    try:
        html = fetch_page()
        jobs = parse_jobs(html)
        save_to_csv(jobs)
    except requests.RequestException as error:
        print(f"Unable to download job listings: {error}")
        return
    except OSError as error:
        print(f"Unable to save the CSV file: {error}")
        return

    print("Scraping completed successfully!")
    print(f"Total jobs collected: {len(jobs)}")
    print(f"Data saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
