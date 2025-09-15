import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Config:
    CLIENT_ID = os.getenv("CLIENT_ID")
    AUTHORITY = os.getenv("AUTHORITY")
    SCOPES = os.getenv("SCOPES")
    GRAPH_API = os.getenv("GRAPH_API")
    VERSION = os.getenv("VERSION")
    RESOURCE = os.getenv("RESOURCE")
