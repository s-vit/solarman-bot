#!/bin/bash

# Script for deploying Solarman Bot on Digital Ocean
# Usage: ./deploy.sh

set -e

echo "🚀 Starting Solarman Bot deployment..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Installing..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    sudo usermod -aG docker $USER
    echo "✅ Docker installed"
else
    echo "✅ Docker is already installed"
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Installing..."
    sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    echo "✅ Docker Compose installed"
else
    echo "✅ Docker Compose is already installed"
fi

# Create logs directory
echo "📁 Creating logs directory..."
mkdir -p logs

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  .env file not found. Creating from example..."
    if [ -f env.example ]; then
        cp env.example .env
        echo "📝 Created .env file from example. Please edit it with your settings."
        echo "   You need to specify:"
        echo "   - TELEGRAM_BOT_TOKEN"
        echo "   - TELEGRAM_CHAT_ID"
        echo "   - SOLARMAN_TOKEN (optional)"
        exit 1
    else
        echo "❌ env.example file not found"
        exit 1
    fi
fi

# Stop existing containers
echo "🛑 Stopping existing containers..."
docker-compose down 2>/dev/null || true

# Build and run
echo "🔨 Building and running application..."
docker-compose up -d --build

# Check status
echo "⏳ Waiting for containers to start..."
sleep 10

# Check container status
if docker-compose ps | grep -q "Up"; then
    echo "✅ Application successfully started!"
    echo ""
    echo "📊 Useful commands:"
    echo "   View logs: docker-compose logs -f"
    echo "   Stop: docker-compose down"
    echo "   Restart: docker-compose restart"
    echo "   Update: git pull && docker-compose up -d --build"
    echo ""
    echo "📝 Logs are saved in logs/ directory"
else
    echo "❌ Application startup error"
    docker-compose logs
    exit 1
fi 