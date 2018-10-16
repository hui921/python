from selenium import webdriver
url = "http://www.naver.com/"

driver = webdriver.PhantomJS("C:/python_tt/python/phantomjs-2.1.1-windows/bin/phantomjs")
driver.implicitly_wait(3)
driver.get(url)
driver.save_screenshot("naver.png")
driver.quit()