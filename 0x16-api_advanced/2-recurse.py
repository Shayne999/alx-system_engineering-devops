#!/usr/bin/python3

""" queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""

import requests
import sys

def recurse(subreddit, hot_list=None, after=None, count=0):
    """ returns a list containing the titles of all hot articles """
    if hot_list is None:
        hot_list = []
    url = "http://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/shayne_ndlovu)"
    }
    params = {
            "after": after,
            "count": count,
            "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
    
