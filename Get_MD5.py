"""
Get_MD5 -获取文件MD5哈希签名，保证不被篡改

Author: Sizhuo Li
Date: 2023/7/21
"""
from hashlib import md5

hasher = md5()

path = 'E:/python/python-3.10.11-amd64.exe'
file = open(path, 'rb')

try:
    data = file.read(512)
    while data:
        hasher.update(data)
        data = file.read(512)
finally:
    file.close()
print(hasher.hexdigest())