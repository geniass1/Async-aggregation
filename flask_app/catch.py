from flask import Flask, request
from PIL import Image
from handle import torch_transformation
import io

app = Flask(__name__)


@app.route("/", methods=['POST'])
def image_catcher():
    file = request.files['img']
    img = Image.open(file.stream)
    with io.BytesIO() as buf:
        img.save(buf, 'jpeg')
        image_bytes = buf.getvalue()
    return torch_transformation(image_bytes)
