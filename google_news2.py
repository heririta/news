import http.client
conn = http.client.HTTPSConnection("google-news.p.rapidapi.com")
headers = {
    'x-rapidapi-host': "google-news.p.rapidapi.com",
    'x-rapidapi-key': "4640dfb997mshc3bf13ae2ca451fp1d5e18jsna65f68056f80"
    }
conn.request("GET", "/v1/search?country=US&lang=en&q=Elon%20Musk", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))