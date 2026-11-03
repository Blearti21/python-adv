import os
import sqlite3
from email.policy import default
from http.client import responses
from pydoc import describe

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Header, HTTPException

from datebase import create_database, get_connection
from models.authors import AuthorCreate, AuthorResponse
from models.book import BookCreate,BookResponse

load_dotenv()
app = FastAPI(title="Simple Book mangament API")
create_database()

def check_key(x_api_key: str |None= Header(default=None)):
    key = os.getenv("API_KEY")
    if key and x_api_key != key:
        raise HTTPException(401,"Invalid api key")

@app.get("/")
def home():
    return {"message":"Book Managment API","dosc":/"dosc"}

@app.get("/authors", responses_model=list[AuthorResponse])
def list_authors():
    with get_connection() as conn:
        return [dict(row) for row in connn.execute("Select * FROM authors ORDER BY id")]



@app.put("/authors/{author_id}", responses_model=AuthorResponse,des)
