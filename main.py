from flask import Flask, render_template, Response, request, send_from_directory

import config
from camera import VideoCamera
import requests

pi_camera = VideoCamera(flip=False)
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html') #you can customze index.html here

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/picture')
def take_picture():
    pi_camera.take_picture()
    return "None"


@app.route('/detect')
def detect():
    frame = pi_camera.get_frame()
    url = f"http://{config.url}:8000/object-to-json"
    response = None
    try:
        response = requests.post(url, files={"file": frame})
        response = response.json()
        print(response)
    except:
        pass
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
