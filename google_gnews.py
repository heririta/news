# https://github.com/johnbumgarner/newspaper3_usage_overview
# https://pypi.org/project/gnews/
import streamlit as st
from gnews import GNews
import json
from newspaper import Config
from newspaper import Article
from newspaper.utils import BeautifulSoup

google_news = GNews(language='id', country='ID', max_results=10,
                    exclude_websites=['google.com'])
indonesia_news = google_news.get_news('telkomsel')
# print(indonesia_news[0])

for news in indonesia_news:
    # print(news['title'])
    # st.write(f"Judul :{news['title']} \n link:{news['url']}\n\n")

    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'

    config = Config()
    config.browser_user_agent = USER_AGENT
    config.request_timeout = 10

    base_url = news['url']
    article = Article(base_url, config=config)
    article.download()
    article.parse()

    st.write(article.title)
    article_meta_data = article.meta_data

    article_summary = {value for (
        key, value) in article_meta_data.items() if key == 'description'}
    st.write(article_summary)
    st.write(base_url)
