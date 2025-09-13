import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Config:
    CLIENT_ID = os.getenv("CLIENT_ID")
    AUTHORITY = os.getenv("AUTHORITY")