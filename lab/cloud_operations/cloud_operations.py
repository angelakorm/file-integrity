from abc import ABC, abstractmethod

class Operations(ABC):
    @abstractmethod
    def create_folder(self, access_token, folder_name):
        pass

    @abstractmethod
    def upload_file(self, access_token, folder_name, file_path):
        pass

    @abstractmethod
    def download_file(self, access_token, folder_name, file_path, download_folder):
        pass