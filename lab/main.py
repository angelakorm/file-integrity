from lab import authentication, upload, download, integrity_verification, performance_measure
from config import Config
import os

def main():
    access_token = authentication.get_token()

    _, elapsed, mem = performance_measure.measure_performance(upload.create_folder, access_token, Config.UPLOAD_FOLDER)
    print(f"Create folder: {elapsed:.4f}s, {mem:.4f} MiB")
    _, elapsed, mem = performance_measure.measure_performance(upload.upload_file, access_token, Config.UPLOAD_FOLDER, Config.LOCAL_FILE_PATH)
    print(f"Upload file: {elapsed:.4f}s, {mem:.4f} MiB")
    _, elapsed, mem = performance_measure.measure_performance(download.download_file, access_token, Config.UPLOAD_FOLDER, Config.LOCAL_FILE_PATH, Config.DOWNLOAD_FOLDER_PATH)
    print(f"Download file: {elapsed:.4f}s, {mem:.4f} MiB")

    original_hash = integrity_verification.sha256_hash(Config.LOCAL_FILE_PATH)
    download_hash = integrity_verification.sha256_hash(f"{Config.DOWNLOAD_FOLDER_PATH}/{os.path.basename(Config.LOCAL_FILE_PATH)}")

    if original_hash == download_hash:
        print("Hashes match.")
    else:
        print("Hashes do not match.")

if __name__ == "__main__":
    main()