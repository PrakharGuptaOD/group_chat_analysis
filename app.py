import streamlit as st
from dashboard import show_dashboard
from explore import show_explore
import pandas as pd
import re
from datetime import datetime

st.set_page_config(layout="wide")

# Session state to store uploaded chat
if "chat_df" not in st.session_state:
    st.session_state.chat_df = None

# Navigation setup
st.sidebar.title("📁 Navigation")
if st.session_state.chat_df is not None:
    page = st.sidebar.radio("Go to", ["Dashboard", "Explore Messages"])
else:
    page = "Home"

# Home - File Upload
if page == "Home":
    st.title("💬 WhatsApp Chat Analyzer")
    st.subheader("Please upload your WhatsApp .txt chat file to begin.")
    uploaded_file = st.file_uploader("📁 Upload your chat file", type="txt")

    if uploaded_file is not None:
        data = uploaded_file.read().decode("utf-8")
        pattern = r"(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}) - ([^:]+): (.+)"
        messages = re.findall(pattern, data)

        df = pd.DataFrame(messages, columns=["date", "time", "user", "message"])
        df["datetime"] = pd.to_datetime(df["date"] + " " + df["time"], errors='coerce', dayfirst=True)
        df.dropna(subset=["datetime"], inplace=True)
        df["date"] = df["datetime"].dt.date
        df["hour"] = df["datetime"].dt.hour
        df["day"] = df["datetime"].dt.day_name()

        st.session_state.chat_df = df

        st.success("✅ Chat file uploaded and processed successfully!")

        st.markdown("### ➡️ Now choose what you want to explore:")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📊 Open Dashboard"):
                st.experimental_rerun()
        with col2:
            if st.button("📬 Explore Messages"):
                st.experimental_rerun()

# Dashboard Page
elif page == "Dashboard":
    show_dashboard(st.session_state.chat_df)

# Explore Page
elif page == "Explore Messages":
    show_explore(st.session_state.chat_df)
