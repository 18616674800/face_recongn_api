import face_recognition
import numpy as np
import time
try:
    from PIL import Image, ImageFilter
except ImportError:
    import Image
    import ImageFilter
import cv2
import os
# Define Image path
#file_path = "/Users/dtan11/.virtualenvs/face_recognition_p3/picture/WechatIMG25.jpg"

#file_path = "/Users/dtan11/.virtualenvs/face_recognition_p3/picture/face_detect_43362039_1510546674.jpg"
file_path = "/Users/dtan11/.virtualenvs/p3.6_face_recognition/picture/Yaxi.jpg"
# 读取图片
image = face_recognition.load_image_file(file_path)

# Define Recognition model
# CPU Model
recogn_mode = "hog"
# GPU Model
#recogn_mode = "cnn"

# 获取面部细节位置
if len(face_recognition.face_landmarks(image)) == 1 :
    face_landmarks = face_recognition.face_landmarks(image)[0]
    #获取人脸code
    face_encoding = face_recognition.face_encodings(image)[0].tolist()
else :
    face_landmarks = face_recognition.face_landmarks(image)[0]
    # 获取人脸code
    face_encoding = face_recognition.face_encodings(image)[0].tolist()

print(face_landmarks)
print(face_encoding)