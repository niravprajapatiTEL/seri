from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "Message" : "Hello , Wellcome To my Page."
    }
@app.get("/contact")
def get_contact():
    return {
        "Message" : "This is Contact Page."
    }