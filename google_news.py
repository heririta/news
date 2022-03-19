from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd
import streamlit as st

googlenews = GoogleNews(start='01/01/2022', end='03/19/2022')
# googlenews.search('heri')
result = googlenews.result()
df = pd.DataFrame(result)


# for i in range(2, 20):
#     googlenews.getpage(i)
#     result = googlenews.result()
#     df = pd.DataFrame(result)

st.dataframe(df)
print(df)
