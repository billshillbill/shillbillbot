# entrypoint.py
import os
import streamlit.web.cli as stcli
import sys

# 🔧 Tell Streamlit to run the dashboard file
sys.argv = [
    "streamlit",
    "run",
    "dashboard.py",
    "--server.port", os.getenv("PORT", "8501"),
    "--server.address", "0.0.0.0"
]

# ✅ Execute the command
sys.exit(stcli.main())
