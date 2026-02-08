"""
Test the scraper with local data first
"""
import pandas as pd
import json
from datetime import datetime

def create_sample_data():
    """Create sample data for testing"""
    sample_data = [
        {"Player": "Virat Kohli", "Runs": 7263, "Matches": 237, "Average": 37.25, "Strike_Rate": 130.02},
        {"Player": "Shikhar Dhawan", "Runs": 6617, "Matches": 217, "Average": 35.08, "Strike_Rate": 126.64},
        {"Player": "David Warner", "Runs": 6397, "Matches": 176, "Average": 41.54, "Strike_Rate": 139.91},
        {"Player": "Rohit Sharma", "Runs": 6211, "Matches": 243, "Average": 30.00, "Strike_Rate": 130.05},
        {"Player": "Suresh Raina", "Runs": 5528, "Matches": 205, "Average": 32.51, "Strike_Rate": 136.73},
        {"Player": "AB de Villiers", "Runs": 5162, "Matches": 184, "Average": 39.71, "Strike_Rate": 151.69},
        {"Player": "Chris Gayle", "Runs": 4965, "Matches": 142, "Average": 39.72, "Strike_Rate": 148.96},
        {"Player": "MS Dhoni", "Runs": 5082, "Matches": 250, "Average": 38.79, "Strike_Rate": 135.92},
        {"Player": "Robin Uthappa", "Runs": 4952, "Matches": 205, "Average": 27.51, "Strike_Rate": 130.35},
        {"Player": "Dinesh Karthik", "Runs": 4516, "Matches": 242, "Average": 26.11, "Strike_Rate": 132.71},
    ]
    
    df = pd.DataFrame(sample_data)
    df['Insight'] = ['Legend', 'Legend', 'Legend', 'Legend', 'Legend', 'Elite', 'Elite', 'Elite', 'Elite', 'Elite']
    
    return df

def save_data(df):
    """Save data to CSV and JSON"""
    season = "IPL - Career Runs (2024 Season)"
    last_updated = datetime.now().strftime("%d %b %Y")
    
    # Save to CSV
    with open("ipl_most_runs_career.csv", 'w', encoding='utf-8') as f:
        f.write(f"# IPL Most Runs - Career Statistics\n")
        f.write(f"# Season: {season}\n")
        f.write(f"# Last Updated: {last_updated}\n")
        f.write(f"# Total Players: {len(df)}\n")
        f.write(f"# Data Source: Sample Data for Testing\n")
    
    df.to_csv("ipl_most_runs_career.csv", mode='a', index=False)
    print("✓ Created 'ipl_most_runs_career.csv'")
    
    # Save to JSON
    output_data = {
        'metadata': {
            'season': season,
            'last_updated': last_updated,
            'total_players': len(df),
            'data_source': 'Sample Data for Testing',
            'description': 'IPL Career Runs Statistics'
        },
        'players': df.to_dict('records')
    }
    
    with open("ipl_most_runs_career.json", 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print("✓ Created 'ipl_most_runs_career.json'")
    
    # Display summary
    total_runs = df['Runs'].sum()
    avg_runs = df['Runs'].mean()
    
    print(f"\n{'='*60}")
    print("SAMPLE DATA CREATED SUCCESSFULLY!")
    print("="*60)
    print(f"\nTotal Players: {len(df)}")
    print(f"Total Runs: {total_runs:,}")
    print(f"Average Runs: {avg_runs:,.0f}")
    print(f"Top Scorer: {df.iloc[0]['Player']} ({df.iloc[0]['Runs']:,} runs)")
    print(f"\nNow run: python app.py")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("CREATING SAMPLE IPL DATA")
    print("="*60)
    print("\nThis will create sample data files for testing.")
    print("The web interface will work with this data.")
    
    df = create_sample_data()
    save_data(df)