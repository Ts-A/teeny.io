from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import random

app = FastAPI()

class TeenyModel(BaseModel):
    created_at: datetime
    updated_at: datetime
    teeny_id: str
    url: str
    visited_count: int
 
db: list[TeenyModel] = [
    {
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "teeny_id": "abc",
        "url": "https://fastapi.tiangolo.com/",
        "visited_count": 2
    },
    {
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "teeny_id": "def",
        "url": "https://excalidraw.com/",
        "visited_count": 1
    }
] 
    
acceptable_chars = ['abcdefghijklmnopqrstuvwxyz1234567890']
    
def generateCode():
    a = random.choices(acceptable_chars, k=6)
    print(a)
    return a
    
@app.get("/")
def read_root():
    return {"message": "hello world!"}

@app.post("/shorten")
def shorten(long_url: str):
    teeny_code: str = generateCode()
    return {
        "teeny_code": teeny_code,
        "url": long_url,
        "shortened_url": "http://localhost:3000/{teeny_code}",
        "createdAt": "2021-09-01T12:00:00Z",
        "updatedAt": "2021-09-01T12:00:00Z"
      }

@app.get("/shorten/{teeny_id}")
def shorten(teeny_id: str):
    try:
        for item in db:
            if teeny_id == item['teeny_id']:
                item['visited_count'] += 1
                return {
                        "created_at": item['created_at'],
                        "updated_at": item['updated_at'],
                        "teeny_id": item['teeny_id'],
                        "url": item['url'],
                        "visited_count": item['visited_count']
                    }
        raise Exception('Not found')  
    except:
        print("something went wrong")
        return {
            "message": "failed"
        }

@app.get("/shorten/{teeny_id}/stats")
def shorten(teeny_id: str):
    # TODO: logic to find shorten url stats
    url: str = ""
    count: int = 0
    return {
        "teeny_id": teeny_id,
        "url": url,
        "shortened_url": "/shorten/{teeny_id}",
        "createdAt": "2021-09-01T12:00:00Z",
        "updatedAt": "2021-09-01T12:00:00Z",
        "count": count
      }

@app.put("/shorten/{teeny_id}")
def shorten(teeny_id: str):
    # TODO: logic to update shorturl
    url: str = ""
    return {
        "teeny_id": teeny_id,
        "url": url,
        "shortCode": "/shorten/{teeny_id}",
        "createdAt": "2021-09-01T12:00:00Z",
        "updatedAt": "2021-09-01T12:00:00Z"
      }

@app.delete("/shorten/{teeny_id}")
def shorten(teeny_id: str):
    # TODO: logic to delete url
    url: str = ""
    return {
        "teeny_id": teeny_id,
        "url": url,
        "shortCode": "/shorten/{teeny_id}",
        "createdAt": "2021-09-01T12:00:00Z",
        "updatedAt": "2021-09-01T12:00:00Z"
      }
