def show_dashboard(df):
    import streamlit as st
    import matplotlib.pyplot as plt
    import seaborn as sns
    from collections import Counter
    from wordcloud import WordCloud
    
    st.title("📊 WhatsApp Chat Dashboard")

    selected_user = st.sidebar.selectbox("Select User", ["All"] + sorted(df["user"].unique()))
    if selected_user != "All":
        df = df[df["user"] == selected_user]

    st.header("1. 📈 Basic Stats")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Messages", len(df))
    col2.metric("Total Words", df["message"].apply(lambda x: len(x.split())).sum())
    col3.metric("Media Shared", df["message"].str.contains("<Media omitted>").sum())
    col4.metric("Links Shared", df["message"].str.contains("http").sum())

    st.divider()

    st.header("2. 👤 User Stats")
    user_stats = df["user"].value_counts().head(10)
    fig1, ax1 = plt.subplots()
    sns.barplot(x=user_stats.values, y=user_stats.index, ax=ax1)
    st.pyplot(fig1)

    st.divider()

    st.header("3. 🕒 Activity Timeline")
    timeline = df.groupby("date").count()["message"]
    fig2, ax2 = plt.subplots()
    timeline.plot(ax=ax2)
    st.pyplot(fig2)

    st.divider()

    st.header("4. 🕰️ Active Hours")
    hour_dist = df["hour"].value_counts().sort_index()
    fig3, ax3 = plt.subplots()
    sns.barplot(x=hour_dist.index, y=hour_dist.values, ax=ax3)
    st.pyplot(fig3)

    st.divider()

    st.header("5. 📅 Active Days")
    day_dist = df["day"].value_counts()
    fig4, ax4 = plt.subplots()
    sns.barplot(x=day_dist.index, y=day_dist.values, ax=ax4)
    st.pyplot(fig4)

    st.divider()

    st.header("6. 💬 Most Common Words")
    stopwords = set("for a of the and to in is it you are on that this with i my".split())
    all_words = " ".join(df["message"])
    words = [word.lower() for word in re.findall(r"\b\w+\b", all_words) if word.lower() not in stopwords]
    word_counts = Counter(words).most_common(20)
    words_df = pd.DataFrame(word_counts, columns=["word", "count"])
    fig5, ax5 = plt.subplots()
    sns.barplot(data=words_df, x="count", y="word", ax=ax5)
    st.pyplot(fig5)

    st.divider()

    st.header("7. 🌈 Word Cloud")
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(words))
    fig6, ax6 = plt.subplots(figsize=(10, 5))
    ax6.imshow(wordcloud, interpolation="bilinear")
    ax6.axis("off")
    st.pyplot(fig6)

    st.divider()

    st.header("8. 🔗 Link Sharing Trends")
    df["has_link"] = df["message"].str.contains("http")
    link_timeline = df[df["has_link"]].groupby("date").count()["message"]
    fig7, ax7 = plt.subplots()
    link_timeline.plot(ax=ax7)
    st.pyplot(fig7)

