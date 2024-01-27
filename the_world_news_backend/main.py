import uvicorn
from fastapi import FastAPI

from the_world_news_backend.services.NewsScraperService import fetch_news

app = FastAPI()


@app.get('/news')
def scrape_worldnews():
    return fetch_news()


def start():
    uvicorn.run("the_world_news_backend.main:app", host="0.0.0.0", port=8000, reload=True)
