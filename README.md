# timeview

## Project Overview & Architecture

**Core Features:**
- Interactive timeline visualization
- Historical events database
- Geographic filtering (events around the world)
- Time period filtering
- Event viewgeolocation on map and we can see it precisely where event is happening at the time

## Tech Stack

**Frontend:**
- React or Vue.js - for UI components
- D3.js - for timeline visualization
- Leaflet.js - for geographic visualization
- Material-UI - for styling

**Backend:**
- Python/Flask - for API
- PostgreSQL - for database implementation in future
- Static JSON files for MVP

**Data Source:**
- Sample data for MVP
- Future integration with Wikipedia API, Wikidata, or historical events APIs
- Manual curation for quality

## Backend API Endpoints

Base URL: `http://localhost:5000`

### Health Check
```
GET /
```
Returns API status and version information.

### Get All Events
```
GET /api/events
```
Retrieve all historical events with optional filtering.

**Query Parameters:**
- `start_year` - Filter events from this year onwards
- `end_year` - Filter events up to this year
- `location` - Filter by location (case-insensitive)
- `category` - Filter by category (case-insensitive)

**Example:**
```
GET /api/events?start_year=1900&end_year=2000&category=technology
```

### Get Event by ID
```
GET /api/events/<event_id>
```
Retrieve a specific event by its ID.

### Get All Categories
```
GET /api/events/categories
```
Returns a list of all unique event categories.

### Get All Locations
```
GET /api/events/locations
```
Returns a list of all unique event locations.

## Getting Started

### Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

The API will be available at `http://localhost:5000`

