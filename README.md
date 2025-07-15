# Solarman Bot

Bot for retrieving data from Solarman solar panel and sending reports to Telegram.

## Description

This project automatically retrieves solar panel electricity generation data through the Solarman API and sends daily reports to a Telegram channel.

## Deployment on Digital Ocean

### 1. Server Preparation

1. Create a Droplet on Digital Ocean:
   - Choose Ubuntu 22.04 LTS
   - Minimum 1GB RAM, 1 CPU
   - Add SSH key for secure access

2. Connect to the server:
```bash
ssh root@your-server-ip
```

### 2. Docker Installation

```bash
# System update
apt update && apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Add user to docker group
usermod -aG docker $USER

# Install Docker Compose
curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

### 3. Project Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd solarman-bot
```

2. Create `.env` file with environment variables:
```bash
# Telegram settings
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=@your_channel_name

# Solarman token (optional, if you need to update)
SOLARMAN_TOKEN=your_solarman_token
```

3. Create logs directory:
```bash
mkdir logs
```

### 4. Application Launch

#### Option 1: One-time launch
```bash
docker-compose up --build
```

#### Option 2: Background launch
```bash
docker-compose up -d --build
```

#### Option 3: Scheduler launch
```bash
# Change the command in docker-compose.yml to:
# command: python scheduler.py
docker-compose up -d --build
```

### 5. Monitoring

Check logs:
```bash
# Application logs
docker-compose logs -f solarman-bot

# File logs
tail -f logs/solarman_bot.log
tail -f logs/scheduler.log
```

### 6. Automatic startup on reboot

Create systemd service:

```bash
sudo nano /etc/systemd/system/solarman-bot.service
```

File content:
```ini
[Unit]
Description=Solarman Bot
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/root/solarman-bot
ExecStart=/usr/local/bin/docker-compose up -d
ExecStop=/usr/local/bin/docker-compose down
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
```

Activate service:
```bash
sudo systemctl enable solarman-bot.service
sudo systemctl start solarman-bot.service
```

## Project Structure

- `solarman_export.py` - Main script for data retrieval
- `telegram_message_sender.py` - Telegram message sending
- `telegram_message_formatter.py` - Report formatting
- `scheduler.py` - Task scheduler
- `solarman_token.py` - Solarman token retrieval
- `docker-compose.yml` - Docker configuration
- `Dockerfile` - Docker image
- `requirements.txt` - Python dependencies

## Environment Variables

- `TELEGRAM_BOT_TOKEN` - Telegram bot token
- `TELEGRAM_CHAT_ID` - Channel or chat ID for message sending
- `SOLARMAN_TOKEN` - Token for Solarman API access

## Application Update

```bash
# Stop containers
docker-compose down

# Get updates
git pull

# Rebuild and launch
docker-compose up -d --build
```

## Troubleshooting

1. **API connection issues**:
   - Check Solarman token
   - Ensure API availability

2. **Telegram sending errors**:
   - Check bot token
   - Ensure bot is added to channel

3. **Docker issues**:
   - Check logs: `docker-compose logs`
   - Restart containers: `docker-compose restart`

## Security

- Don't commit `.env` file to repository
- Use strong SSH passwords
- Regularly update system and Docker
- Configure firewall to limit access 