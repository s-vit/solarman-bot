# Quick Deployment of Solarman Bot on Digital Ocean

## Step 1: Create Droplet
1. Go to Digital Ocean
2. Create a new Droplet:
   - Ubuntu 22.04 LTS
   - 1GB RAM, 1 CPU (sufficient)
   - Add SSH key

## Step 2: Connect to server
```bash
ssh root@your-server-ip
```

## Step 3: Clone project
```bash
git clone <your-repo-url>
cd solarman-bot
```

## Step 4: Configure environment variables
```bash
cp env.example .env
nano .env
```
Edit the `.env` file:
- `TELEGRAM_BOT_TOKEN` - your Telegram bot token
- `TELEGRAM_CHAT_ID` - channel ID (e.g., @v7_solar)
- `SOLARMAN_TOKEN` - Solarman token (optional)

## Step 5: Automatic deployment
```bash
./deploy.sh
```

## Step 6: Setup automatic launch (optional)
```bash
./cron_setup.sh
```

## Verify operation
```bash
# View logs
docker-compose logs -f

# Manual launch
docker-compose run --rm solarman-bot python solarman_export.py
```

## Useful commands
```bash
# Stop
docker-compose down

# Restart
docker-compose restart

# Update
git pull && docker-compose up -d --build

# View logs
tail -f logs/solarman_bot.log
```

## Troubleshooting
1. **Docker errors**: `docker system prune -a`
2. **Permission issues**: `sudo chown -R $USER:$USER .`
3. **Clear logs**: `rm -rf logs/*` 