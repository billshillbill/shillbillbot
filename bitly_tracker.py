# bitly_tracker.py
import requests
import os

def get_bitly_clicks():
    access_token = os.getenv("BITLY_API_KEY")
    bitlink = "bit.ly/ShillBill"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    params = {"unit": "day", "units": -1}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("total_clicks", 0)
    else:
        return f"Error: {response.status_code}"
