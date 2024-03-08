# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

import os
import requests
from dotenv import load_dotenv

load_dotenv()

d_url = "http://localhost:3030"
sent_url = "http://localhost:5050/analyze/"
backend_url = os.getenv('backend_url', default=d_url)
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default=sent_url)


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        params = "&".join(f"{key}={value}" for key, value in kwargs.items())

    request_url = f"{backend_url}{endpoint}?{params}"

    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print(f"Network exception occurred: {e}")


def analyze_review_sentiments(text):
    request_url = f"{sentiment_analyzer_url}{text}"
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


def post_review(data_dict):
    request_url = f"{backend_url}/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as e:
        print(f"Network exception occurred: {e}")
