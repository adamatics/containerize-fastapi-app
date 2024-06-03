from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import List
from starlette.middleware.sessions import SessionMiddleware

# Define FastAPI App
app = FastAPI()

# Secret Key for session management
app.add_middleware(SessionMiddleware, secret_key='my-secret-key')

# Templates settings
templates = Jinja2Templates(directory="templates")

# Class for Tasks app
class Task(BaseModel):
    name: str
    status: bool

my_tasks: List[Task] = [Task(name="Start learning FastAPI!", status=True)]

# Define Pydantic Model for New Task Form
class NewTask(BaseModel):
    name: str


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/tasks", response_class=HTMLResponse)
async def get_tasks(request: Request):
    form = NewTask(name="")
    return templates.TemplateResponse("tasks.html", {"request": request, "my_tasks": my_tasks, "form": form})


@app.post("/tasks", response_class=HTMLResponse)
async def post_tasks(request: Request, name: str = Form(...)):
    new_task = Task(name=name, status=False)
    my_tasks.append(new_task)
    form = NewTask(name="")
    return templates.TemplateResponse("tasks.html", {"request": request, "my_tasks": my_tasks, "form": form})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
