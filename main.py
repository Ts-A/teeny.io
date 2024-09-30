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
    access_count: int
 
db: list[TeenyModel] = [
    {
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "teeny_id": "abc",
        "url": "https://fastapi.tiangolo.com/",
        "access_count": 2
    },
    {
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "teeny_id": "def",
        "url": "https://excalidraw.com/",
        "access_count": 1
    }
]

teeny_id_dict = {'abc': 'https://fastapi.tiangolo.com/', 'def': 'https://excalidraw.com/'}
long_url_dict = {'https://fastapi.tiangolo.com/': 'abc', 'https://excalidraw.com/': 'def'}
    
acceptable_chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    
def find_first(teeny_id: str):
    for item in db:
        if teeny_id == item['teeny_id']:
            return item
    return None

def find_first_and_remove(teeny_id: str):
    found_index = -1
    for index, item in enumerate(db):
        if teeny_id == item['teeny_id']:
            found_index = index
            break
    if found_index == -1:        
        return None
    teeny_id_dict.pop(teeny_id)
    long_url_dict.pop(db[found_index]['url'])
    return db.pop(found_index)

def find_first_and_update(teeny_id: str, long_url: str):
    found_index = -1
    for index, item in enumerate(db):
        if teeny_id == item['teeny_id']:
            found_index = index
            break
    if found_index == -1:        
        return None
    long_url_dict.pop(db[found_index]['url'])
    teeny_id_dict[teeny_id] = long_url
    long_url_dict[db[found_index]['url']] = teeny_id
    db[found_index]['url'] = long_url
    db[found_index]['access_count'] += 1
    return db[found_index]

def create(long_url: str):
    if long_url in long_url_dict.keys():
        for item in db:
            if long_url == item['url']:
                return item
    teeny_id = ""
    while teeny_id == "" or teeny_id in teeny_id_dict:
        teeny_id = ''.join(random.choices(acceptable_chars, k=6))
    item = {
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "teeny_id": teeny_id,
        "url": long_url,
        "access_count": 1
    }
    db.append(item)
    teeny_id_dict[teeny_id] = long_url
    long_url_dict[long_url] = teeny_id
    return item
    
@app.get("/")
def read_root():
    return {"message": "hello world!"}

@app.post("/shorten")
def shorten(long_url: str):
    try:
        item = create(long_url)
        if item == None:
            raise Exception('Not found')
        return {
                "teeny_id": item['teeny_id'],
                "url": item['url'],
            }
    except:
        print("something went wrong")
        return {
            "message": "unable to process the request",
        }
        
@app.get("/shorten/{teeny_id}")
def get_shorten(teeny_id: str):
    try:
        item = find_first(teeny_id)
        item['access_count'] += 1
        if item == None:
            raise Exception('Not found')
        return {
                "teeny_id": item['teeny_id'],
                "url": item['url'],
            }
    except:
        print("something went wrong")
        return {
            "message": "unable to process the request",
        }

@app.get("/shorten/{teeny_id}/stats")
def get_stats(teeny_id: str):
    try:
        item = find_first(teeny_id)
        if item == None:
            raise Exception("Something went wrong")
        return item
    except:
        print("something went wrong")
        return {
            "message": "unable to process the request",
        }

@app.put("/shorten/{teeny_id}")
def update_shorten(teeny_id: str, long_url: str):
    try:
        item = find_first_and_update(teeny_id, long_url)
        if item == None:
            raise Exception("Something went wrong")
        return item
    except:
        print("something went wrong")
        return {
            "message": "unable to process the request",
        }

@app.delete("/shorten/{teeny_id}")
def shorten(teeny_id: str):
    try:
        item = find_first_and_remove(teeny_id)
        if item == None:
            raise Exception("Something went wrong")
        return item
    except:
        print("something went wrong")
        return {
            "message": "unable to process the request",
        }
