from fastapi import FastAPI

from the_world_news_backend.services.NewsScraperService import fetch_news

app = FastAPI()


@app.get('/news')
def scrape_worldnews():
    return fetch_news()
