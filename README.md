# 🗞️ Twitter Personal Newspaper

This project creates a personalized newspaper from tweets using PySpark and NLP, focusing on big data processing and distributed systems.

## Features
- Spark-based real-time data pipeline
- NLP preprocessing (tokenization, stopwords)
- Topic modeling via LDA
- Sentiment-aware summaries
- Flask web app for interactive viewing
- Weekly email newsletter in HTML format

## Tech Stack
- PySpark
- Tweepy / Static JSON
- Flask
- HTML + CSS

## How to Run
1. Process data: `spark_pipeline/preprocess_and_lda.py`
2. Generate topic summaries: `assign_dominant_topic.py`
3. View on web: `cd webapp && python app.py`
4. Generate weekly newsletter: `newsletter/generate_email_newsletter.py`
