from abc import ABC, abstractmethod

class Verifier(ABC):
    @abstractmethod
    def verifying_algorithm(self, file_path):
        pass