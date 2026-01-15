from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Load sample events data
def load_events():
    """Load events from JSON file"""
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'events.json')
    try:
        with open(data_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'success',
        'message': 'TimeView API is running',
        'version': '1.0.0'
    })

@app.route('/api/events', methods=['GET'])
def get_events():
    """
    Get all events with optional filtering
    Query parameters:
    - start_year: Filter events from this year onwards
    - end_year: Filter events up to this year
    - location: Filter by location/country
    - category: Filter by event category
    """
    events = load_events()
    
    # Get query parameters
    start_year = request.args.get('start_year', type=int)
    end_year = request.args.get('end_year', type=int)
    location = request.args.get('location', type=str)
    category = request.args.get('category', type=str)
    
    # Filter events based on query parameters
    filtered_events = events
    
    if start_year:
        filtered_events = [e for e in filtered_events if e.get('year', 0) >= start_year]
    
    if end_year:
        filtered_events = [e for e in filtered_events if e.get('year', 0) <= end_year]
    
    if location:
        filtered_events = [e for e in filtered_events if location.lower() in e.get('location', '').lower()]
    
    if category:
        filtered_events = [e for e in filtered_events if category.lower() in e.get('category', '').lower()]
    
    return jsonify({
        'status': 'success',
        'count': len(filtered_events),
        'data': filtered_events
    })

@app.route('/api/events/<int:event_id>', methods=['GET'])
def get_event_by_id(event_id):
    """Get a specific event by ID"""
    events = load_events()
    event = next((e for e in events if e.get('id') == event_id), None)
    
    if event:
        return jsonify({
            'status': 'success',
            'data': event
        })
    else:
        return jsonify({
            'status': 'error',
            'message': 'Event not found'
        }), 404

@app.route('/api/events/categories', methods=['GET'])
def get_categories():
    """Get all unique event categories"""
    events = load_events()
    categories = list(set(e.get('category', 'Unknown') for e in events))
    
    return jsonify({
        'status': 'success',
        'count': len(categories),
        'data': sorted(categories)
    })

@app.route('/api/events/locations', methods=['GET'])
def get_locations():
    """Get all unique event locations"""
    events = load_events()
    locations = list(set(e.get('location', 'Unknown') for e in events))
    
    return jsonify({
        'status': 'success',
        'count': len(locations),
        'data': sorted(locations)
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Internal server error'
    }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
