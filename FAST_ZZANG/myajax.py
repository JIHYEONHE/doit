from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def zzang(request: Request):
    return templates.TemplateResponse("zzang.html", {"request": request})

@app.get("/zzang2", response_class=HTMLResponse)
async def zzang2(request: Request):
    return templates.TemplateResponse("zzang2.html", {"request": request})

@app.get("/zzang3", response_class=HTMLResponse)
async def zzang3(request: Request):
    return templates.TemplateResponse("zzang3.html", {"request": request})

#uvicorn myajax:app --reload