from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# sites
link = 'https://shopee.com.my/search?keyword='
driver = webdriver.Chrome(options=chrome_options)


def main():
    # must add the keyword to search
    driver.get(link + 'vitamin')

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



main()
findPrice()
print("Next")
driver.exit()

# print("Program Ended")
