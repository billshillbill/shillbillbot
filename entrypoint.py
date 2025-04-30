# entrypoint.py
import os
import streamlit.web.cli as stcli
import sys

sys.argv = ["streamlit", "run", "dashboard.py", "--server.port", os.getenv("PORT", "8501"), "--server.address", "0.0.0.0"]
sys.exit(stcli.main())
