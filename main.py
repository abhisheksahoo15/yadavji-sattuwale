from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount the static directory (for CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates directory
templates = Jinja2Templates(directory="templates")

# Home page
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# About page
@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# Products page
@app.get("/products")
def products(request: Request):
    return templates.TemplateResponse("products.html", {"request": request})

# Order Now page
@app.get("/order")
def ordernow(request: Request):
    return templates.TemplateResponse("ordernow.html", {"request": request})
