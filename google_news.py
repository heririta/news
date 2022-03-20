from doctest import DocFileCase
from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd
import streamlit as st

googlenews = GoogleNews(
    start='01/01/2022', end='03/19/2022', lang='en', region='id')
googlenews.search('JK:TLKM')
# result = googlenews.result()
# df = pd.DataFrame(result)


for i in range(2, 20):
    googlenews.getpage(i)
    result = googlenews.result()
    df = pd.DataFrame(result)

st.dataframe(df)
# print(df)


df.to_csv('google_news.csv', index=False)
