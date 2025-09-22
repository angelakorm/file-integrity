import hashlib
from lab.integrity_verification.verifier import Verifier

class SHA256(Verifier):
    def verifying_algorithm(self, file_path):
        hash_obj = hashlib.sha256()
        with open(file_path, "rb") as file:
            while byte_block := file.read(4096):
                hash_obj.update(byte_block)
        return hash_obj.hexdigest()