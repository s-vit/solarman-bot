import schedule
import time
import logging
from solarman_export import main as run_report

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/scheduler.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def job():
    """Execute scheduled task"""
    logger.info("Starting scheduled task")
    try:
        run_report()
        logger.info("Task completed successfully")
    except Exception as e:
        logger.error(f"Error executing task: {str(e)}")

def main():
    """Main scheduler function"""
    logger.info("Starting Solarman Bot scheduler")
    
    # Schedule task for every day at 9:00
    schedule.every().day.at("09:00").do(job)
    
    # You can also add other schedules
    # schedule.every().monday.at("09:00").do(job)  # Mondays only
    # schedule.every(1).hours.do(job)  # Every hour
    
    logger.info("Scheduler configured for daily execution at 09:00")
    
    # Infinite loop for task execution
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main() 