from config import Config
import requests
from lab import *


def create_folder(access_token, folder_name):
    url = f"{Config.GRAPH_API}/{Config.VERSION}/{Config.RESOURCE}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    folder_data = {
        "name": folder_name,
        "folder": {},
        "@microsoft.graph.conflictBehavior": "rename"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code in [200, 201]:
        print("Folder created successfully.")
    else:
        print("Failed to create folder.")


