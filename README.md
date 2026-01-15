# timeview

> **⚠️ Project Under Development:**  
> This project is currently in active development. Features, APIs, and documentation are subject to change. Contributions, suggestions, and feedback are welcome!

---

## 📝 Implementation Checklist (Priority Order)

### 1. Core Backend Functionality
- [x] Implement `/api/events` endpoint (with filtering, pagination, and validation).
- [x] Implement `/api/events/<event_id>` endpoint (fetch event by ID with error handling).
- [ ] Implement `/api/events/categories` and `/api/events/locations` endpoints.
- [x] Connect backend to static JSON data (initial MVP).

### 2. Core Frontend Functionality
- [ ] Set up frontend app structure (React or Vue.js).
- [ ] Timeline component with interactive controls (zoom, scroll, select).
- [ ] Map visualization (integrate Leaflet.js).
- [ ] Display events on map and timeline, enable click-to-view details.
- [ ] Implement event filters (time period, category, location).

### 3. Data Improvements
- [ ] Expand and refine sample historical event data.
- [ ] Add more locations and categories for filtering.
- [ ] Add data validation scripts/utilities.

### 4. UI/UX Polish & Extras
- [ ] Add Material-UI for styling and layout.
- [ ] Responsive layout for mobile/web.
- [ ] Tooltips, modals, or popups for event details.
- [ ] Error/loading states and user feedback.

### 5. Advanced/Stretch Goals
- [ ] Integrate with external APIs (Wikipedia, Wikidata, etc.) for dynamic event loading.
- [ ] Implement user curation/admin interface for event data.
- [ ] Migrate data to PostgreSQL, update API accordingly.
- [ ] User accounts, favoriting/bookmarking events.

### 6. Testing, Docs & Deployment
- [ ] Write unit/integration tests for backend and frontend.
- [ ] Improve API and contributor documentation.
- [ ] Prepare production deployment configs.

---



---
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


| Endpoint                      | Method | Description                                   |
|-------------------------------|--------|-----------------------------------------------|
| `/`                           | GET    | Returns API status and version information.   |
| `/api/events`                 | GET    | Retrieve all historical events with optional filtering. |
| `/api/events/<event_id>`      | GET    | Retrieve a specific event by its ID.          |
| `/api/events/categories`      | GET    | Returns a list of all unique event categories.|
| `/api/events/locations`       | GET    | Returns a list of all unique event locations. |


**Query Parameters:**
- `start_year` - Filter events from this year onwards
- `end_year` - Filter events up to this year
- `location` - Filter by location (case-insensitive)
- `category` - Filter by category (case-insensitive)

| Endpoint Example                              | Description                                 |
|-----------------------------------------------|---------------------------------------------|
| `GET /api/events?start_year=1900&end_year=2000&category=technology` | Retrieve all events from 1900 to 2000, filtered by category `technology`. |
| `GET /api/events/<event_id>`                  | Retrieve a specific event by its ID.        |
| `GET /api/events/categories`                  | Returns a list of all unique event categories. |
| `GET /api/events/locations`                   | Returns a list of all unique event locations. |

## Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

