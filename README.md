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

---

## **Software**

### **Dependencies**
The Raspberry Pi runs Raspbian OS. A Python virtual environment is used for installing and isolating libraries required for face recognition. The system uses the `face_recognition` library, along with the following tools:

1. **Python (3.9) with NumPy1.24**: The script runs within a virtual environment which ensures compatibility with dlib without having to downgrade the system-wide version of Python. Installed using `pyenv`.
2. **Face recognition python library** [face_recognition](https://github.com/ageitgey/face_recognition) - .
3. **Dlib**: The face recognition library is built using dlib. 
4. **Flask**: For setting up the video streaming server.

### **Flask Server**
The Raspberry Pi runs a Flask server that streams live video. The external device accesses this stream and runs face recognition scripts.

---

## **Implementation**

### **Hardware Assembly**
1. Solder the battery to the power management board and connect it to the Raspberry Pi through a switch.
2. Assemble the 3D-printed casing to house the components securely.
3. Attach the PiCamera module and position it for optimal video capture.

### **Software Workflow**
1. Set up the Python virtual environment (`venv`) using `pyenv`.
2. Install dependencies and libraries within the `venv`.
3. Configure the Flask server to stream video from the camera module.
4. On the external device, run the face recognition script that processes the video stream and identifies individuals.

---

## **Results**
- The system successfully streams live video from the Raspberry Pi to an external device.
- Face recognition is performed in real-time, triggering notifications on the laptop.

---

## **Upcoming Features**
1. Add a **LiPO battery** to make the system fully wireless.
2. Automate the startup process by running the Flask server and face recognition script at boot.
3. Improve notification features with a more advanced user interface, potentially using Tkinter or another GUI framework.

---

## **Gallery**
- Images of the hardware setup.
- Screenshots of the Flask server video stream.
- Demonstrations of the face recognition system in action.

---

## **License**
This project is open source under the [MIT License](LICENSE).

---

## **Contact**
For questions or collaboration opportunities, feel free to reach out or submit an issue on this repository.

---

## **Acknowledgments**
Thanks to the open-source community for providing tools and resources that made this project possible.
