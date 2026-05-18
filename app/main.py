from fastapi import FastAPI

from app.database import engine, Base
from app.models import Task, Project, ProjectWork, Journal

app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Daily Journal API Running"}


# if __name__ == "__main__":
