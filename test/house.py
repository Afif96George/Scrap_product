from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, Chrome
# declare driver

def main():
	driver = webdriver.Chrome(executable_path=r"C:/project/house_random/chromedriver.exe")
	# opts = ChromeOptions(executable_path=r"C:/project/house_random/test/chromedriver.exe")
	# opts.add_experimental_option("detach", True)
	# driver = Chrome(chrome_options=opts)
	driver.get("https://www.python.org")
	print(driver.title)
	search_bar = driver.find_element("q")
	search_bar.clear()
	search_bar.send_keys("getting started with python")
	search_bar.send_keys(Keys.RETURN)
	print(driver.current_url)
	# driver.close()

	# driver.close()

if __name__ == '__main__': 
	main()
