#!/usr/bin/python3
"""
Importing requests module
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)

    # Check if the request was successful
    if response.status_code != 200:
        return 0

    try:
        all_data = response.json()
        return all_data.get('data', {}).get('subscribers', 0)

    except (KeyError, ValueError):
        return 0
