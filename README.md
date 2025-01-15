# **Camera with Face Recognition**

A doorbell system built with a Raspberry Pi Zero W that streams video via a Flask server to an external device for face recognition and automatic popups with information about who is outside the door.

---

## **Introduction**
This project aims to implement face recognition using dlib on a compact and cheap single board computer. Initially intended to run without external computing but shifted focus limited hardware, while maintaining the goal of using having a compact product at the end.

### **Project Highlights**
- Streams live video from the Raspberry Pi using a Flask-server.
- The users device performs face recognition and sends real-time notifications.
- Designed to be compact.

---

## **Hardware**

### **Component List**
- **Raspberry Pi Zero W**: The core processor for video streaming.
- **PiCamera Module (OV5647 sensor)**: Captures video for processing.
- **Power bank**
- **3D-printed housing** - A couple of designs in the `hardware/` directory.

---

## **Software**

### **Dependencies**
The Raspberry Pi runs Raspbian OS. A Python virtual environment is used for installing and isolating libraries required for face recognition. The system uses the `face_recognition` library, along with the following tools:

1. **Python (3.9) with NumPy1.24**: The script runs within a virtual environment which ensures compatibility with dlib without having to downgrade the system-wide version of Python. Installed using `pyenv`.
2. **[face_recognition](https://github.com/ageitgey/face_recognition) python library**: Used for face recognition.
3. **Dlib**: The face recognition library is built using [dlib](https://github.com/davisking/dlib). 
4. **Flask**: Video streaming server hosted by the Raspberry Pi.
---

## **Implementation**

### **Software Workflow**
#### **On the users computer**
1. Set up a Python virtual environment using `pyenv`. Make sure the version of python is compatible with dlib.
2. Install dependencies and libraries within the venv.
3. Run the script `picam_recog.py` on the users computer.
#### **On the raspberry Pi**
5. Prepare the Raspberry Pi with SSH and set up the video streaming script `pistream.py` with SCP.
6. Run the script.

---

## **Results**
The compact system mounts on a door nicely. Whenever there is a person outside the door the user gets a pop-up containing the name of the person if known, otherwise a photo can be captured and the person added to known people. The system has very hiogh accuracy.

