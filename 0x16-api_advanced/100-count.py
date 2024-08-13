#!/usr/bin/python3

"""
Recursive function to query Reddit API and count occurrences of specific keywords in hot post titles.
"""

from collections import defaultdict
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Queries Reddit API and counts occurrences of keywords in hot post titles.
    
    Args:
        subreddit (str): The subreddit to query.
        word_list (list): The list of keywords to count.
        after (str): The pagination token for the Reddit API.
        counts (dict): A dictionary to keep track of the count of each keyword.
    
    Returns:
        None
    """
    # Initialize the counts dictionary if it's the first call
    if counts is None:
        counts = defaultdict(int)
    
    # Normalize the word list to lowercase and handle duplicates
    normalized_word_list = [w.lower() for w in word_list]
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditApp/0.1 by Forward-Age6992'}
    params = {'limit': 25, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()

        data = response.json().get('data', {})
        posts_list = data.get('children', [])

        for post in posts_list:
            title = post['data']['title'].lower()
            title_words = title.split()

            for word in title_words:
                # Clean word of any punctuation
                word = word.strip('.,!?_"\'-:;')
                if word in normalized_word_list:
                    counts[word] += 1

        # Retrieve the after token for pagination
        after = data.get('after')

        # Recursively call the function if there's more data to fetch
        if after:
            return count_words(subreddit, word_list, after, counts)

        # If we are done with pagination, sort and print the results
        if counts:
            # Sort by count (descending) and alphabetically by word (ascending)
            sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

            for word, count in sorted_counts:
                print(f'{word}: {count}')

    except requests.exceptions.RequestException:
        return None
