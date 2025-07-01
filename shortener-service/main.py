from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis
import string
import random

app = FastAPI()
redis_client = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)

def generate_short_id(num_chars=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=num_chars))

class URLItem(BaseModel):
    url: str

@app.get("/")
def read_root():
    return {"message": "URL Shortener API running!"}

@app.post("/shorten")
def shorten_url(item: URLItem):
    url = item.url
    short_id = generate_short_id()
    # Check if short_id already exists
    while redis_client.exists(short_id):
        short_id = generate_short_id()
    redis_client.set(short_id, url)
    return {"short_url": f"http://localhost:8000/{short_id}"}

@app.get("/{short_id}")
def redirect_url(short_id: str):
    url = redis_client.get(short_id)
    if url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"url": url}
