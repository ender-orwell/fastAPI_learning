from fastapi import FastAPI


app = FastAPI()


@app.get("/") # path, endpoint
def home_page():
    return {"message": "Hello World"}