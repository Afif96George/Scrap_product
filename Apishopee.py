import requests
import pandas as pd
Shopee_url = 'https://shopee.com.my'
keyword_search = 'Longitech MK470'
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
prices_min  = []
prices_max = []
rating_star =  []
shop = []
# set what arrtibut wants to get 
for item in r['items']:
    titles_list.append(item['name'])
    prices_list.append(item['price']/100000)
    prices_min.append(item['price_min']/100000)
    prices_max.append(item['price_max']/100000)
    rating_star.append(item['item_rating']['rating_star'])
    shop.append(item['shop_location'])
Shopee = pd.DataFrame(zip(titles_list, (round(x,2) for x in prices_list),(round(x,2)for x in prices_min),(round(x,2)for x in prices_max),(round(x,2)for x in rating_star), shop),  columns=["ItemName", "Price(MYR)","Price Minimum(MYR)","Price Maximum(MYR)","Rating", "Shop Location"])

# print(Shopee)
# print(Shopee.dtypes)

# convert to csv 
Shopee.to_csv('./Shopee MK470.csv', encoding ='utf-8')