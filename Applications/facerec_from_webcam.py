import face_recognition
import cv2
import requests
import json
import random

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
facesets = "1"
API_BASEURL = "http://127.0.0.1:8000"
tolerance_threadhold = 0.6
class CompareFace:
    """
    人脸比较接口
    """

    def __init__(self):
        """
        初始化相关数据,包括接口的url,headers和parm
        :return: None
        """
        self.url = API_BASEURL+"/CompareFaces/"
        self.headers = {
            "Authorization":"JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTE4MTA1OTMxLCJlbWFpbCI6IiJ9.kX5zV4iZVEu3AtsP0rrzUKALhVQPkyTYFEN216tVNhI",
            "Content-Type":"application/json"
        }

    def compare_face(self, faceset,search_encode ):
        """

        :return:data
        """
        parm = {
            'faceset': faceset,
            'search_encode':search_encode,

        }

        pd_data = requests.post(self.url, data=json.dumps(parm), headers=self.headers)
        result = pd_data.json()
        result['status_code'] = pd_data.status_code
        return result


# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)




while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            face_encoding = str(face_encoding.tolist())
            com = CompareFace()
            result = com.compare_face(facesets, face_encoding)
            del com
            if float(result['tolerance']) <= tolerance_threadhold :
                name = result['related_name']
            else :
                name = "Unknown"

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()