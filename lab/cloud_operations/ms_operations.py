from lab.cloud_operations.cloud_operations import Operations
from lab.configuration.config import Config
import requests
import os

class MSOperations(Operations):
    def __init__(self):
        pass

    def create_folder(self, access_token, folder_name):
        check_url = f"{Config.GRAPH_API}/{Config.VERSION}/{Config.RESOURCE}/root:/{folder_name}"

        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        check_response = requests.get(check_url, headers=headers)

        if check_response.status_code == 200:
            print("Folder already exists.")
            return True
        elif check_response.status_code == 404:
            url = f"{Config.GRAPH_API}/{Config.VERSION}/{Config.RESOURCE}/root/children"

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
        else:
            print("Error checking folder.")
            return False

    def upload_file(self, access_token, folder_name, file_path):
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

    def download_file(self, access_token, folder_name, file_path, download_folder):
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

