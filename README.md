# 🐍 Air Quality Index Scraper

This project scrapes data about the 10 largest cities by population in a specified country and retrieves the Air Quality Index (AQI) for those cities. The data is sourced from [World Population Review](https://worldpopulationreview.com).

## Features

- **City Population Data:** Extracts the 10 largest cities in a country based on population.
- **AQI Data Retrieval:** Fetches real-time AQI information for each city.
- **Web Scraping Compliance:** Adheres to the website's `robots.txt` rules.

## Website Details

**Sources:**

- [World Population Review - Countries](https://worldpopulationreview.com/countries/italy)
- [Air Quality Index (AQI) - City](https://aqicn.org/search/#q=Rome)

### `robots.txt` Configuration

```txt
# *
User-agent: *
Allow: /

# Host
Host: https://worldpopulationreview.com/

# Sitemaps
Sitemap: https://worldpopulationreview.com/sitemap.xml
Sitemap: https://worldpopulationreview.com/sitemap/index.xml
```

The above configuration allows all web crawlers to access the site, and the sitemap provides detailed indexing information.
