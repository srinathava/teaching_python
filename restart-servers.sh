#!/bin/bash

echo "Killing existing server processes..."

# Create a directory for PIDs if it doesn't exist
mkdir -p .pids

# More aggressive process killing
kill_processes() {
    # Kill by port for frontend (Vite uses 5173 by default)
    echo "Killing any processes using port 5173..."
    lsof -ti:5173 | xargs kill -9 2>/dev/null || true
    
    # Kill any processes with 'vite' in the name
    echo "Killing any Vite processes..."
    pkill -f "vite" 2>/dev/null || true
    
    # Kill any processes with 'node' running the frontend dev server
    echo "Killing any Node processes related to frontend..."
    pkill -f "node.*frontend" 2>/dev/null || true
    
    # Kill backend uvicorn processes
    echo "Killing any Uvicorn processes..."
    pkill -f "uvicorn" 2>/dev/null || true
    
    # Kill by PID file if it exists
    local pid_file=$1
    if [ -f "$pid_file" ]; then
        pid=$(cat "$pid_file")
        if ps -p $pid > /dev/null; then
            echo "Killing process with PID $pid..."
            kill -9 $pid 2>/dev/null || true
            rm "$pid_file"
        fi
    fi
    
    # Small delay to ensure processes are terminated
    sleep 1
}

# Kill existing processes
kill_processes ".pids/frontend.pid"
kill_processes ".pids/backend.pid"

# Clean up any remaining PID files
rm -f .pids/*.pid 2>/dev/null || true

echo "Setting up backend..."
cd backend
source venv/bin/activate

# Install/upgrade dependencies
echo "Installing/upgrading Python dependencies..."
pip install -r requirements.txt

# Run database migrations
echo "Running database migrations..."
alembic upgrade head

# Create temporary user for development
echo "Creating temporary user..."
python -c "
from src.database import get_db_context
from src.models import User

with get_db_context() as db:
    if not db.query(User).filter(User.id == 1).first():
        db.add(User(id=1))
        db.commit()
        print('Created temporary user with ID 1')
    else:
        print('Temporary user already exists')
"

echo "Starting backend server..."
python -m uvicorn src.api.main:app --reload & echo $! > ../.pids/backend.pid

echo "Starting frontend server..."
cd ../frontend
npm run dev & echo $! > ../.pids/frontend.pid

echo "Servers restarted! Give them a few seconds to initialize..."