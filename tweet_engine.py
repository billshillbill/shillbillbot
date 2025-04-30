# tweet_engine.py
import requests

def get_scheduled_tweets():
    api_key = "41xgmI4i7FCJaXDa"  # Typefully API key
    username = "BillShillBill"    # Your Typefully username

    url = f"https://api.typefully.com/v0/users/{username}/tweets"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            tweets = [item.get("text", "") for item in data.get("tweets", [])]
            return tweets[:5] if tweets else ["(No scheduled tweets found.)"]
        elif response.status_code == 404:
            return ["(No tweets scheduled or endpoint returned 404)"]
        else:
            return [f"Error: {response.status_code}"]
    except Exception as e:
        return [f"Exception: {str(e)}"]
