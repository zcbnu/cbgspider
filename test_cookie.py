import requests
import browsercookie
cookie=browsercookie.chrome()
session=requests.session()
response = session.get("https://yys.cbg.163.com/cgi/mweb/pl/role?platform_type=2&view_loc=equip_list",cookies=cookie)
response=session.get("https://yys.cbg.163.com/cgi/mweb/pl/role?platform_type=2&view_loc=equip_list")
print(response.text)