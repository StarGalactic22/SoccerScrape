from selenium import webdriver


driver = webdriver.Firefox()
driver.get("")


#Extract lists 

times = driver.find_elements_by_xpath('//div[@class="vidiline-time"]')
soccerinfo=driver.find_elements_by_xpath('//div[@class="vidiline-message"]')
num_page_times = len(times)
for i in range(num_page_times):
    print(times[i].text + ":" + soccerinfo[i].text)
    
driver.close()