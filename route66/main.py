from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json

from get_services import get_services

app = FastAPI()

# Mount the "static" directory to serve static files (e.g., images)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/services")
async def services():
    return get_services()


@app.get("/")
async def main():
    return HTMLResponse(open("static/index.html").read())
