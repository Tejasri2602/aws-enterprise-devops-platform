
import os

TARGET_DIRECTORY = "./backups"

if os.path.exists(TARGET_DIRECTORY):

    for item in os.listdir(TARGET_DIRECTORY):

        path = os.path.join(TARGET_DIRECTORY, item)

        if os.path.isdir(path):
            print(f"Found backup: {path}")

print("Cleanup completed")
