import numpy as np
import requests
import math
from bs4 import BeautifulSoup
from sklearn.model_selection import train_test_split


def get_search_results_count(query):
    API_URL = "https://www.googleapis.com/customsearch/v1"
    # Replace with your actual API key
    API_KEY = "AIzaSyA1X0vp6vdOMePQ2wWv7VKNGVjiD9mTqWY"
    CX = "5105aae66f0bd4140"  # Replace with your actual custom search engine ID
    params = {
        "q": query,
        "key": API_KEY,
        "cx": CX,
        "fields": "searchInformation(totalResults)",
    }

    response = requests.get(API_URL, params=params)
    data = response.json()

    if "searchInformation" in data:
        total_results = int(data["searchInformation"]["totalResults"])
        return total_results

    return 0

# Example usage
# search_query = "python programming"
# results_count = get_search_results_count(search_query)
# print(f"Number of results for '{search_query}': {results_count}")


def ngd(w1, w2):
    try:
        f_w1 = math.log(get_search_results_count(w1), 2)
        f_w2 = math.log(get_search_results_count(w2), 2)
        f_w1_w2 = math.log(get_search_results_count(w1+" "+w2), 2)
        N = 25270000000

        return (max(f_w1, f_w2) - f_w1_w2) / (N - min(f_w1, f_w2))
    except ZeroDivisionError:
        return float("inf")


def get_top_words(input_phrase, predictions, num_words):
    # Calculate NGD for each predicted word
    ngd_scores = [(word, ngd(input_phrase, word)) for word in predictions]

    # Sort the words based on their NGD scores in ascending order
    sorted_words = sorted(ngd_scores, key=lambda x: x[1])

    # Get the top 'num_words' words with the smallest NGD scores
    top_words = [word for word, _ in sorted_words[:num_words]]

    return top_words
