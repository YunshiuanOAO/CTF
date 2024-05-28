import io
import secrets
import hashlib
from os import getenv

from flask import Flask, request, jsonify, render_template
from PIL import Image, ImageChops

import util
# 假設 target_image 是已經創建好的目標圖片

def generate_image():
    h = hashlib.sha256(secrets.token_bytes(16)).hexdigest()

    image = Image.new("L", (16, 16), 0)
    pixels = [255 if c == '1' else 0 for c in bin(int(h, 16))[2:].zfill(256)]
    image.putdata(pixels)
    return image

def generate_image2():
    h = hashlib.sha256(secrets.token_bytes(16)).hexdigest()
    print(h)
    image2 = Image.new("L", (16, 16), 0)
    pixels = [255 if c == '1' else 255 for c in bin(int(h, 16))[2:].zfill(256)]
    image2.putdata(pixels)
    return image2


myimage = generate_image2()
target_image = generate_image()

def is_same_image(img1: Image.Image, img2: Image.Image) -> bool:
    #img1 = img1.convert('RGB')
    #img2 = img1.convert('RGB')
    #print(img1.getbbox())
    #print(img2.getbbox())
    data = ImageChops.difference(img1, img2)
    img1.save("img1.png")
    img2.save("img2.png")
    data.save("test.png")

    print(ImageChops.difference(img1, img2))
    print(ImageChops.difference(img1, img2).getbbox())
    return ImageChops.difference(img1, img2).getbbox() == None

print(is_same_image(target_image,myimage))

# 獲取目標圖片的像素數據
pixels = list(target_image.getdata())

# 創建一個新的圖片對象，與目標圖片相同的尺寸和模式
new_image = Image.new("L", target_image.size)

# 將目標圖片的像素數據填充到新圖片中
new_image.putdata(pixels)

# 可以選擇保存這個新圖片
new_image.save("new_image.png")
