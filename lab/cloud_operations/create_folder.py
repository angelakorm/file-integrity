from lab.configuration.config import Config
import requests

def create_folder(access_token, folder_name):
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
