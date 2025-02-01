from fastapi import FastAPI


app = FastAPI()


@app.get("/") # path, endpoint
def home_page():
    return {"message": "Hello World"}

@app.get("/items/{item_id}") # using a path parameter
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}