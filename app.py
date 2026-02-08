"""
IPL STATS WEB INTERFACE - SIMPLIFIED VERSION
"""

from flask import Flask, render_template, send_file, jsonify, request
import pandas as pd
import os
import json

app = Flask(__name__)

def load_data():
    """Load data from CSV or JSON"""
    try:
        # Try JSON first
        if os.path.exists('ipl_most_runs_career.json'):
            with open('ipl_most_runs_career.json', 'r') as f:
                data = json.load(f)
                players = data.get('players', [])
                metadata = data.get('metadata', {})
                return players, metadata
        
        # Try CSV
        elif os.path.exists('ipl_most_runs_career.csv'):
            df = pd.read_csv('ipl_most_runs_career.csv')
            players = df.to_dict('records')
            metadata = {
                'last_updated': 'Today',
                'season': 'IPL Career Runs',
                'total_players': len(players)
            }
            return players, metadata
        
        return [], {}
    
    except Exception as e:
        print(f"Error loading data: {e}")
        return [], {}

@app.route('/')
def index():
    """Main page"""
    players, metadata = load_data()
    
    # Filter if requested
    top_n = request.args.get('top', type=int)
    if top_n and top_n > 0:
        players = players[:top_n]
    
    # Calculate stats
    stats = {
        'total_players': len(players),
        'total_runs': sum(p.get('Runs', 0) for p in players),
        'top_scorer': players[0]['Player'] if players else 'N/A',
        'top_runs': players[0]['Runs'] if players else 0
    }
    
    return render_template(
        'index.html',
        players=players,
        stats=stats,
        metadata=metadata,
        has_data=len(players) > 0
    )

@app.route('/download/csv')
def download_csv():
    """Download CSV"""
    if os.path.exists('ipl_most_runs_career.csv'):
        return send_file('ipl_most_runs_career.csv', as_attachment=True)
    return "File not found", 404

@app.route('/download/json')
def download_json():
    """Download JSON"""
    if os.path.exists('ipl_most_runs_career.json'):
        return send_file('ipl_most_runs_career.json', as_attachment=True)
    return "File not found", 404

@app.route('/api/players')
def api_players():
    """API endpoint"""
    players, metadata = load_data()
    return jsonify({
        'success': True,
        'count': len(players),
        'players': players,
        'metadata': metadata
    })

@app.route('/api/stats')
def api_stats():
    """Stats API"""
    players, metadata = load_data()
    
    if not players:
        return jsonify({'success': False, 'error': 'No data'})
    
    df = pd.DataFrame(players)
    stats = {
        'total_players': len(players),
        'total_runs': int(df['Runs'].sum()) if 'Runs' in df.columns else 0,
        'average_runs': float(df['Runs'].mean()) if 'Runs' in df.columns else 0,
        'top_scorer': df.iloc[0]['Player'] if len(df) > 0 else 'N/A'
    }
    
    return jsonify({
        'success': True,
        'stats': stats,
        'metadata': metadata
    })

if __name__ == '__main__':
    print("\n" + "="*50)
    print("IPL STATS WEB SERVER")
    print("="*50)
    print("\nStarting server...")
    print("Open: http://localhost:5000")
    print("\nPress CTRL+C to stop")
    print("="*50)
    
    # Run the app
    app.run(debug=True, host='0.0.0.0', port=5000)