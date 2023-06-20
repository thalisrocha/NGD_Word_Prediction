import numpy as np
import requests
import math
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

from googleapiclient.discovery import build


def get_search_results_count(query):
    query = quote_plus(query)
    api_key = "AIzaSyDgwHlDitP3b8-mxfV6f5v8rt9TVq1_iZk"
    cse_id = "7283c75e4d73e4937"
    
    service = build("customsearch", "v1", developerKey=api_key)
    result = service.cse().list(q=query, cx=cse_id).execute()

    
    if "searchInformation" in result:
        total_results = int(result["searchInformation"]["totalResults"])
        return total_results
    
    return 0


# def get_search_results_count(query):
#     API_URL = "https://www.googleapis.com/customsearch/v1"
#     # Replace with your actual API key
#     API_KEY = "AIzaSyAUnck98rl4DsEV0SoHgrfZ76h5PXO2eBk"
#     CX = "7283c75e4d73e4937"  # Replace with your actual custom search engine ID
#     query = quote_plus(query)
#     print(query)
#     params = {
#         "q": query,
#         "key": API_KEY,
#         "cx": CX,
#         "fields": "searchInformation(totalResults)",
#     }

#     response = requests.get(API_URL, params=params)
#     data = response.json()
    
#     total_results = 0
#     print(data)
    
#     if "searchInformation" in data:
#         total_results = int(data["searchInformation"]["totalResults"])
#         return total_results

#     return 0

# def get_search_results_count(query):
#     query = quote_plus(query)
#     print(query)
#     search_url = f"https://www.google.com/search?q={query}"
#     print(search_url)
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
#     }

#     response = requests.get(search_url, headers=headers)
#     soup = BeautifulSoup(response.content, "html.parser")
#     result_stats = soup.find(id="result-stats")
#     print(result_stats)
#     if result_stats:
#         total_results_text = result_stats.get_text()
#         total_results = int("".join(filter(str.isdigit, total_results_text)))
#         return total_results

#     return 0

# def get_search_results_count(query):
#     query = quote_plus(query)
#     n_results = 0
    
#     # Setup Chrome options
#     chrome_options = Options()
#     chrome_options.add_argument("--headless") # Ensure GUI is off
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--disable-gpu")

#     # Set path to chromedriver as per your configuration
#     webdriver_service = Service(ChromeDriverManager().install())

#     # Choose Chrome Browser
#     driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

#     driver.get(f"https://www.google.com/search?q={query}")
    
#     # try:
#     result_stats = driver.find_element(By.ID, "result-stats").text
#     print(query,result_stats)
    
#     match = re.search(r"Environ ([\d\s\u202f]+)", result_stats)
#     print(match)
#     if match:
#         n_results = int(match.group(1).replace(" ", "").replace("\u202f", ""))
#         print("bizoia", n_results)
    
#     driver.quit()
        
#     return n_results
         
    # except:
    #     print("No results found")

    # driver.quit()    
    
    # return 0

def ngd(w1, w2):
    # print('"'+w1+'"',get_search_results_count('"'+w1+'"'))
    f_w1 = math.log(get_search_results_count(w1), 2)
    f_w2 = math.log(get_search_results_count(w2), 2)
    f_w1_w2 = math.log(get_search_results_count('"'+ w1 +" " + w2 +'"'), 2)
    N = 25270000000

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