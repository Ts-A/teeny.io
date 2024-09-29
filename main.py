from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "hello world!"}

@app.get("/ping")
def pong():
    return {"message": "pong"}

@app.post("/shorten")
def shorten(long_url: str):
    # TODO: logic to shorten url
    shortened_url: str = ""
    return {
        "teeny_id": "1",
        "url": long_url,
        "shortened_url": shortened_url,
        "createdAt": "2021-09-01T12:00:00Z",
        "updatedAt": "2021-09-01T12:00:00Z"
      }

@app.get("/shorten/{teeny_id}")
def shorten(teeny_id: str):
    # TODO: logic to find long url using id
    url: str = ""
    return {
        "teeny_id": teeny_id,
        "url": url,
        "shortened_url": "/shorten/{teeny_id}",
        "createdAt": "2021-09-01T12:00:00Z",
        "updatedAt": "2021-09-01T12:00:00Z"
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
        "teeny_id": "1",
        "url": url,
        "shortCode": "/shorten/{teeny_id}",
        "createdAt": "2021-09-01T12:00:00Z",
        "updatedAt": "2021-09-01T12:00:00Z"
      }
