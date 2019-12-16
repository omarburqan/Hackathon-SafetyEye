from flask import Flask
from flask import request

app = Flask(__name__)

newPic = "false"
image = ""


@app.route('/', methods=["POST"])
def hello_world():
    data = request.get_json()
    global newPic
    global image
    try:
        image = data['image']
        newPic = "true"
    except KeyError:
        pass
    print(data)

    return 'Hello, World!'


@app.route('/newPic')
def new_pic():
    global newPic
    print(newPic)
    temp = newPic
    if newPic == "true":
        newPic = "false"
    print(newPic)
    return temp


@app.route('/getImage')
def get_image():
    global image
    return image
