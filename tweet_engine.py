# tweet_engine.py
import requests
import os

def get_scheduled_tweets():
    api_key = os.getenv("TYPEFULLY_API_KEY")
    username = os.getenv("TYPEFULLY_USERNAME")
    url = f"https://api.typefully.com/v0/users/{username}/queue"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        tweets = [item.get("text", "") for item in data.get("scheduled", [])]
        return tweets[:5]  # limit to 5 upcoming tweets
    else:
        return [f"Error: {response.status_code}"]
