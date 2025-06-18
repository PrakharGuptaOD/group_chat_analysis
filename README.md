# 📊 Group Chat Analyzer (WhatsApp Version)

A simple and interactive **Streamlit** web application that helps you analyze and explore your WhatsApp group chat data.

## 🔍 What It Does

This tool takes a **WhatsApp exported `.txt` chat file** and processes it to generate:

- 📈 **Message statistics** per user (like total messages, media, links shared)
- 📊 **Top users** by number of messages
- 🕒 **Activity timeline** (daily message trends)
- 🕰️ **Most active hours** and **days**
- 💬 **Most common words** and a beautiful **word cloud**
- 🔗 **Link sharing trends**
- 📬 **Message Explorer** with full search and date filtering

## ✅ Use Cases

### 👨‍🏫 For Teachers or Educators:
- Understand which students are **most active or least active** in discussions
- Identify the **best time to send announcements or assignments**
- Track **engagement levels** over time for feedback or improvement

### 🏢 For Corporate or Team Leads:
- Measure **team communication trends** during projects
- Detect periods of **high or low collaboration**
- Recognize **key contributors** or **quiet members**
- Share visual insights with the team for retrospectives

### 👥 For Community Managers:
- Track who is **most engaged** and **who needs nudging**
- Find the **ideal time window** for announcements or polls
- Spot common keywords used, helping with **topic curation**
- Monitor **link sharing patterns** to keep spam in check

### 🔍 Understand Individuals Better:
- Identify highly engaged vs passive users
- Spot signs of helpful behavior (e.g., link/media sharing)
- Analyze message patterns to know if a person is consistent or sporadic

## 📁 File Structure

```
.
├── app.py             # Main app with file upload and navigation
├── dashboard.py       # Dashboard visualizations and stats
├── explore.py         # Message explorer with search and filters
├── README.md          # You're reading it!
```

## 🚧 Limitations

- Currently supports only **WhatsApp** `.txt` format exports
- One group chat at a time
- Designed for **personal/group use**, not enterprise-scale data

## 🚀 How to Run

1. Install the required libraries:
   ```bash
   pip install streamlit pandas matplotlib seaborn wordcloud
   ```

2. Run the app:
   ```bash
   streamlit run app.py
   ```

3. Upload your WhatsApp chat `.txt` file and explore!

---

👨‍💻 Built by **Prakhar** with ❤️ to understand group conversations better.

> This is an educational project. Feel free to fork and extend for Telegram/Discord/Slack in the future!
