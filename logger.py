import os
import sys
import logging

log = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
logs_dir = "./logs"
os.makedirs(logs_dir, exist_ok=True)
log_filepath = os.path.join(logs_dir, "running_logs.log")

logging.basicConfig(
    level=logging.INFO,
    format=log,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout),
    ]
)

logger = logging.getLogger("Logs")