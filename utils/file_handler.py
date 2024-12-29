import os
import shutil
from config.config import TEMP_DOWNLOAD_PATH

def cleanup_files(file_path: str):
    """Remove temporary files after processing"""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Error cleaning up files: {str(e)}")

def cleanup_temp_folder():
    """Clean up entire temporary folder"""
    try:
        if os.path.exists(TEMP_DOWNLOAD_PATH):
            shutil.rmtree(TEMP_DOWNLOAD_PATH)
            os.makedirs(TEMP_DOWNLOAD_PATH)
    except Exception as e:
        print(f"Error cleaning up temp folder: {str(e)}")