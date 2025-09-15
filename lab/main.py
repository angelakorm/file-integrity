from lab import authentication, upload, download, integrity_verification
from config import Config
import os

def main():
    access_token = authentication.get_token()
    upload.create_folder(access_token, Config.UPLOAD_FOLDER)
    upload.upload_file(access_token, Config.UPLOAD_FOLDER, Config.LOCAL_FILE_PATH)
    download.download_file(access_token, Config.UPLOAD_FOLDER, Config.LOCAL_FILE_PATH, Config.DOWNLOAD_FOLDER_PATH)

    original_hash = integrity_verification.sha256_hash(Config.LOCAL_FILE_PATH)
    download_hash = integrity_verification.sha256_hash(f"{Config.DOWNLOAD_FOLDER_PATH}/{os.path.basename(Config.LOCAL_FILE_PATH)}")

    if original_hash == download_hash:
        print("Hashes match.")
    else:
        print("Hashes do not match.")

if __name__ == "__main__":
    main()