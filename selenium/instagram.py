import selenium.webdriver as webdriver

tag = 'your-tag-name'
url = 'https://www.instagram.com/explore/tags/' + tag
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('/Applications/chromedriver', options=options)

driver.implicitly_wait(5)
driver.get(url)
totalCount = driver.find_element_by_class_name('g47SY').text
print("totalCount :", totalCount)

driver.quit()