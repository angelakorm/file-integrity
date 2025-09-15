from config import Config
import requests
import os

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

    response = requests.post(url, headers=headers, json=folder_data)

    if response.status_code in [200, 201]:
        print("Folder created successfully.")
    else:
        print("Failed to create folder.")

def upload_file(access_token, folder_name, file_path):
    file_name = os.path.basename(file_path)
    url = f"{Config.GRAPH_API}/{Config.VERSION}/me/drive/root:/{folder_name}/{file_name}:/content"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    with open(file_path, "rb") as file_data:
        response = requests.put(url, headers=headers, data=file_data)

    if response.status_code in [200, 201]:
        print("File uploaded successfully.")
    else:
        print("Failed to upload file.")
