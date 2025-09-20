from helpers.config import get_settings, Settings
import os 
import random
import string

UPLOAD_DIR = "/content/"
os.makedirs(UPLOAD_DIR, exist_ok=True)
class BaseController :
    def __init__(self):

     self.app_settings = get_settings()
     self.base_dir = UPLOAD_DIR
     self.files_dir = os.path.join(
            self.base_dir,
            "files"
        )
        
    def generate_random_string(self, length: int=12):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
