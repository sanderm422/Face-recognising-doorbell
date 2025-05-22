import os
import cv2
import numpy as np
import face_recognition
import requests
from io import BytesIO
from PIL import Image

# CONFIG
KNOWN_FACES_DIR = 'data/known_faces'
pi_ip = '192.168.0.238:5000'
VIDEO_STREAM_URL = f'http://{pi_ip}/video_feed'

def convert_img(bgr_im):
    rgb_im = cv2.cvtColor(bgr_im,cv2.COLOR_BGR2RGB)
    rgb_im.astype('uint8')
    return rgb_im

# Load images with faces and create facial feature encodings

# Image 1. Sander
sanderimg = cv2.imread("data/known_faces/sander.jpg")
rgb_sanderim = convert_img(sanderimg)

# Image 2. Paulina
pau = cv2.imread("data/known_faces/pau.jpg")
rgb_pau = convert_img(pau)

pau_face_encoding = face_recognition.face_encodings(rgb_pau)[0]
sander_face_encoding = face_recognition.face_encodings(rgb_sanderim)[0]

# Facial feature encodings and names are stored in lists
encodings_known_faces = [sander_face_encoding, pau_face_encoding]
known_faces_names = ['Sander','Paulina']

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

    rgb_frame = convert_img(frame)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        
        matches = face_recognition.compare_faces(encodings_known_faces, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(encodings_known_faces, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_faces_names[best_match_index]

        padding = 38
        top = max(0, top - padding)
        right = min(frame.shape[1], right + padding)
        bottom = min(frame.shape[0], bottom + padding)
        left = max(0, left - padding)


        # Special heart drawing if recognized as Paulina
        if name == "Paulina":
            # Heart color
            heart_color = (255, 0, 255)  # Pinkish color (BGR)

            # Coordinates for center of heart
            center_x = (left + right) // 2
            center_y = (top + bottom) // 2
            width = right - left
            height = bottom - top

            # Draw two circles for heart top
            radius = min(width, height) // 6
            cv2.circle(frame, (center_x - radius, center_y - radius), radius, heart_color, -1)
            cv2.circle(frame, (center_x + radius, center_y - radius), radius, heart_color, -1)

            # Draw the triangle for heart bottom
            points = np.array([
                [center_x - 2 * radius, center_y - radius],
                [center_x + 2 * radius, center_y - radius],
                [center_x, center_y + 2 * radius]
            ])
            cv2.fillPoly(frame, [points], heart_color)

        else:
            # Choose color based on if recognized or unknown
            if name == "Unknown":
                box_color = (0, 102, 255)  # Light red
            else:
                box_color = (0, 255, 0)    # Green

            # Draw rectangle around face
            cv2.rectangle(frame, (left, top), (right, bottom), box_color, 2)

            # Draw rectangle behind name
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), box_color, cv2.FILLED)


        # Draw rectangle around face
        cv2.rectangle(frame, (left, top), (right, bottom), box_color, 2)

        # Draw rectangle behind name
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), box_color, cv2.FILLED)

        # Draw the name text (black color now)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 0, 0), 1)

    # Show the frame
    cv2.imshow('Video', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()