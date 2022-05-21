#!/usr/bin/python3
"""
Function that queries the Reddig API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """ Prints the titles of the top ten hot posts for a given subreddit """

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {'User-Agent': 'Mozilla/5.0'}

    r = requests.get(url, headers=header,
                     allow_redirects=False).json()

    try:
        list = r.get('data').get('children')
        for i in list:
            print(i.get('data').get('title'))
    except Exception:
        print(None)
