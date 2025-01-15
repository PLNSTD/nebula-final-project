# 🐍 World Population Scraper

This project scrapes data of about the 10 largest cities by population in a specified country and retrieves the population info [World Population Review](https://worldpopulationreview.com).

## Table of Contents

- [🐍 World Population Scraper](#-world-population-scraper)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Website Details](#website-details)
    - [`robots.txt` Configuration](#robotstxt-configuration)
  - [Setup Instructions](#setup-instructions)
  - [Deployment](#deployment)
    - [Steps to Deploy:](#steps-to-deploy)
  - [API Documentation](#api-documentation)
    - [Base URL](#base-url)
    - [Endpoints](#endpoints)
      - [1. **`GET /`**](#1-get-)
      - [2. **`GET /population_chart/<country>`**](#2-get-population_chartcountry)
      - [3. **`GET /population_chart`**](#3-get-population_chart)
      - [4. **`GET /scrape_and_store/continents`**](#4-get-scrape_and_storecontinents)
      - [5. **`GET /scrape_and_store/countries`**](#5-get-scrape_and_storecountries)
      - [6. **`GET /scrape_and_store/cities`**](#6-get-scrape_and_storecities)
      - [7. **`GET /scrape_and_store/population`**](#7-get-scrape_and_storepopulation)
    - [Error Handling](#error-handling)
    - [Usage Examples](#usage-examples)
      - [1. Fetch a Population Chart for a Country](#1-fetch-a-population-chart-for-a-country)
  - [License](#license)

## Features

- **City Population Data:** Fetches and stores population data for cities across different countries. The API allows access to the top 10 most populous cities in each country, with the ability to scrape data and keep the database up to date.
- **Population projections:** Provides detailed population projections, including charts and data up until the year 2095. These projections are stored in the database and can be accessed via the API to visualize trends.
- **Web Scraping Compliance:** Fully adheres to the website's `robots.txt` rules, ensuring all scraping activities are compliant with the website's guidelines and restrictions.

## Website Details

**Sources:**

- [World Population Review - Countries](https://worldpopulationreview.com/countries/<country-name>)

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

## Setup Instructions

```markdwon
To get this project up and running locally, follow these steps:

1. Clone the repository:
   git clone https://github.com/yourusername/yourprojectname.git

2. Install required Python libraries:
   pip install -r requirements.txt

3. Start the Flask server:
   python app.py
```

## Deployment

This application is deployed on [Render.com](https://render.com), a cloud platform that offers simple, fast, and scalable deployment for web applications.

### Steps to Deploy:

1. **Create a Render Account:**

   - Sign up for a free account at [Render.com](https://render.com).

2. **Connect Your GitHub Repository:**

   - In your Render dashboard, click **New Web Service** and choose to deploy from GitHub.
   - Select the repository containing your application.

3. **Set Up Environment Variables:**

   - Add any necessary environment variables (e.g., for database connections, secret keys) in the **Environment** tab of your Render service.
   - Ensure the proper configurations for `DB_HOST`, `DB_NAME`, `DB_PASSWORD`, `DB_USER` and `ENVIRONMENT` are in place.

4. **Automatic Deployments:**

   - Render will automatically deploy your app whenever you push changes to the connected GitHub repository.

5. **Access the Application:**
   - After deployment, you will receive a public URL where your Flask API can be accessed. This is where your application is hosted and can be accessed via the web.

## API Documentation

### Base URL

The base URL for the API is:

- project deployed on render.com -> https://nebula-final-project-9f8r.onrender.com
- project running locally -> http://127.0.0.1:5000

---

### Endpoints

#### 1. **`GET /`**

- **Description**: Displays a welcome message for the API.
- **Response**:
  - `200 OK`: `Welcome to the Flask API with psycopg2!`

---

#### 2. **`GET /population_chart/<country>`**

- **Description**: Generates and returns a population trend chart for the specified country, combining historical and projection data.
- **Parameters**:
  - `country` (path parameter, required): The name of the country (case insensitive).
- **Response**:
  - `200 OK`: Returns a PNG image of the population chart.
  - `404 Not Found`: If the specified country does not exist in the database.

---

#### 3. **`GET /population_chart`**

- **Description**: Generates and returns a comparison population trend chart for multiple countries.
- **Query Parameters**:
  - `country` (query parameter, required): List of country names to include in the comparison. Example: `?country=Italy&country=India`.
- **Response**:
  - `200 OK`: Returns a PNG image of the comparison population chart.
  - `404 Not Found`: If none of the provided countries exist in the database.

---

#### 4. **`GET /scrape_and_store/continents`**

- **Description**: Scrapes, processes, and stores continent data into the database.
- **Response**:
  - `200 OK`: `{'message': 'Continents data scraped, processed and stored successfully!'}`.
  - `500 Internal Server Error`: If an error occurs during scraping or database insertion.

---

#### 5. **`GET /scrape_and_store/countries`**

- **Description**: Scrapes, processes, and stores country data into the database.
- **Response**:
  - `200 OK`: `{'message': 'Countries data scraped, processed and stored successfully!'}`.
  - `500 Internal Server Error`: If an error occurs during scraping or database insertion.

---

#### 6. **`GET /scrape_and_store/cities`**

- **Description**: Scrapes, processes, and stores city data into the database.
- **Response**:
  - `200 OK`: `{'message': 'Cities data scraped, processed and stored successfully!'}`.
  - `500 Internal Server Error`: If an error occurs during scraping or database insertion.

---

#### 7. **`GET /scrape_and_store/population`**

- **Description**: Scrapes, processes, and stores population projection data for countries into the database.
- **Response**:
  - `200 OK`: `{'message': 'Population projections data scraped, processed and stored successfully!'}`.
  - `500 Internal Server Error`: If an error occurs during scraping or database insertion.

---

### Error Handling

- **404 Not Found**:

  - Returned when an endpoint or requested resource does not exist.
  - Example Response: `"404 Error: The page you're looking for doesn't exist."`

- **500 Internal Server Error**:
  - Indicates an unexpected error occurred while processing the request.
  - The response will include the error message for debugging purposes:
    ```json
    { "Error": "<error_message>" }
    ```

---

### Usage Examples

#### 1. Fetch a Population Chart for a Country

**Request**:

```bash
GET /population_chart/United States
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
