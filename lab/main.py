from lab import authentication, upload, download
from config import Config

def main():
    access_token = authentication.get_token()
    upload.create_folder(access_token, Config.UPLOAD_FOLDER)
    upload.upload_file(access_token, Config.UPLOAD_FOLDER, Config.LOCAL_FILE_PATH)
    download.download_file(access_token, Config.UPLOAD_FOLDER, Config.LOCAL_FILE_PATH, Config.DOWNLOAD_FOLDER_PATH)

if __name__ == "__main__":
    main()