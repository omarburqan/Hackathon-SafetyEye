from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

data_json = {}
newPic = "false"
image = ""


@app.route('/', methods=["POST"])
def hello_world():
    data = request.get_json()
    global newPic
    global image
    global data_json
    try:
        image = data['image']
        data_json = data
        newPic = "true"
    except KeyError:
        pass
    print(data)

    return 'Hello, World!'


@app.route('/newPic')
def new_pic():
    global newPic
    global data_json
    print(newPic)
    temp = newPic
    if newPic == "true":
        newPic = "false"
        data_json = {}
    print(newPic)
    return temp


@app.route('/getImage')
def get_image():
    global data_json
    return jsonify(data_json)




