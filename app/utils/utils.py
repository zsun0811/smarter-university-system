

import hashlib


def generate_id(seed:str) -> str:
    """
    Generates unique identifier for data
    that is stored as part of the application.
    """
    return hashlib.md5(seed.encode('utf-8')).hexdigest()