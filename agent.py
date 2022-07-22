import datetime
import logging
from io import BytesIO
from time import sleep
from PIL import Image
import requests
from picamera import PiCamera

import config
# from camera import VideoCamera

# cam = VideoCamera()
last_report = datetime.datetime.utcnow()


def get_frame():
    # Create the in-memory stream
    stream = BytesIO()
    camera = PiCamera(resolution=(2560, 1440))
    camera.start_preview()
    sleep(3)
    camera.capture(stream, format='jpeg')
    camera.close()
    # "Rewind" the stream to the beginning so we can read its content
    stream.seek(0)
    image = Image.open(stream)
    return image, stream

def detect():
    frame, stream = get_frame()
    url = f"http://{config.url}:8000/model/inference_and_report"
    response = None
    try:
        response = requests.post(url, files={"file": stream.getvalue()})
        response = response.json()
    except:
        pass
    return response


def report(force=False):
    global last_report
    now = datetime.datetime.utcnow()
    if (now - last_report).total_seconds() <= 60 * 10 and not force:
        return
    last_report = now
    frame, stream = get_frame()
    url = f"http://{config.url}:8000/image/report"
    try:
        response = requests.post(url, files={"file": stream.getvalue()})
        logging.info(response.json())
    except:
        pass


def main():
    report(force=True)
    while True:
        results = detect()
        report()
        logging.info(results)
        logging.info("Going to Sleep")
        sleep(3)

if __name__ == '__main__':
    main()
