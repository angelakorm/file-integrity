import hashlib

def sha256_hash(file_path):
    hash_obj = hashlib.sha256()
    with open(file_path, "rb") as file:
        while byte_block := file.read(4096):
            hash_obj.update(byte_block)
    return hash_obj.hexdigest()