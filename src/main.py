import uvicorn
from fastapi import FastAPI

from src.services.ScraperService import fetch_news

app = FastAPI()


@app.get('/')
async def root():
    return 'Hey there! Head to /news to find the latest news!'


@app.get('/news')
def scrape_worldnews():
    return fetch_news()


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
