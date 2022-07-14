import datetime
from time import sleep
import requests

import config
from camera import VideoCamera

cam = VideoCamera()
last_report = datetime.datetime.utcnow()


def detect():
    frame = cam.get_frame()
    url = f"http://{config.url}:8000/model/inference_and_report"
    response = None
    try:
        response = requests.post(url, files={"file": frame})
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
    frame = cam.get_frame()
    url = f"http://{config.url}:8000/image/report"
    try:
        response = requests.post(url, files={"file": frame})
        print(response.json())
    except:
        pass


def main():
    report(force=True)
    while True:
        results = detect()
        report()
        print(results)
        sleep(5)


if __name__ == '__main__':
    main()
