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

LANGUAGES = [
    {
        "Linguagem":"CSharp",
        "Proeficiencia":"70%" 
    },
      {
        "Linguagem":"Java",
        "Proeficiencia":"60%" 
    },
      {
        "Linguagem":"Java Script",
        "Proeficiencia":"50%" 
    },
      {
        "Linguagem":"Python",
        "Proeficiencia":"35%" 
    },
]

@app.get("/info")
def info():
    return DATA

@app.get("/languages")
def languages():
    return LANGUAGES