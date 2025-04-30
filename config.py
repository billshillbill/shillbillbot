# config.py
import os
from dotenv import load_dotenv

load_dotenv()

BITLY_API_KEY = os.getenv("BITLY_API_KEY")
TYPEFULLY_API_KEY = os.getenv("TYPEFULLY_API_KEY")
TYPEFULLY_USERNAME = os.getenv("TYPEFULLY_USERNAME")
