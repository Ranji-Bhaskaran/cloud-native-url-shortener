from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app import models, crud
from app.database import Base, engine, SessionLocal


# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic input model
class URLItem(BaseModel):
    url: str

@app.get("/")
def read_root():
    return {"message": "URL Shortener API with PostgreSQL is running!"}

@app.post("/shorten")
def shorten_url(item: URLItem, db: Session = Depends(get_db)):
    new_url = crud.create_short_url(db, target_url=item.url)
    return {"short_url": f"http://localhost:8000/{new_url.short_id}"}

@app.get("/{short_id}")
def redirect_url(short_id: str, db: Session = Depends(get_db)):
    result = crud.get_url_by_short_id(db, short_id=short_id)
    if not result:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"url": result.target_url}
