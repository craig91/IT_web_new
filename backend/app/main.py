from fastapi import FastAPI
from sqlalchemy import create_engine, text
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "mysql+mysqlconnector://craig:password123@localhost/pydb"

engine = create_engine(DATABASE_URL)

@api.get("/emails")
def read_root():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT id, email FROM emails LIMIT 20"))
        emails = [{"id": row[0], "email": row[1]} for row in result]
    return {"emails": emails}