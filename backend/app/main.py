import uuid
import uvicorn
import base64
from io import BytesIO
from PIL import Image
from pydantic import BaseModel
from fastapi import FastAPI, WebSocket
from fastapi.responses import Response
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
from ekorpkit import eKonf
from ekorpkit.tasks.multi import StableDiffusion


app = FastAPI()

ws = eKonf.set_workspace(
    workspace="/workspace",
    project="ekorpkit-app", 
    task="aiart", 
    log_level="INFO"
)
sd = StableDiffusion()


@app.get("/")
def read_root():
    return {"message": "Welcome to the ekorpkit API"}


@app.get("/version")
def read_version():
    return {"version": eKonf.__version__}


@app.get("/config")
def read_config(config_group: str = "task=stable.diffusion"):
    return eKonf.compose(config_group, return_as_dict=True)


@app.get("/envs")
def read_env():
    return ws.envs.dict()


@app.get("/secrets")
def read_env():
    return ws.secrets.dict()


class ImagineRequest(BaseModel):
    text_prompts: str = "Beautiful photorealistic rendering of Jeju Island."
    batch_name: str = str(uuid.uuid4())
    num_inference_steps = 100
    num_samples = 1
    init_image: str = None


@app.post("/imagine")
async def imagine(req: ImagineRequest):
    batch_name = str(uuid.uuid4())
    req.batch_name = batch_name
    req = req.dict()
    # init_image = req.get("init_image")
    # if init_image is not None:
    #     init_image = bytearr_to_image(init_image)
    #     init_image_path = sd.save_init_image(batch_name, init_image)
    #     print(f"init_image_path: {init_image_path}")
    #     req["init_image"] = init_image_path

    results = sd.generate(**req)
    image_filepaths = results.image_filepaths
    response = results.dict()
    if image_filepaths:
        response["images"] = [
            image_to_bytearr(Image.open(img_file)) for img_file in image_filepaths
        ]
    return response


def bytearr_to_image(image):
    return Image.open(BytesIO(base64.b64decode(image)))


def image_to_bytearr(image: Image):
    img_bytearr = BytesIO()
    image.save(img_bytearr, format=image.format)
    img_bytearr = img_bytearr.getvalue()
    encoded = base64.b64encode(img_bytearr)
    decoded = encoded.decode("ascii")
    return decoded


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
