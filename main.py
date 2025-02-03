from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
import typing as t


app = FastAPI()


@app.get("/") # path, endpoint
def home_page():
    return {"message": "Hello World"}

@app.get("/items/{item_id}") # using a path parameter
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/me") # must be before users/user_id to avoid expected int error
async def read_user_me():
    return {"user_id": "The current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

class ModelName(str, Enum):
    ALEXNET = "ALEXNET"
    RESNET = "RESNET"
    LENET = "LENET"

@ app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.ALEXNET:
        return {"model_name": model_name}
    elif model_name.value == "LENET":
        return {"model_name": "Good choice: lenet"}
    else:
        return {"model_name": f"You have selected {model_name.value}"}

@ app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

dummy_db = [{"item_name":"t-shirt"}, {"item_name":"shoe"}, {"item_name":"watch"}]

@app.get("/items/") # use query parameters
async def read_item(skip: int=0, limit: int=10, optional_parameter: t.Optional[int]=None):
    # example: ?skip=2&limit=1&optional_parameter=53673
    return {"items": dummy_db[skip:skip+limit], "optional_parameter": optional_parameter}

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: int, q: t.Optional[str] = None, short: bool = False
):
# example: /users/89/items/33?q=Gian&short=True
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": 1}) # if there is an optional parameter
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

class Book(BaseModel):
    name: str
    author: str
    description: t.Optional[str] = None
    price: float

@app.post("/books/")
async def create_item(book: Book):
    # we can go test in the /docs and try out:
    # {
    #   "name": "Harry Potter",
    #   "author": "J K Rowling",
    #   "description": "The Chamber of Secrets",
    #   "price": 13
    # }
    return book