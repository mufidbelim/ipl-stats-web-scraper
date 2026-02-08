"""
ALTERNATIVE: Use cricket API instead of web scraping
"""
import requests
import pandas as pd
import json

def fetch_from_cricket_api():
    """
    Try to fetch IPL data from cricket API
    """
    try:
        # This is a public cricket API endpoint
        response = requests.get(
            "https://cricket-api.vercel.app/api/ipl/stats/batsmen",
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            if data and 'players' in data:
                return pd.DataFrame(data['players'])
    except:
        pass
    
    return None

# You can integrate this into the scraper as another option