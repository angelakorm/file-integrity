import os
import dropbox
from lab.cloud_operations.cloud_operations import Operations
from lab.configuration.config import Config


class DBXOperations(Operations):
    def __init__(self):
        self.dbx = dropbox.Dropbox(Config.DROPBOX_ACCESS_TOKEN)

    def create_folder(self, access_token, folder_name):
        folder_path = f"/{folder_name}"

        try:
            self.dbx.files_get_metadata(folder_path)
            print("Folder already exists.")
            return False
        except dropbox.exceptions.ApiError as e:
            if e.error.is_path() and e.error.get_path().is_not_found():
                try:
                    self.dbx.files_create_folder_v2(folder_path)
                    print(f"Folder created.")
                    return True
                except Exception as ex:
                    print("Error creating folder:", ex)
                    return False
            else:
                print("Error checking folder:", e)


    def upload_file(self, access_token, folder_name, file_path):
        file_name = os.path.basename(file_path)
        folder_path = f"/{folder_name}/{file_name}"

        with open(file_path, "rb") as file_data:
            try:
                self.dbx.files_upload(file_data.read(),folder_path)
                print("File successfully uploaded.")
                return True
            except Exception as e:
                print("Error uploading file:", e)
                return False

    def download_file(self, access_token, folder_name, file_path, download_folder):
        file_name = os.path.basename(file_path)
        folder_path = f"/{folder_name}/{file_name}"
        download_path = f"{download_folder}/{file_name}"

        try:
            metadata, res = self.dbx.files_download(folder_path)
            with open(download_path, "wb") as file_data:
                file_data.write(res.content)
            print(f"File successfully downloaded.")
            return True
        except Exception as e:
            print("Download failed:", e)
            return False

