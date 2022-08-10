import io
import os

from PIL import Image
from torchvision.transforms import transforms

import torch

IMAGE_PREPROCESS = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

torch.hub._validate_not_a_forked_repo = lambda a, b, c: True
MODEL = torch.hub.load('pytorch/vision:v0.9.0', os.getenv('ARCHITECTURE'))


def torch_transformation(img):
    image = Image.open(io.BytesIO(img))
    input_tensor = IMAGE_PREPROCESS(image)
    input_batch = input_tensor.unsqueeze(0)

    with torch.no_grad():
        output = MODEL(input_batch)

    result = torch.nn.functional.softmax(output[0], dim=0).tolist()
    return result.index(max(result))
