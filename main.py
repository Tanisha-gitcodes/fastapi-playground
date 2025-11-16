from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

fake_items = [{"item1" : "Foo"}, {"item2" : "Bar"}, {"item3" : "Baz"}]

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "AlexNet model"}

    elif model_name == ModelName.resnet:
        return {"model_name": model_name, "message": "ResNet model"}

    return {"model_name": model_name, "message": "Have some residual"}

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items[skip : skip + limit]