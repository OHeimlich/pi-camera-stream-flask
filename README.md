# Make you own Raspberry Pi Camera Stream

Create your own live stream from a Raspberry Pi using the Pi camera module. Build your own applications from here.

## Preconditions

* Raspberry Pi 4, 2GB is recommended for optimal performance. However you can use a Pi 3 or older, you may see a increase in latency.
* Raspberry Pi 4 Camera Module or Pi HQ Camera Module (Newer version)
* Python 3 recommended.

## Library dependencies
Install the following dependencies to create camera stream.

```
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqtgui4
sudo apt-get install libqt4-test
sudo apt-get install libhdf5-dev

sudo pip3 install flask
sudo pip3 install numpy
sudo pip3 install opencv-contrib-python
sudo pip3 install imutils
sudo pip3 install opencv-python

```

Note: This installation of opencv may take a while depending on your pi model.

OpenCV alternate installation (in the event of failed opencv builds):

```
sudo apt-get install libopencv-dev python3-opencv
```

## Step 1 – Cloning Raspberry Pi Camera Stream
Open up terminal and clone the Camera Stream repo:

```
cd /home/pi
git clone https://github.com/EbenKouao/pi-camera-stream-flask.git
```

## step 2 - Create virtual environment
```
python3 -m venv venv
```
## step 3 - Install requirements 
```
pip install -r requirements.txt
```

## Step 4 – Launch Web Stream
```
python /home/pi/pi-camera-stream-flask/main.py
```

## Step 5 - Setup the detection agent
```
sudo cp agent.service /etc/systemd/system/
sudo systemctl enable agent
sudo systemctl start agent
```
