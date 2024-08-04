import hashlib

# MD5 加密
def md5(input_string: str):
    return hashlib.md5(input_string.encode('utf-8')).hexdigest()