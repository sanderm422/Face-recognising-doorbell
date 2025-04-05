import os
import cv2
import numpy as np
import face_recognition
import requests
from io import BytesIO
from PIL import Image

# CONFIG
KNOWN_FACES_DIR = 'data/known_faces'
VIDEO_STREAM_URL = 'http://raspberrypi.local:5000/video_feed'  # Change to your Pi's URL

# Lists to hold encodings and labels
encodings_known_faces = []
known_faces_names = []

# Converts BGR images to RGB 8-bit
def convert_img(bgr_im):
    rgb_im = cv2.cvtColor(bgr_im, cv2.COLOR_BGR2RGB)
    return rgb_im.astype('uint8')

# Load known faces
print("Loading known faces...")
for name in os.listdir(KNOWN_FACES_DIR):
    person_dir = os.path.join(KNOWN_FACES_DIR, name)
    if not os.path.isdir(person_dir):
        continue
    for filename in os.listdir(person_dir):
        filepath = os.path.join(person_dir, filename)
        image = cv2.imread(filepath)
        if image is None:
            continue
        rgb_image = convert_img(image)
        encodings = face_recognition.face_encodings(rgb_image)
        if encodings:
            encodings_known_faces.append(encodings[0])
            known_faces_names.append(name)
print(f"Loaded {len(encodings_known_faces)} faces.")

# MJPEG Stream reader
def get_mjpeg_frame(url):
    stream = requests.get(url, stream=True)
    bytes_data = bytes()
    for chunk in stream.iter_content(chunk_size=1024):
        bytes_data += chunk
        a = bytes_data.find(b'\xff\xd8')
        b = bytes_data.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = bytes_data[a:b+2]
            bytes_data = bytes_data[b+2:]
            frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            yield frame

# Main loop
for frame in get_mjpeg_frame(VIDEO_STREAM_URL):
    if frame is None:
        continue

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        
        matches = face_recognition.compare_faces(encodings_known_faces, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(encodings_known_faces, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_faces_names[best_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
