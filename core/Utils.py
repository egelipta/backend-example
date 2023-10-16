# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Maintainer: dgos
@Des: 工具函数
"""

import dlib
from PIL import Image
import os
import cv2
import hashlib
import random
import uuid
from passlib.handlers.pbkdf2 import pbkdf2_sha256


def random_str():
    """
    唯一随机字符串
    :return: str
    """
    only = hashlib.md5(str(uuid.uuid1()).encode(encoding='UTF-8')).hexdigest()
    return str(only)


def en_password(psw: str):
    """
    密码加密
    :param psw: 需要加密的密码
    :return: 加密后的密码
    """
    password = pbkdf2_sha256.hash(psw)
    return password


def check_password(password: str, old: str):
    """
    密码校验
    :param password: 用户输入的密码
    :param old: 数据库密码
    :return: Boolean
    """
    check = pbkdf2_sha256.verify(password, old)
    if check:
        return True
    else:
        return False


def code_number(ln: int):
    """
    随机数字
    :param ln: 长度
    :return: str
    """
    code = ""
    for i in range(ln):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        code += ch

    return code


def cleanse_filename_for_url(filename):
    # Remove any characters that are not URL-friendly
    url_friendly_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-.'
    filename = ''.join(c for c in filename if c in url_friendly_chars)

    # Replace any remaining spaces with hyphens or underscores
    filename = filename.replace(' ', '-')

    # Convert the filename to lowercase
    filename = filename.lower()

    # Return the cleansed filename
    return filename


def remove_dots_except_last(filename, replacement_char=''):
    # Split the filename into base name and extension
    base_name, ext = os.path.splitext(filename)

    # Replace all dots in the base name with the replacement character
    base_name = base_name.replace('.', replacement_char)

    # Return the new filename
    return base_name + ext


def crop_face(path, write_path, padding):

    faceDetector = dlib.get_frontal_face_detector()
    img = cv2.imread(path)
    faces = faceDetector(img, 0)

    if len(faces) > 0:
        for i in range(0, len(faces)):
            img_h, img_w, c = img.shape
            face_h = int(faces[i].bottom() - faces[i].top())
            face_w = int(faces[i].right() - faces[i].left())

            rect_top = int(faces[i].top()) - (face_h * padding)
            if rect_top < 0:
                rect_top = 0
            rect_bottom = int(faces[i].bottom()) + (face_h * padding)
            if rect_bottom > img_h:
                rect_bottom = img_h
            rect_left = int(faces[i].left()) - (face_w * padding)
            if rect_left < 0:
                rect_left = 0
            rect_right = int(faces[i].right()) + (face_w * padding)
            if rect_right > img_w:
                rect_right = img_w

            face_img = img[int(rect_top):int(rect_bottom),
                           int(rect_left):int(rect_right)]
            cv2.imwrite(write_path, face_img)
        #  compress_image(str(write_path))


def compress_image(filename):
    # Open the image file
    img = Image.open(filename)

    # Get the current file size in bytes
    filesize = os.path.getsize(filename)
    if filesize <= 198 * 1024:  # 200KB
        # If the file size is already below 200KB, no need to compress
        return

    # Calculate the new dimensions of the image to achieve a file size <= 200KB
    width, height = img.size
    ratio = (198 * 1024) / filesize
    new_width = int(width * ratio)
    new_height = int(height * ratio)
    new_size = (new_width, new_height)

    # Resize the image
    img = img.resize(new_size, resample=Image.LANCZOS)

    # Save the compressed image as a new file
    if 'png' in filename:
        new_filename = os.path.splitext(filename)[0] + '.png'
    elif 'jpg' in filename:
        new_filename = os.path.splitext(filename)[0] + '.jpg'
    elif 'jpeg' in filename:
        new_filename = os.path.splitext(filename)[0] + '.jpeg'

    # new_filename = cleanse_filename_for_url(new_filename)
    print("new filename: ", new_filename)
    img.save(new_filename, optimize=True, quality=80)

    # Delete the original image file
    # os.remove(filename)

    # Print some output
    print(
        f"Compressed {filename} ({filesize/1024:.1f} KB) to {new_filename} ({os.path.getsize(new_filename)/1024:.1f} KB)")

# Example usage
# compress_image('my_image.jpg')


# crop_face('input/161_Akmaludin.png', 'output/161_Akmaludin.png', 0)

# import required module
