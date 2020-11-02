import get_equip
import json

data = get_equip.printEquip("202010121001616-10-GDRYQK15SC9H8", '10')
print data['detail']
print get_equip.printUserData(data)