#!/bin/bash

# Script for setting up cron jobs for Solarman Bot
# Usage: ./cron_setup.sh

echo "⏰ Setting up cron jobs for Solarman Bot..."

# Get absolute path to project directory
PROJECT_DIR=$(pwd)
PYTHON_SCRIPT="$PROJECT_DIR/solarman_export.py"

# Create cron job for daily execution at 9:00
CRON_JOB="0 9 * * * cd $PROJECT_DIR && docker-compose run --rm solarman-bot python solarman_export.py >> $PROJECT_DIR/logs/cron.log 2>&1"

# Add job to crontab
(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

echo "✅ Cron job added:"
echo "   Execution time: daily at 9:00"
echo "   Command: $CRON_JOB"
echo ""
echo "📋 Current cron jobs:"
crontab -l
echo ""
echo "📝 Cron logs will be saved in logs/cron.log" 