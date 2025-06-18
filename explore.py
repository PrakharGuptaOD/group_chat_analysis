def show_explore(df):
    import streamlit as st

    st.title("📬 Explore All Messages")

    search_term = st.text_input("🔍 Search for a specific message, word or user:")

    min_date = df["datetime"].min().date()
    max_date = df["datetime"].max().date()
    selected_dates = st.date_input("📅 Filter by Date Range", [min_date, max_date])

    filtered_df = df.copy()
    if isinstance(selected_dates, list) and len(selected_dates) == 2:
        start_date, end_date = selected_dates
        mask = (filtered_df["datetime"].dt.date >= start_date) & (filtered_df["datetime"].dt.date <= end_date)
        filtered_df = filtered_df[mask]

    if search_term:
        filtered_df = filtered_df[
            filtered_df["message"].str.contains(search_term, case=False, na=False) |
            filtered_df["user"].str.contains(search_term, case=False, na=False)
        ]

    st.dataframe(
        filtered_df[["datetime", "user", "message"]].sort_values(by="datetime", ascending=False),
        use_container_width=True,
        height=500
    )
