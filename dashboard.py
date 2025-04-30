# dashboard.py
import streamlit as st
from bitly_tracker import get_bitly_clicks
from tweet_engine import get_scheduled_tweets

def show_dashboard():
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
# Call the dashboard render function
show_dashboard()
