from fastapi import FastAPI
import uvicorn
from mylib.logistics import distance
from mylib.wiki import get_keywords
from pydantic import BaseModel

app = FastAPI()

class City(BaseModel):
    name: str

@app.get("/")
async def root():
    return {"message": "Hello niikun"}


@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """
    Add two numbers together
    """
    total = num1 + num2
    return {"total": total}


@app.get("/distance/{city1}/{city2}")
async def get_distance(city1: str, city2: str):
    """
    Get the distance between two cities
    """
    dist = distance(city1, city2)
    return {"distance": dist}


@app.get("/hours/{city1}/{city2}/{speed}")
async def get_hours(city1: str, city2: str, speed: int):
    """
    Get the hours to travel between two cities
    """
    dist = distance(city1, city2)
    hours = dist / speed
    return {"hours": hours}

@app.post("/keywords")
async def get_wiki_keywords(city: City):
    """
    Get the keywords of a wikipedia page
    """
    keywords = get_keywords(city.name)
    return {"keywords": keywords}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')