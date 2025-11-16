from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "AlexNet model"}

    elif model_name == ModelName.resnet:
        return {"model_name": model_name, "message": "ResNet model"}

    return {"model_name": model_name, "message": "Have some residual"}
