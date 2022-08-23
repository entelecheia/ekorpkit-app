import io
import uuid
import uvicorn
import base64
from PIL import Image
from pydantic import BaseModel
from fastapi import FastAPI, WebSocket
from fastapi.responses import Response
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
from ekorpkit import eKonf


app = FastAPI()
eKonf.setLogger()
disco_cfg = eKonf.compose("model/disco")
disco = eKonf.instantiate(disco_cfg)


@app.get("/")
def read_root():
    return {"message": "Welcome to the ekorpkit API"}


@app.get("/version")
def read_version():
    return {"version": eKonf.__version__}


@app.get("/config")
def read_config(config_group: str = "model/disco"):
    return eKonf.compose(config_group, return_as_dict=True)


@app.get("/env")
def read_env():
    return eKonf.env().dict()


class ImagineRequest(BaseModel):
    text_prompts: str = "Beautiful photorealistic rendering of Jeju Island."
    batch_name: str = str(uuid.uuid4())
    steps = 100
    display_rate = 10
    n_samples = 1


@app.post("/imagine")
async def imagine(req: ImagineRequest):
    req = req.dict()
    req["n_samples"] = 1
    response = disco.imagine(**req)
    image_filepaths = response.get("image_filepaths", [])
    if image_filepaths:
        response["images"] = [
            image_to_bytearr(Image.open(img_file)) for img_file in image_filepaths
        ]
    return response


@app.websocket("/imagine_stream")
async def imagine_websocket(websocket: WebSocket, req: ImagineRequest):
    await websocket.accept()
    while True:
        if req is not None:
            for sample in get_samples(req):
                await websocket.send_json(sample)


def get_samples(req: ImagineRequest):
    req = req.dict()
    for i, sample in enumerate(disco.imagine_generator(**req)):
        image = sample.get("image")
        if image is not None:
            print(i, sample)
            sample["image"] = image_to_bytearr(image)
        yield sample


def image_to_bytearr(image: Image):
    img_bytearr = io.BytesIO()
    image.save(img_bytearr, format=image.format)
    img_bytearr = img_bytearr.getvalue()
    encoded = base64.b64encode(img_bytearr)
    decoded = encoded.decode("ascii")
    return decoded


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
