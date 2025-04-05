# Installation Guide for Face Recognition System

Use ```install_dependencies.sh``` to setup your machine. If issues occur, the install guide below is referred to.

## Python Compatibility
- Recommended: **Python 3.10.10**, which can be installed with deadsnakes for Linux.
- Not compatible with Python 3.11 or newer.
- Use **numpy 1.24** (not 2.0).

Using a virtual environment:
```bash
python3.10 -m venv venv
source venv/bin/activate
```

---

## dlib installation
### Linux:
```bash
sudo apt-get update
sudo apt-get install build-essential cmake

git clone https://github.com/davisking/dlib.git

python3 -m venv ~/dlib_env
source ~/dlib_env/bin/activate

cd dlib
python setup.py install
```
### Windows:
Download dlib-19.22.99-cp310-cp310-win_amd64.whl from the dlib GitHub.

Install with pip:
```
python -m pip install dlib-19.22.99-cp310-cp310-win_amd64.whl
```
