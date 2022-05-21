#!/usr/bin/python3
"""
Write a function that requieres the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """ Script that returns the number of subscribers for a given subreddit """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=header, allow_redirects=False).json()
    try:
        subs = r.get("data", {}).get("subscribers", 0)
        return subs
    except ValueError:
        return 0
