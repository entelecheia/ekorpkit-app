import requests
import base64
from io import BytesIO
from PIL import Image


class ServiceError(Exception):
    def __init__(self, status_code):
        self.status_code = status_code


def imagine_from_backend(backend_url, text_prompts, steps):
    url = backend_url + "/imagine"
    req = {"prompt": text_prompts, "steps": steps}
    r = requests.post(url, json=req)
    if r.status_code == 200:
        res = r.json()
        images = res.get("images")
        if images:
            res["images"] = [
                Image.open(BytesIO(base64.b64decode(img))) for img in images
            ]
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
