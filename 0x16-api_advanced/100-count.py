#!/usr/bin/python3
"""
recursive function that queries the Reddit API, parses the
title of all hot articles, and prints a
sorted count of given keywords (case-insensitive, delimited by spaces
"""
from collections import Counter
import re
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """Count occurrences of words in hot post titles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"
    headers = {'User-Agent': 'custom'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    hot_posts = data['data']['children']
    for post in hot_posts:
        title = post['data']['title'].lower()
        hot_list.extend(re.findall(r'\b\w+\b', title))

    after = data['data']['after']
    if after is not None:
        return count_words(subreddit, word_list, hot_list, after)

    word_count = Counter(hot_list)
    sorted_words = sorted([(word, word_count[word]) for word in word_list
                           if word_count[word] > 0],
                          key=lambda x: (-x[1], x[0]))
    for word, count in sorted_words:
        print("{}: {}".format(word, count))
