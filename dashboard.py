# dashboard.py
import streamlit as st
from bitly_tracker import get_bitly_clicks
from tweet_engine import get_scheduled_tweets

st.set_page_config(page_title="ShillBill Control Panel", layout="centered")
st.title("🧠 ShillBillBot Dashboard")

# Display Bitly stats
st.header("📊 Bitly Click Stats")
clicks = get_bitly_clicks()
st.metric("Total Clicks", clicks)

# Show scheduled tweets
st.header("📅 Scheduled Tweets")
scheduled = get_scheduled_tweets()
for tweet in scheduled:
    st.text(tweet)

# 🔧 Streamlit port binding for Railway (add at bottom)
import os
port = int(os.environ.get("PORT", 8501))

st.write(f"Running on port {port}... (bound by Railway)")

st.experimental_set_query_params(dummy=port)  # Hack to prevent Streamlit timeout
