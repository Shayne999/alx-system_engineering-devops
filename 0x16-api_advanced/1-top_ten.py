#!/usr/bin/python3
""" Queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests

def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""

    url = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if url.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in url.json().get("data").get("children")]
