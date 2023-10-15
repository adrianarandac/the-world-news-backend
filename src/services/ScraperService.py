import requests
import json

from src.Constants import MAX_ARTICLES, REDDIT_URL


def fetch_news():
    try:
        response = requests.get(REDDIT_URL)
        site_json = json.loads(response.text)

        post_titles = [
            {'title': post['data']['title'], 'url': 'https://www.reddit.com' + post['data']['permalink']}
            for i, post in enumerate(site_json['data']['children'])
            if i <= MAX_ARTICLES and 'r/WorldNews Live Thread:' not in post['data']['title']
        ]
    except:
        post_titles = [
            {'title': "Sorry for the inconvenience, it seems Reddit is not available for scrapping right now.\n"
                      "Give it some time or click here to visit WorldNews subreddit!",
             'url': 'https://www.reddit.com/r/worldnews'}
        ]

    return {'post_titles': post_titles}
