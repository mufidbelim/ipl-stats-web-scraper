# IPL Top Run Scorers Scraper

A Python web scraping project that extracts IPL player statistics from ESPNcricinfo and displays them through a web interface. This project demonstrates professional web scraping, data processing, and web development skills.

## Features

- Scrapes official IPL data from ESPNcricinfo
- Cleans and processes player statistics
- Generates CSV and JSON files for data analysis
- Beautiful web interface with Flask
- JSON API endpoints for developers
- Responsive design for all devices
- Automatic data refresh
- Download functionality
- Data filtering options
- Error handling and logging

## Data Source

The project scrapes data from ESPNcricinfo's official IPL statistics page:
- URL: `https://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?id=117;type=trophy`
- Data includes: Player name, runs, matches, average, strike rate
- Updated regularly from official sources

## Quick Start

### 1. Installation

```bash
# Clone or download the project
# Install dependencies
pip install -r requirements.txt