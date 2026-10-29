from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

img_url = "https://img.magnific.com/free-photo/closeup-shot-beautiful-butterfly-with-interesting-textures-orange-petaled-flower_181624-7640.jpg?semt=ais_hybrid&w=740&q=80"

@app.get("/", response_class=HTMLResponse)
def home():
    return f"""
    <h1>Hello, Welcome To My Page!</h1>
    <img src="{img_url}" width="200" alt="Beautiful butterfly">
    """
@app.get("/contact")
def get_contact():
    return {
        "Message" : "This is Contact Page."
    }