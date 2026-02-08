# IPL Statistics Web Scraper

A Python-based web scraping project that extracts IPL cricket statistics from ESPNcricinfo and displays them through an interactive web interface. This project demonstrates practical skills in web scraping, data processing, and full-stack web development.

## 📋 Features

- **Web Scraping**: Fetches live IPL player data from ESPNcricinfo
- **Data Processing**: Cleans and processes statistics using Pandas
- **Web Interface**: Interactive Flask-based dashboard
- **Multiple Formats**: Export data as CSV or JSON
- **API Endpoints**: RESTful API for programmatic access
- **Filtering Options**: View top 5, 10, 20, or all players
- **Player Insights**: Automatic categorization (Legend/Elite/Good)
- **Responsive Design**: Works on desktop and mobile devices

## 🏗️ Project Structure

ipl-stats-web-scraper/
├── scraper.py # Main scraping script
├── app.py # Flask web application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore # Git ignore rules
├── templates/
│ └── index.html # Web interface template
├── ipl_most_runs_career.csv # Sample output data
└── ipl_most_runs_career.json # Sample output data


## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mufidbelim/ipl-stats-web-scraper.git
cd ipl-stats-web-scraper
pip install -r requirements.txt
