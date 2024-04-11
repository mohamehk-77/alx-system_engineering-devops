#!/usr/bin/python3
"""eturns a list containing the
titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Get all hot post titles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += "?after={}".format(after)
    headers = {'User-Agent': 'custom'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    hot_posts = data['data']['children']
    for post in hot_posts:
        hot_list.append(post['data']['title'])

    after = data['data']['after']
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
