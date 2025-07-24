from sqlalchemy.orm import Session
from . import models
import string
import random

def generate_short_id(length: int = 6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_short_url(db: Session, target_url: str) -> models.URL:
    short_id = generate_short_id()
    
    # Ensure unique short ID
    while db.query(models.URL).filter_by(short_id=short_id).first():
        short_id = generate_short_id()

    db_url = models.URL(short_id=short_id, target_url=target_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url_by_short_id(db: Session, short_id: str) -> models.URL:
    return db.query(models.URL).filter_by(short_id=short_id).first()
