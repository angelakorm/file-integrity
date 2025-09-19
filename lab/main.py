from lab.authentication import authentication
from lab.integrity_verification import sha_256
from lab.cloud_operations import create_folder, download_file, upload_file
from lab.performance import performance_measure
from lab.configuration.config import Config
import os

def main():
    access_token = authentication.get_token()

    _, elapsed, mem = performance_measure.measure_performance(create_folder.create_folder, access_token, Config.UPLOAD_FOLDER)
    print(f"Create folder: {elapsed:.4f}s, {mem:.4f} MiB")
    _, elapsed, mem = performance_measure.measure_performance(upload_file.upload_file, access_token, Config.UPLOAD_FOLDER, Config.LOCAL_FILE_PATH)
    print(f"Upload file: {elapsed:.4f}s, {mem:.4f} MiB")
    _, elapsed, mem = performance_measure.measure_performance(download_file.download_file, access_token, Config.UPLOAD_FOLDER, Config.LOCAL_FILE_PATH, Config.DOWNLOAD_FOLDER_PATH)
    print(f"Download file: {elapsed:.4f}s, {mem:.4f} MiB")

    original_hash = sha_256.sha256_hash(Config.LOCAL_FILE_PATH)
    download_hash = sha_256.sha256_hash(f"{Config.DOWNLOAD_FOLDER_PATH}/{os.path.basename(Config.LOCAL_FILE_PATH)}")

    if original_hash == download_hash:
        print("Hashes match.")
    else:
        print("Hashes do not match.")

if __name__ == "__main__":
    main()