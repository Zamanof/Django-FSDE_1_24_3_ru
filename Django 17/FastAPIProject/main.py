from fastapi import FastAPI, Query, Form, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import (
FileResponse,
HTMLResponse,
JSONResponse,
Response,
RedirectResponse
)
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class User(BaseModel):
    email: str
    password: str

@app.get("/")
async def root():
    # return {"message": "Hello World"}
    return FileResponse("static/index.html")


# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}

@app.get("/file", response_class=FileResponse)
async def root_html():
    return "static/index.html"


@app.get("/get-image")
async def get_image():
    return FileResponse("public/logo-teal.png", media_type="image/png")


@app.get("/download-image")
async def download_image():
    return FileResponse("public/logo-teal.png",
                        media_type="application/octet-stream",
                        filename="fast.png")


@app.get("/my-hello")
async def my_hello():
    html = "<h1 style='color:turquoise;'>Назаров Рамин Намиг</h1>"
    return HTMLResponse(html)


@app.get("/get-json")
async def get_json():
    data = {
        'name': "Илькин",
        'age': 24,
    }
    json_data = jsonable_encoder(data)
    return JSONResponse(json_data)


@app.get("/get-text")
async def get_text():
    html = "<h1 style='color:turquoise;'>Назаров Рамин Намиг</h1>"
    return Response(content=html, media_type="text/plain")

def as_user_from_form(
        email: str=Form(...),
        password: str=Form(...))->User:
    return User(email=email, password=password)

@app.post("/login")
async def login(user: User=Depends(as_user_from_form)):
    return {"message": f"{user.email} {user.password}"}




