from fastapi import FastApi
from pyexpat.errors import messages

from models import Developer, Project

app = FastAPI()

@app.post("/developers/")
def create_developer(developer: Developer):
    return {"messages":"Developer created successfully","developer":developer}

@app.post("/projects/")
def create_project(project:Project):
    return {"messages":"Proejct created successfully","project":project}