
from datetime import datetime
import shutil
import os

SOURCE_DIR = "./application"
BACKUP_DIR = "./backups"

os.makedirs(BACKUP_DIR, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

backup_path = f"{BACKUP_DIR}/backup_{timestamp}"

shutil.copytree(SOURCE_DIR, backup_path)

print(f"Backup created: {backup_path}")
