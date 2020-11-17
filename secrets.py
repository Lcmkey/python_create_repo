import os
from dotenv import load_dotenv
# import getpass

load_dotenv()

# WHOAMI = getpass.getuser()
WHOAMI = os.getlogin()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
API_URL = os.getenv("API_URL")
OWNER = os.getenv("OWNER")
