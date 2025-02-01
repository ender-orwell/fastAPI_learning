# Fast API

Here is a mini project to practice the use of fastAPI

## 1. Create a virtual env and activate it

python -m venv ./fastapi-env

./fastapi-env/Scripts/activate

## 2. Install the packages

pip install fastapi

And also our web server gateway interface server
pip install "uvicorn[standard]"

## 3. Create our main.py file

put here the testing endpoints

## 4. Start our server

uvicorn main:app --reload

## Remember
- Use deactivate to deactivate the environment
- The documentation generated automatically by fastAPI is in **/docs** or in **/redoc**