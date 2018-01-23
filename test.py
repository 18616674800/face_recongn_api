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
file_path = "/Users/dtan11/.virtualenvs/face_recognition_p3/picture/WechatIMG25.jpg"
#file_path = "/Users/dtan11/.virtualenvs/face_recognition_p3/picture/category-women-img-06.png"

# 读取图片
image = face_recognition.load_image_file(file_path)

# Define Recognition model
# CPU Model
recogn_mode = "hog"
# GPU Model
#recogn_mode = "cnn"

# 获取人脸位置
face_locations = face_recognition.face_locations(image, model=recogn_mode)
# 格式 top, right, bottom, left
for face in face_locations:
    print(type(face))
    box = (face[3],face[0],face[1],face[2])
    cv2.rectangle(image, (face[3],face[0]), (face[1],face[2]), (0, 0, 255), 2)
    cv2.imwrite('contours.png',image)

# 获取面部细节位置
face_landmarks_list = face_recognition.face_landmarks(image)
print(face_landmarks_list)
#获取人脸code
face_encoding = face_recognition.face_encodings(image)[0]


print(len(face_recognition.face_encodings(image)))
# search image
search_image_path = "/Users/dtan11/.virtualenvs/face_recognition_p3/picture/WechatIMG25.jpg"
search_image = face_recognition.load_image_file(search_image_path)
search_image_encoding = face_recognition.face_encodings(search_image)[0]

# 转list 转ndarray
# print(np.array(search_image_encoding.tolist()))

start = time.clock()
print(face_encoding.tolist())
print(search_image_encoding.tolist())
results = face_recognition.compare_faces([face_encoding], search_image_encoding)
end = time.clock()

# running time
# CPU running time
print(end-start)

print(results)


def compare_faces_tolerance(known_face_encodings, face_encoding_to_check):
    """
    Compare a list of face encodings against a candidate encoding to see if they match.

    :param known_face_encodings: A list of known face encodings
    :param face_encoding_to_check: A single face encoding to compare against the list
    :param tolerance: How much distance between faces to consider it a match. Lower is more strict. 0.6 is typical best performance.
    :return: A list of True/False values indicating which known_face_encodings match the face encoding to check
    """
    return face_recognition.face_distance(known_face_encodings, face_encoding_to_check)

results = compare_faces_tolerance([face_encoding], search_image_encoding)
print(results)




# file_name = serializer.data['picture'].split('/')[-1]
#         file_path = os.path.join(settings.UPLOAD_ROOT, file_name)
#         file_detected_path = os.path.join(settings.DETECTED_ROOT, file_name)
#         # Load image
#         image = face_recognition.load_image_file(file_path)
#         # get face detail
#         # face_landmarks_list = face_recognition.face_landmarks(image)
#         face_encoding = face_recognition.face_encodings(image)
#         if len(face_encoding) == 1:
#             face_encoding = face_encoding[0]
#         else:
#             # 2 face in one picture
#             face_encoding = face_encoding[0]
#         #  ndarray 转 list
#         face_encoding_list = face_encoding.tolist()
#         print(face_encoding_list)
#
#         # print(np.array(search_image_encoding.tolist()))
#
#         # get face location
#         #face_locations = face_recognition.face_locations(image, model=settings.RECOGN_MODE)
#         # mark the face and save picture
#         #for face in face_locations:
#         #    box = (face[3], face[0], face[1], face[2])
#         #    cv2.rectangle(image, (face[3], face[0]), (face[1], face[2]), (0, 0, 255), 2)
#         #    cv2.imwrite(file_detected_path, image)

#
# def get_file_path(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = "%s.%s" % (uuid.uuid4(), ext)
#     return os.path.join('upload/', filename)
#
#
# class FaceInfo(models.Model):
#     """
#     人脸上传
#     """
#     faceset = models.ForeignKey(FaceSets, verbose_name="人脸库", help_text="储存到对应的人脸库",related_name="face_sets")
#     name = models.CharField(max_length=100, default="", verbose_name="用户名")
#     picture = models.ImageField(upload_to=get_file_path,verbose_name="用户图片")
#     add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
#
#     class Meta:
#         verbose_name = '人脸上传'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name