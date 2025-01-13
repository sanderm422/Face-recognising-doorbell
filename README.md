# **Camera with Face Recognition**

A smart doorbell system built with a Raspberry Pi Zero W that streams video via a Flask server to an external device for face recognition. This project combines Linux, Python, and Flask to create an intelligent and portable solution for home security.

---

## **Introduction**
The primary objective of this project is to develop a smart system that recognizes faces and notifies the user when someone is at the door. Initially intended as a handheld camera, the project shifted focus due to hardware limitations on the Raspberry Pi Zero W.

### **Project Highlights**
- Streams live video from the Raspberry Pi to a laptop using Flask.
- External device performs face recognition and sends real-time notifications.
- Designed to be compact, portable, and battery-powered.
- Runs entirely on Linux with Python virtual environments for software isolation.

---

## **Hardware**

### **Component List**
- **Raspberry Pi Zero W**: The core processor for video streaming.
- **PiCamera Module (OV5647 sensor)**: Captures video for processing.
- **LCD 1x16 Display (JHD161A TN)**: (Optional) Displays status messages.
- **LiPO Battery (1200mAh)**: Powers the system for mobility.
- **Powerboost 1000c (Adafruit)**: Manages power and charging.
- **Switch**: Enables convenient system power control.
- **3D-Printed Casing (PLA)**: Encases the components securely.

---

## **Software**

### **Setup**
The Raspberry Pi runs Raspbian OS. A Python virtual environment is used for installing and isolating libraries required for face recognition. The system uses the `face_recognition` library, along with the following tools:

1. **Python (3.9)**: Installed using `pyenv` due to compatibility issues with newer Python versions.
2. **Numpy and Scipy**: Installed with specific versions to ensure compatibility.
3. **Dlib**: Installed using cross-compilation to overcome hardware limitations.
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
