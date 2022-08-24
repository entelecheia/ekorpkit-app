import requests
import base64
from io import BytesIO
from PIL import Image


class ServiceError(Exception):
    def __init__(self, status_code):
        self.status_code = status_code


def imagine_from_backend(
    backend_url, text_prompts, steps, skip_steps=10, n_samples=1, init_image=None
):
    url = backend_url + "/imagine"
    if init_image:
        init_image = image_to_bytearr(init_image)

    req = {
        "text_prompts": text_prompts,
        "steps": steps,
        "skip_steps": skip_steps,
        "n_samples": n_samples,
        "init_image": init_image,
    }
    r = requests.post(url, json=req)
    if r.status_code == 200:
        res = r.json()
        images = res.get("images")
        if images:
            res["images"] = [bytearr_to_image(img) for img in images]
        return res
    else:
        raise ServiceError(r.status_code)


def get_version(backend_url):
    url = backend_url + "/version"
    r = requests.get(url)
    if r.status_code == 200:
        version = r.json()["version"]
        return version
    else:
        raise ServiceError(r.status_code)


def bytearr_to_image(image):
    return Image.open(BytesIO(base64.b64decode(image)))


def image_to_bytearr(image: Image):
    img_bytearr = BytesIO()
    image.save(img_bytearr, format=image.format)
    img_bytearr = img_bytearr.getvalue()
    encoded = base64.b64encode(img_bytearr)
    decoded = encoded.decode("ascii")
    return decoded
