from selenium import webdriver

driver=webdriver.Chrome(r'C:\Users\Chaitanya Bonagiri\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
print(driver.capabilities)
print(driver.maximize_window())
print(driver.get_cookies())
print(driver.close)

#to find element by css selector
driver.find_element_by_css_selector("input[name='name']").send_keys("Rahul")
#driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_class_name("btn btn-success")
driver.find_element_by_id("Submit").click()
driver.close()

#customized css classses

# tagname=[attribute='value']-->Tagname optional
# Ex: [attribute*='value']
# input[name='name']
#
#
# #customized Xpath Synatax:
# //taganme[@attrribute=value] -->Tag anem optional
# EX:[contains{@attribute,'value'}]
#
#Generating CSS From ID
