from selenium import webdriver
import browsercookie
import requests

cj = browsercookie.chrome()
# print(cj)
# driver = webdriver.Chrome() # You can replace this with other web drivers
# driver.add_cookie(cj)
response = requests.get("https://mail.google.com/mail/u/0/#inbox", cookies=cj)
# cookies = driver.get_cookies() # Here is your populated data.
# driver.quit() # don't forget to quit the driver!
print(response.text)
