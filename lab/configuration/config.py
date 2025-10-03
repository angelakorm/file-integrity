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
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
    LOCAL_FILE_PATH = os.getenv("LOCAL_FILE_PATH")
    DOWNLOAD_FOLDER_PATH = os.getenv("DOWNLOAD_FOLDER_PATH")
    PROVIDER = os.getenv("PROVIDER")
    VERIFIER = os.getenv("VERIFIER")
    DROPBOX_ACCESS_TOKEN = os.getenv("DROPBOX_ACCESS_TOKEN")
