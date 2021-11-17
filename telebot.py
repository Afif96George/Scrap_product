
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


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

   

# get price base on list 
def findPrice():
    xpathPrice = ['RM' + my_element.text for my_element in WebDriverWait(driver, 5).until(
    EC.visibility_of_all_elements_located((By.XPATH, "//span[text()='RM']//following::span[1]")))]
    print(xpathPrice)
# use Bs4 for better extracting the data 
def findProduct():
    page_source = driver.page_source
    product =  BeautifulSoup(page_source)
    # print(product)
    for item in product.select('div[data-sqe="item"]'):
        # dataImg=item.img
        name=item.find('div',class_="_10Wbs- _5SSWfi UjjMrh")
        price=item.find('div',class_="zp9xm9 xSxKlK _1heB4J")
        
    
        print({'Product Name':name,'Price':price})


main()
# findProduct()
try:
    
    xpathProduct = ['Product Name : ' + my_element.text for my_element in WebDriverWait(driver, 5).until(
    EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='_10Wbs- _5SSWfi UjjMrh']"),))]
    xpathPrice = ['RM' + my_element.text for my_element in WebDriverWait(driver, 5).until(
    EC.visibility_of_all_elements_located((By.XPATH, "//span[text()='RM']//following::span[1]")))]
    print(xpathProduct, xpathPrice)
    # print(span.text)

except TypeError:
        print('TypeError Exception Raised')

else:
        print("Title is found ... success")

print("Next")
driver.close()

# print("Program Ended")
