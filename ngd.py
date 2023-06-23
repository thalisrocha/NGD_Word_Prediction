import numpy as np
import math
from nltk.tokenize import word_tokenize
from urllib.parse import quote_plus

from googleapiclient.discovery import build


def get_search_results_count(query):
    query = quote_plus(query)
    api_key = "AIzaSyCsuFrF6LOR0IF8nqpzsDWCp0F0sMBrZeU"
    cse_id = "7283c75e4d73e4937"
    
    service = build("customsearch", "v1", developerKey=api_key)
    result = service.cse().list(q=query, cx=cse_id).execute()

    
    if "searchInformation" in result:
        total_results = int(result["searchInformation"]["totalResults"])
        return total_results
    
    return 0

def ngd(w1, w2):
    # print('"'+w1+'"',get_search_results_count('"'+w1+'"'))
    f_w1 = math.log(get_search_results_count('"'+ w1 +'"'), 2)
    f_w2 = math.log(get_search_results_count(w2), 2)
    f_w1_w2 = math.log(get_search_results_count('"'+ w1 +" " + w2 +'"'), 2)
    N = 25270000000000

    return (max(f_w1, f_w2) - f_w1_w2) / (N - min(f_w1, f_w2))


def get_top_words_v1(input_phrase, predictions, num_words):
    ngd_scores = [(word, ngd(input_phrase, word)) for word in predictions]

    sorted_words = sorted(ngd_scores, key=lambda x: x[1])

    top_words = [word for word, _ in sorted_words[:num_words]]

    return top_words

def get_top_words_v2(input_phrase, predictions, num_words):
    input_tokens = word_tokenize(input_phrase)
    print(input_tokens)

    ngd_scores = []
    for word in predictions:
        ngd_scores.append((word, get_mean_ngd(input_tokens, word)))

    sorted_words = sorted(ngd_scores, key=lambda x: x[1])

    top_words = [word for word, _ in sorted_words[:num_words]]

    return top_words


def get_mean_ngd(tokens1, tokens2):
    total_ngd = 0.0
    count = 0

    for token1 in tokens1:
        total_ngd += ngd(token1, tokens2)
        count += 1

    mean_ngd = total_ngd / count

    return mean_ngd