# TimeView Backend API

Flask-based REST API for serving historical events data.

## Setup

1. **Install Dependencies**
```bash
cd backend
pip install -r requirements.txt
```

2. **Run the Application**
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### 1. Health Check
```
GET /
```
Returns API status and version information.

### 2. Get All Events
```
GET /api/events
```
Returns all historical events with optional filtering.

**Query Parameters:**
- `start_year` (int) - Filter events from this year onwards
- `end_year` (int) - Filter events up to this year
- `location` (string) - Filter by location (case-insensitive)
- `category` (string) - Filter by category (case-insensitive)

**Example:**
```
GET /api/events?start_year=1900&end_year=2000&category=technology
```

### 3. Get Event by ID
```
GET /api/events/<event_id>
```
Returns a specific event by its ID.

**Example:**
```
GET /api/events/1
```

### 4. Get All Categories
```
GET /api/events/categories
```
Returns a list of all unique event categories.

### 5. Get All Locations
```
GET /api/events/locations
```
Returns a list of all unique event locations.

## Response Format

All responses follow this structure:

**Success Response:**
```json
{
  "status": "success",
  "count": 10,
  "data": [...]
}
```

**Error Response:**
```json
{
  "status": "error",
  "message": "Error description"
}
```

## Event Data Structure

Each event contains:
```json
{
  "id": 1,
  "title": "Event Title",
  "description": "Event description",
  "year": 1969,
  "month": 7,
  "day": 20,
  "location": "Location Name",
  "coordinates": {
    "lat": 0.0,
    "lng": 0.0
  },
  "category": "Category Name"
}
```

## Development

- The API uses CORS to allow frontend communication
- Sample data is stored in `data/events.json`
- Add more events by editing the JSON file

## Future Enhancements

- PostgreSQL database integration
- Wikipedia API integration
- User authentication
- Event creation/editing endpoints
- Advanced search and filtering
- Pagination support
