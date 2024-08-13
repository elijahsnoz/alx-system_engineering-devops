#!/usr/bin/python3

"""
A function that queries the Reddit API
and returns the number of total subscribers for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers to a particular subreddit.
    If the subreddit is invalid, return 0.
    """

    if not subreddit or not isinstance(subreddit, str):
        return 0

    # Reddit API endpoint for subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Custom User-Agent to avoid 429 Too Many Requests error
    headers = {'User-Agent': 'MyRedditApp/0.1 by Forward-Age6992'}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        data = response.json().get('data')

        if data is None:
            return 0

        # Return the number of subscribers
        return data.get('subscribers', 0)

    except requests.RequestException:
        # Return 0 if any errors occur
        return 0
