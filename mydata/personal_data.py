from fastapi import  FastAPI

app = FastAPI()


DATA = [
    {
        "Nome":"Wilton Garcia",
        "Empresa":"ThoughtWorks",
        "Email":"wiltongarciaweb@gmail.com",
        "GitHub":"Wilton-Garcia"
    }
]

@app.get("/info")
def info():
    return DATA