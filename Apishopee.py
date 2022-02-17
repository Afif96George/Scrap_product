import requests
import pandas as pd
Shopee_url = 'https://shopee.com.my'
keyword_search = 'Longitech Camera'
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
 "Referer": "{}search?keyword={}".format(Shopee_url, keyword_search)
}
url = "https://shopee.com.my/api/v2/search_items/?by=relevancy&keyword={}&limit=100&newest=0&order=desc&page_type=search".format(keyword_search)

# Shopee API request
r = requests.get(url, headers = headers).json()
# Shopee scraping script
titles_list = []
prices_list = []
currencyMY  =  []
for item in r['items']:
    titles_list.append(item['name'])
    prices_list.append(item['price_min'])
Shopee = pd.DataFrame(zip(titles_list, prices_list), columns=["ItemName", "Price"])

print(Shopee)