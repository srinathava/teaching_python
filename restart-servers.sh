#!/bin/bash

echo "Killing existing server processes..."

# Create a directory for PIDs if it doesn't exist
mkdir -p .pids

# Function to kill process by PID file if it exists
kill_by_pid() {
    local pid_file=$1
    if [ -f "$pid_file" ]; then
        pid=$(cat "$pid_file")
        if ps -p $pid > /dev/null; then
            kill $pid
            rm "$pid_file"
        fi
    fi
}

# Kill existing processes using their PID files
kill_by_pid ".pids/frontend.pid"
kill_by_pid ".pids/backend.pid"

echo "Starting backend server..."
cd backend
source venv/bin/activate
python -m uvicorn src.api.main:app --reload & echo $! > ../.pids/backend.pid

echo "Starting frontend server..."
cd ../frontend
npm run dev & echo $! > ../.pids/frontend.pid

echo "Servers restarted! Give them a few seconds to initialize..."