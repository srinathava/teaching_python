# Python Teaching Platform

A full-stack application designed to teach Python programming through interactive exercises and lessons.

## Project Structure

- `frontend/` - SvelteKit application with TailwindCSS and Monaco Editor
- `backend/` - FastAPI Python server with code validation and OpenAI integration
- `docs/` - Project documentation and architecture details

## Prerequisites

- Node.js (v18 or higher)
- Python 3.8 or higher
- Redis server (for backend caching)
- npm or yarn
- Python virtual environment tool (venv)

## Installation

### Backend Setup

1. Create and activate a Python virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
```
Edit `.env` and set:
- `OPENAI_API_KEY` - Your OpenAI API key for error translations
- `REDIS_URL` - Redis connection URL (default: redis://localhost:6379)
- `RATE_LIMIT_PER_MINUTE` - API rate limit (default: 30)

### Frontend Setup

1. Install Node.js dependencies:
```bash
cd frontend
npm install
```

2. Configure environment variables:
```bash
cp .env.example .env
```
The frontend uses SQLite by default with:
- `DATABASE_URL=file:local.db`

3. Initialize the database:
```bash
npm run db:reset  # This will run migrations and seed data
```

## Development

You can start both servers using the provided script:

```bash
./restart-servers.sh
```

Or start them individually:

### Backend
```bash
cd backend
source venv/bin/activate
python -m uvicorn src.api.main:app --reload
```

### Frontend
```bash
cd frontend
npm run dev
```

The application will be available at:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000

## Available Scripts

### Frontend

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run check` - Type-check the codebase
- `npm run lint` - Lint and format check
- `npm run format` - Format code with Prettier
- `npm test` - Run all tests
- `npm run db:reset` - Reset and seed the database

### Backend

- Development server runs with auto-reload enabled
- Tests can be run with: `python -m pytest`

## Documentation

Additional documentation can be found in:
- `architecture.md` - System architecture overview
- `design.md` - Design decisions and patterns
- `frontend.md` - Frontend-specific documentation
- `variables.md` - Variable lesson documentation
- `backend/docs/code-validation.md` - Code validation documentation