# Forbes Billionaires Scraper

## Overview
This project extracts billionaire data from Forbes using Scrapy by leveraging internal API endpoints instead of traditional HTML scraping.

## Key Features
- API-based data extraction (no JavaScript rendering required)
- Pagination using `start` and `limit` parameters
- Extracts 500+ billionaire records

## Data Fields
- Name
- Net Worth
- Rank
- Age
- Country
- Source of Wealth
- Industry

## Tech Stack
- Python
- Scrapy

## How it Works
- Inspected Forbes website using browser DevTools
- Identified hidden JSON API in Network tab
- Reverse-engineered pagination logic
- Built Scrapy spider to automate extraction

## Output
- CSV file (`bills.csv`) with structured billionaire
