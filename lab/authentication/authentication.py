from abc import ABC, abstractmethod

class Authenticator(ABC):
    @abstractmethod
    def get_access_token(self):
        pass