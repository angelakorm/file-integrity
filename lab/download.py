from config import Config
import requests
import os

def download_file(access_token, folder_name, file_path, download_folder):
    file_name = os.path.basename(file_path)
    url = f"{Config.GRAPH_API}/{Config.VERSION}/{Config.RESOURCE}/root:/{folder_name}/{file_name}:/content"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    download_path = f"{download_folder}/{file_name}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with open(download_path, "wb") as file_data:
            file_data.write(response.content)
            print("File downloaded successfully.")
    else:
        print("Failed to download file.")
