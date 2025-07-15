# Solarman Bot Deployment Guide on Digital Ocean

## Project Overview

Solarman Bot is a Python application that:
- Retrieves solar panel electricity generation data through the Solarman API
- Formats data into readable reports
- Sends reports to a Telegram channel
- Can work both one-time and on schedule

## Deployment Preparation

### 1. Create Telegram Bot

1. Find @BotFather in Telegram
2. Send `/newbot` command
3. Follow instructions to create bot
4. Save bot token
5. Add bot to your channel and make it administrator

### 2. Create Digital Ocean Droplet

1. Log into Digital Ocean
2. Click "Create" → "Droplets"
3. Select:
   - **Image**: Ubuntu 22.04 LTS
   - **Size**: Basic, 1GB RAM, 1 CPU (sufficient for bot)
   - **Region**: Choose closest to you
   - **Authentication**: SSH Key (recommended) or Password
4. Click "Create Droplet"

### 3. Connect to server

```bash
ssh root@your-server-ip
```

## Deployment

### Option 1: Automatic deployment (recommended)

1. Clone repository:
```bash
git clone <your-repo-url>
cd solarman-bot
```

2. Configure environment variables:
```bash
cp env.example .env
nano .env
```

3. Run automatic deployment:
```bash
./deploy.sh
```

### Option 2: Manual deployment

1. Install Docker:
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
sudo usermod -aG docker $USER
```

2. Install Docker Compose:
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

3. Clone and configure project:
```bash
git clone <your-repo-url>
cd solarman-bot
cp env.example .env
nano .env
mkdir logs
```

4. Launch application:
```bash
docker-compose up -d --build
```

## Automatic Launch Setup

### Option 1: Cron (recommended)

```bash
./cron_setup.sh
```

This will create a cron job for daily execution at 9:00.

### Option 2: Python Scheduler

Change the command in `docker-compose.yml`:
```yaml
command: python scheduler.py
```

### Option 3: Systemd Service

Create file `/etc/systemd/system/solarman-bot.service`:

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

## Monitoring and Management

### View Logs

```bash
# Docker container logs
docker-compose logs -f

# Application logs
tail -f logs/solarman_bot.log

# Scheduler logs
tail -f logs/scheduler.log

# Cron logs
tail -f logs/cron.log
```

### Application Management

```bash
# Stop
docker-compose down

# Restart
docker-compose restart

# Update
git pull && docker-compose up -d --build

# Manual launch
docker-compose run --rm solarman-bot python solarman_export.py
```

### Status Check

```bash
# Container status
docker-compose ps

# Resource usage
docker stats

# Check cron jobs
crontab -l
```

## Troubleshooting

### Docker Issues

```bash
# Docker cleanup
docker system prune -a

# Restart Docker
sudo systemctl restart docker

# Check permissions
sudo chown -R $USER:$USER .
```

### API Connection Issues

1. Check Solarman token in `.env` file
2. Ensure API is available
3. Check logs for connection errors

### Telegram Issues

1. Check bot token
2. Ensure bot is added to channel
3. Check bot permissions in channel

### Scheduler Issues

```bash
# Check cron jobs
crontab -l

# Restart cron
sudo systemctl restart cron

# Check cron logs
sudo tail -f /var/log/cron
```

## Security

### Basic Recommendations

1. **SSH Keys**: Use SSH keys instead of passwords
2. **Firewall**: Configure UFW to limit access
3. **Updates**: Regularly update system
4. **Environment Variables**: Don't commit `.env` file
5. **Logs**: Regularly clean logs

### Firewall Setup

```bash
# Install UFW
sudo apt install ufw

# Configure rules
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Activate
sudo ufw enable
```

### Automatic Updates

```bash
# Install unattended-upgrades
sudo apt install unattended-upgrades

# Configure
sudo dpkg-reconfigure -plow unattended-upgrades
```

## Backup

### Create Backup

```bash
# Create project archive
tar -czf solarman-bot-backup-$(date +%Y%m%d).tar.gz \
    --exclude=logs \
    --exclude=__pycache__ \
    --exclude=.git \
    .

# Backup logs
tar -czf logs-backup-$(date +%Y%m%d).tar.gz logs/
```

### Restore

```bash
# Extract archive
tar -xzf solarman-bot-backup-YYYYMMDD.tar.gz

# Restore logs
tar -xzf logs-backup-YYYYMMDD.tar.gz

# Restart
docker-compose up -d --build
```

## Scaling

### Resource Monitoring

```bash
# Install htop
sudo apt install htop

# Real-time monitoring
htop
```

### Increase Resources

If application consumes many resources:
1. Go to Digital Ocean
2. Select your Droplet
3. Click "Resize"
4. Choose larger plan
5. Confirm changes

## Support

When problems occur:

1. Check logs: `docker-compose logs`
2. Check container status: `docker-compose ps`
3. Check environment variables: `cat .env`
4. Try manual launch: `docker-compose run --rm solarman-bot python solarman_export.py`

## Application Update

```bash
# Stop
docker-compose down

# Get updates
git pull

# Rebuild and launch
docker-compose up -d --build

# Check status
docker-compose ps
``` 