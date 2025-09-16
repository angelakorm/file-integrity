from config import Config
import requests
import os

def upload_file(access_token, folder_name, file_path):
    file_name = os.path.basename(file_path)
    url = f"{Config.GRAPH_API}/{Config.VERSION}/{Config.RESOURCE}/root:/{folder_name}/{file_name}:/content"

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
