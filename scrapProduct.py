
from pandas.core.series import Series
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--incognito')
# chrome_options.add_argument('--headless')
# sites
link = 'https://shopee.com.my/search?keyword='
driver = webdriver.Chrome(options=chrome_options)



def main():
    # must add the keyword to search
    driver.get(link + 'keyboard')

    try:
        # to select the languagae
        # by default we select english
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='modal']/div[1]/div[1]/div/div[3]/div[1]/button"))).click()

    except TypeError:
        print('TypeError Exception Raised')

    else:
        print("Element Found ... success")

   


# def findProduct():
#     page_source = driver.page_source
#     # page_str =  1
#     feature ="html.parser"
#     product =  BeautifulSoup(page_source, feature)
    

#     # Find the product with price
#     for item in product.select('div[data-sqe="item"]'):
            
#             name=item.find('div',class_="_10Wbs- _5SSWfi UjjMrh").text
#             price=item.find('div',class_="zp9xm9 xSxKlK _1heB4J").text
            
#             print('Product Name :',name,'Price :',price)
            
            # return 
           
def getEmProduct():
    try:
    
        # get product
        xpathProduct = [  my_element.text for my_element in WebDriverWait(driver, 5).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='_10Wbs- _5SSWfi UjjMrh']")))]
        # get price
        xpathPrice = [ my_element.text for my_element in WebDriverWait(driver, 5).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='zp9xm9 xSxKlK _1heB4J']")))]
        print(xpathProduct, xpathPrice)

        # store file in csv
        df = pd.DataFrame.from_dict({"hai":xpathProduct})
        df.insert(1,"test1",xpathPrice)

        print(df)
        df.to_csv('file2.csv', index=False, header=False)


    except TypeError:
        print('TypeError Exception Raised')

    else:
        print("Title is found ... success")

main()
# findProduct()
getEmProduct()
print("Next")
driver.close()
