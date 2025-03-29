import os
from dotenv import load_dotenv
load_dotenv()
api_url = os.getenv('API_URL')
api_key = os.getenv('API_KEY')