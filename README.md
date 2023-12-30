# Website Information Extractor

This Python script extracts information from a list of websites, including location, names, email, and social media links. It utilizes web scraping with BeautifulSoup, IP geolocation with ipapi.co, and named entity recognition with spaCy.

## Prerequisites

- Python 3.x
- Required libraries: requests, bs4 (BeautifulSoup), socket, spacy, prettytable

Install the required libraries using the following command:

```bash
pip install requests beautifulsoup4 spacy prettytable
python -m spacy download en_core_web_sm
```

## Features

-Extracts location information using IP geolocation.
-Scrapes website content with BeautifulSoup.
-Identifies names using spaCy's named entity recognition.
-Collects social media links (Twitter, Facebook, LinkedIn, Instagram, YouTube).

## Output
The script generates a table with the extracted information, including website, location, names, email, and social media links.

### Example Output:

| Website             | Location                | Names               | Email              | Instagram | YouTube | LinkedIn | Twitter | Facebook |
|---------------------|-------------------------|---------------------|--------------------|-----------|---------|----------|---------|----------|
| somewebsite1.com    | N/A                     | ['Ayse Nur Ozer']   | N/A                | N/A       | N/A     | N/A      | N/A     | N/A      |
| somewebsite2.com    | N/A                     | ['Ayse Nur Ozer']   | N/A                | N/A       | N/A     | N/A      | N/A     | N/A      |
| somewebsite3.com    | {'ip': ..., 'city': ...,| ['Ayse Nur Ozer']   | N/A                | N/A       | N/A     | N/A      | N/A     | N/A      |
|                     | 'region': ..., 'country':|                     |                    |           |         |          |         |          |
|                     | ..., 'zip code': ...}    |                     |                    |           |         |          |         |          |
| ...                 | ...                     | ...                 | ...                | ...       | ...     | ...      | ...     | ...      |


