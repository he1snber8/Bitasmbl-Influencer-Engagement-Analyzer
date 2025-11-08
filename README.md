# Bitasmbl-Influencer-Engagement-Analyzer — Influencer-Engagement-Analyzer

Description

A platform that analyzes social media influencer performance by aggregating engagement metrics such as likes, comments, follower growth, and post frequency. The system computes engagement rates, trends, and performance indicators and presents them through interactive charts and comparison views to help users evaluate influencer impact and trends.

## Tech Stack

- FastAPI (API)
- React (Front-End)
- Recharts (Visualization)

## Requirements

- Fetch influencer data from social media APIs or datasets
- Calculate engagement rates, trends, and performance indicators
- Display insights using charts, comparisons, and intuitive visuals
- Allow users to search, filter, and compare influencers
- Handle missing, inconsistent, or rate-limited API data

## Installation

Clone the repository

1. git clone https://github.com/he1snber8/Bitasmbl-Influencer-Engagement-Analyzer.git
2. cd Bitasmbl-Influencer-Engagement-Analyzer

The repository is structured with a backend (FastAPI) and frontend (React):

- backend/  -> FastAPI app (Python)
- client/   -> React app (Recharts visualizations)

Backend (FastAPI)

1. cd backend
2. Create a Python virtual environment and activate it:
   - Linux / macOS:
     python3 -m venv .venv
     source .venv/bin/activate
   - Windows (PowerShell):
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
3. Install dependencies:
   pip install -r requirements.txt
4. Create a .env file (or copy .env.example) in backend/ and set required environment variables. Example .env keys:
   - SOCIAL_API_KEY=your_social_api_key
   - SOCIAL_API_SECRET=your_social_api_secret
   - SOCIAL_API_BASE_URL=https://api.socialplatform.com
   - RATE_LIMIT_BACKOFF_MS=1000
   - CACHE_TTL_SECONDS=300
   - DATABASE_URL=sqlite:///./data.db  # optional local storage
5. Run the development server:
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
6. Open API docs: http://localhost:8000/docs

Frontend (React + Recharts)

1. Open a new terminal
2. cd client
3. Install dependencies:
   npm install
4. Create a .env.local (or .env) in client/ with at least:
   - REACT_APP_API_BASE_URL=http://localhost:8000/api
5. Run the dev server:
   npm start
6. Open the app: http://localhost:3000

Notes

- Backend dev port: 8000. Frontend dev port: 3000.
- The FastAPI app exposes /docs and /redoc for API exploration.
- Ensure your SOCIAL_API_* credentials have permission to fetch the influencer data you need.

## Usage

1. Start the backend and frontend as described in Installation.
2. Use the frontend UI to search influencers, view individual influencer dashboards, or choose multiple influencers to compare.
3. API docs (FastAPI) are available at http://localhost:8000/docs for direct API calls, examples, and testing.
4. Frontend visualizations (Recharts) display:
   - Engagement rate over time
   - Likes/comments ratio
   - Follower growth charts
   - Post frequency histograms
   - Comparison radar/line charts for selected influencers
5. If social API data is missing or rate-limited, the backend will return partial results with metadata about which fields are missing and caching/backoff info. The frontend surfaces these warnings.

## Implementation Steps

1. Initialize repository structure with backend/ (FastAPI) and client/ (React).
2. Build FastAPI app skeleton: app/main.py, app/api/, app/services/, app/models/, requirements.txt, .env.example.
3. Implement social API connectors in backend/services/social_connector.py with:
   - request retries and exponential backoff controlled by RATE_LIMIT_BACKOFF_MS env var
   - response validation and normalization
   - caching layer (in-memory TTL or lightweight DB) controlled by CACHE_TTL_SECONDS
   - graceful handling of missing fields
4. Design data models (Pydantic) for influencer summaries, time series, and comparison payloads.
5. Implement endpoints for search, details, and comparison (see API Endpoints below).
6. Add metric calculation utilities in backend/services/metrics.py to compute:
   - engagement rate (e.g., (likes + comments) / followers)
   - follower growth rate
   - average post frequency
   - trending slope (simple linear regression over recent points)
7. Add unit tests for metric calculations and connector normalization.
8. Build React app with create-react-app or equivalent in client/.
9. Implement components:
   - SearchBar, InfluencerCard, InfluencerDetail (time series), ComparisonView
   - Charts using Recharts (LineChart, BarChart, RadarChart)
10. Implement filter and compare state management (React context or local state) and connect to backend API endpoints.
11. Handle API errors and rate-limit responses in the frontend with clear UI messages and retry options.
12. Add basic styling and responsive layout for dashboards and comparison pages.
13. Document environment variables, run commands, and deployment notes.

Optional next steps:
- Add authentication and user accounts to save favorites/compare lists
- Add persistent DB for historical aggregated data
- Add scheduled backend job to pre-fetch and cache influencer time series

## API Endpoints

The FastAPI backend exposes a JSON API under /api (or root depending on implementation). Example endpoints:

1. GET /api/health
   - Purpose: Lightweight health check
   - Response: { "status": "ok" }

2. GET /api/influencers?query=term&platform=instagram&limit=20&offset=0
   - Purpose: Search influencers
   - Query params: query (string), platform (string), limit, offset
   - Response example:
     [
       {
         "id": "123",
         "username": "influencer_name",
         "platform": "instagram",
         "followers": 120000,
         "avg_engagement_rate": 0.034,
         "last_updated": "2025-01-01T12:00:00Z"
       }
     ]

3. GET /api/influencers/{id}
   - Purpose: Get detailed metrics and time series for a single influencer
   - Response example:
     {
       "id": "123",
       "username": "influencer_name",
       "platform": "instagram",
       "followers": 120000,
       "metrics": {
         "engagement_rate": 0.034,
         "follower_growth_7d": 0.012,
         "avg_post_frequency_per_week": 3.5
       },
       "time_series": [
         { "date": "2025-10-01", "followers": 118000, "likes": 4200, "comments": 120 },
         { "date": "2025-10-08", "followers": 119200, "likes": 4500, "comments": 130 }
       ],
       "warnings": ["partial_data", "rate_limited"]
     }

4. POST /api/compare
   - Purpose: Compare multiple influencers
   - Request body example:
     { "ids": ["123", "456"], "metrics": ["engagement_rate","follower_growth_7d"] }
   - Response: comparison payload with normalized metric values and timeseries for plotting

5. GET /api/search-autocomplete?term=abc&platform=instagram
   - Purpose: Provide fast autocomplete suggestions for the frontend search box

Rate limiting and headers

- When proxied social API rate limits are encountered, the backend will propagate helpful headers and include a "warnings" field in JSON responses. Typical headers:
  - X-RateLimit-Limit
  - X-RateLimit-Remaining
  - X-RateLimit-Reset

Error handling

- Missing or inconsistent data returns HTTP 206 (Partial Content) or 200 with a "warnings" array describing what is missing; full errors use relevant 4xx/5xx codes.

For exact parameter names and schemas consult the OpenAPI docs at /docs when the backend is running.

----

Repository and contribution

- Repo: https://github.com/he1snber8/Bitasmbl-Influencer-Engagement-Analyzer
- Issues and PRs: Please open issues or pull requests in the repo above. If you are using this as a base for your own fork, keep environment secrets out of source control and use .env files.

License

- Add your chosen license file (e.g., LICENSE) at the repository root.

If you need starter code snippets for app/main.py, example React components, or metric formulas, ask and I will provide them tailored to FastAPI and React + Recharts.