from lab.authentication.dbx_authentication import DBXAuthentication
from lab.authentication.ms_authentication import MSAuthentication
from lab.integrity_verification.sha256 import SHA256
from lab.performance import performance_measure
from lab.configuration.config import Config
from lab.cloud_operations.ms_operations import MSOperations
import os

def main():
    if Config.PROVIDER == "Microsoft":
        authenticator = MSAuthentication()
        access_token = authenticator.get_access_token()
        # access_token2 = authenticator.get_access_token()
        operations = MSOperations()
    elif Config.PROVIDER == "Dropbox":
        authenticator = DBXAuthentication()
        access_token = authenticator.get_access_token()
    else:
        print("Invalid cloud provider.")

    _, elapsed, mem = performance_measure.measure_performance(operations.create_folder, access_token, Config.UPLOAD_FOLDER)
    print(f"Create folder: {elapsed:.4f}s, {mem:.4f} MiB")
    _, elapsed, mem = performance_measure.measure_performance(operations.upload_file, access_token, Config.UPLOAD_FOLDER, Config.LOCAL_FILE_PATH)
    print(f"Upload file: {elapsed:.4f}s, {mem:.4f} MiB")
    _, elapsed, mem = performance_measure.measure_performance(operations.download_file, access_token, Config.UPLOAD_FOLDER, Config.LOCAL_FILE_PATH, Config.DOWNLOAD_FOLDER_PATH)
    print(f"Download file: {elapsed:.4f}s, {mem:.4f} MiB")

    if Config.VERIFIER == "SHA256":
        verifier = SHA256()
    else:
        print("Invalid verification method.")

    original_hash = verifier.verifying_algorithm(Config.LOCAL_FILE_PATH)
    download_hash = verifier.verifying_algorithm(f"{Config.DOWNLOAD_FOLDER_PATH}/{os.path.basename(Config.LOCAL_FILE_PATH)}")

    if original_hash == download_hash:
        print("Hashes match.")
    else:
        print("Hashes do not match.")

if __name__ == "__main__":
    main()