# JMA Weather Data Scraping

This project demonstrates how to scrape, parse, and structure weather data (per 10 min) from the Japan Meteorological Agency (JMA) website using Python.

## Project Context
Access to structured weather data is essential for time-series analysis and modeling, but some JMA data are only available through HTML tables. 
This project builds a pipeline to extract and clean that data for analysis.

## Key Skills Demonstrated
- Scraping tabular data using `requests`
- Parsing HTML with `BeautifulSoup`
- Cleaning and exporting data using `pandas`

## Requirements
- Python 3.x
- `requests`
- `bs4`
- `pandas`

## Blog Post
[Read the full tutorial here](https://www.DataDrivenMai/blog/)

## How to Run
Open the notebook and run all cells sequentially.

## Project Structure
- `jma_weather_scraping.ipynb`
- `data/`
- `images/`