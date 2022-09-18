from app import db
from app.api.models import Message
from sqlalchemy import asc

def get_all_messages():
    messages = Message.query.order_by(asc(Message.date)).all()
    return messages

def add_message(text):
    message = Message(text=text)
    db.session.add(message)
    db.session.commit()
    message_json = {"id":message.id,
                    "text":message.text,
                    "date":f"{message.date.year}-{message.date.month}-{message.date.day}"}
    return message_json