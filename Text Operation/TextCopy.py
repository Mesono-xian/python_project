"""
TextCopy - 文件的复制

Author: Sizhuo Li
Date: 2023/7/21
"""
with open('C:/Users/Lumina/Pictures/Potter.png', 'rb') as source:
    with open('C:/Users/Lumina/Desktop/harry.png', 'wb') as target:
        data = source.read(512)
        while data:
            target.write(data)
            data = source.read(512)
