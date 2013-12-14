djandro
=======

Django on Android

A friend of mine wanted to get an offline version of his django site that he could carry around on his phone, so I made this app. It basically starts django as a service that runs in the background, and you can connect to it using your phone's browser.

## Requirements
- python-for-android
- django

## Steps
### 1. Get python-for-android
- Get your environment set-up by following this [link](http://python-for-android.readthedocs.org/en/latest/toolchain/).
- Downloading the .vbi image and running it in Virtualbox is the quickest option.

### 2. Distribute
Create your Arm distribution of Python
```
python-for-android$ ./distribute.sh -m "kivy sqlite3"
```
### 3. Include modules
Comment out the following modules from `python-for-android/dist/default/blacklist.txt`:
```
# - sqlite3 (2 lines to comment out)
# - wsgiref
# - unittest
```
### 4. Download [django](https://github.com/django/django/tree/master/django)
Place it into the `service` folder of this project

### 5. Build the app
```
python-for-android/dist/default$ ./build.py --package com.example.djandro \
  --name "Djandro" \
  --version 1 \
  --permission INTERNET \
  --dir path/to/djandro debug installd
```
`installd` will install if the phone is connected via USB. If you are using the VM and haven't configured USB, you can scp the .apk file to your local (non-virtual) machine or upload it somewhere and grab it from your phone, etc.

## Connect

1. Run the app. The first run can take a couple of minutes because python and the various media files have to get unpacked. Be patient.

2. Open the phone's browser to `http://localhost:8000/myapp/`.

The site should also be available from other devices connected to the same network (replace `localhost` with the IP of your device). When no networks are in range, your device can be used as a router while it serves Django:

Android Settings > More... > Tethering & portable hotspot > Portable Wi-Fi hotspot (check) 
