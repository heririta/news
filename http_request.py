import requests

query = "selenium"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
url = 'https://www.google.com?q=' + query
res = requests.get(url, headers=headers)
print(res)




