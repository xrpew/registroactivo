from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

@app.get('/')
def root():
   return 'usuario activo'

@app.get('/sergio')
def root():
   return 'sergio activo'

data = [
   {"name":'sergio',
    "edad":32},
    {"name":'gabriela',
    "edad":28}
]

@app.get("/user/")
def get_user(q: str):
    for da in data:
       if da['name']== q:
        return da
    return 'usuario no existe'
          