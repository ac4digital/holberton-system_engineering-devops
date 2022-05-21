#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Script that returns a list of all hot post titles
    for a given subreddit """

    try:
        r = requests.get('https://www.reddit.com/r/{}/hot.json'
                         .format(subreddit),
                         headers={'User-Agent': 'Mozilla/5.0'},
                         params={'after': after}).json()
    except Exception:
        return None

    if ("data" in r and "children" in r.get("data")):
        for i in r.get("data").get("children"):
            hot_list.append(i.get("data").get("title"))
        if "after" in r.get("data") and r.get("data").get("after"):
            return recurse(subreddit, hot_list,
                           r.get("data").get("after"))
        else:
            return hot_list
    else:
        return None
