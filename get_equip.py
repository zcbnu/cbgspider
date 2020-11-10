# -*- coding: utf-8 -*-
import requests
import json
import re
import array
import string
# source="https://yys.cbg.163.com/cgi/api/get_equip_detail"
# data={'serverid':13, 'ordersn':'202001042101616-13-FCZS7JPBRUNRC', 'view_loc':'search_cond|tag_key:{"sort_key": "price", "tag": "user", "sort_order": "DESC"}'}
# # response=requests.get("https://yys.cbg.163.com/cgi/mweb/equip/13/202001042101616-13-FCZS7JPBRUNRC?view_loc=search_cond%7Ctag_key%3A%7B%22sort_key%22%3A%20%22price%22,%20%22tag%22%3A%20%22user%22,%20%22sort_order%22%3A%20%22DESC%22%7D&tag=user")
# response=requests.post(source, data)
# print(response.status_code)
# print(response.text)
# # matchObj=re.match('[^\()]*\((.*)\)$', response.text)
# jstr=response.text
# data=json.loads(jstr, encoding='utf-8')
# detail=json.loads(data['equip']['equip_desc'])
# equip=detail['inventory']

# print equip[u'5cad6024d31ce28854159943']
_allAttrNames = [u'critPowerAdditionVal', u'attackAdditionVal', u'speedAdditionVal', u'defenseAdditionVal', u'critRateAdditionVal', u'debuffEnhance', u'maxHpAdditionRate', u'attackAdditionRate', u'defenseAdditionRate', u'debuffResist', u'maxHpAdditionVal']
_mainAttrNames = [u'\u751f\u547d', u'\u66b4\u51fb\u4f24\u5bb3', u'\u66b4\u51fb', u'\u653b\u51fb', u'\u653b\u51fb\u52a0\u6210', u'\u751f\u547d\u52a0\u6210', u'\u9632\u5fa1', u'\u6548\u679c\u62b5\u6297', u'\u901f\u5ea6', u'\u6548\u679c\u547d\u4e2d', u'\u9632\u5fa1\u52a0\u6210']
_suits = {
	'300010':[u'招财', 'zhaocai'],
	'300030':[u'破势', 'poshi'],
	'300036':[u'针女', 'zhennv'],
	'300048':[u'狂骨', 'kuanggu'],
	'300052':[u'荒骷髅', 'huang'],
	'300077':[u'歌女', 'genv']
}
# _useless = []
_usableAttrList = {
	u'maxHpAdditionRate':10, 
	u'attackAdditionRate':10, 
	u'critPowerAdditionVal':15, 
	u'speedAdditionVal':15, 
	u'critRateAdditionVal':15, 
	u'debuffEnhance':15, 
	u'debuffResist':12
}
_uselessMainAttr = {
	'2':[u'防御加成'],
	'4':[u'防御加成'],
	'6':[u'防御加成']
}

_statis = {};

# calculate equip value 
def calEquipVal(data):
	if _checkMainAttr(data) == False:
		# _useless.append(data)
		return
	val = _calUsable(data)
	statistic(data, val, lambda : '_', lambda: val[1])
	val = _calEffective(data)
	statistic(data, val, lambda: '_4', lambda: val[1])
	statistic(data, val, lambda: val[2], lambda: val[1])
	val = _calSpecial(data)
	statistic(data, val, lambda: '_3', lambda: val[1])
	statistic(data, val, lambda: val[2], lambda: 1)
	val = _calSpeed(data)
	statistic(data, val, lambda: val[2], lambda: val[1], True)
	# val = _calSuit(data)
	# statistic(data, val, lambda: val[2], lambda: val[1], True)

def _checkMainAttr(data):
	if data[u'pos'] not in _uselessMainAttr : return True
	if data[u'attrs'][0][0] in _uselessMainAttr[data[u'pos']]: return False
	return True
def _getGoodMainBonus(data):
	key = data[u'attrs'][0][0]+str(data[u'pos'])
	if key in _goodMainAttr : return _goodMainAttr[key]
	return 1
def statistic(data, val, staticFunc, valFunc, maxMark=False):
	key = staticFunc()
	if val[0] not in _statis: _statis[val[0]] = {}
	if key not in _statis[val[0]]: _statis[val[0]][key] = valFunc()
	elif not maxMark: _statis[val[0]][key] += valFunc()
	else: _statis[val[0]][key] = max(_statis[val[0]][key], valFunc())

_effectives = [
	{'need':10,u'critRateAdditionVal':2},
	{'need':10,u'speedAdditionVal':2},
	{'need':16,u'attackAdditionRate':1, u'critPowerAdditionVal':2, u'speedAdditionVal':2, u'critRateAdditionVal':3},
	{'need':16,u'maxHpAdditionRate':1, u'debuffResist':2,u'debuffEnhance':2,u'speedAdditionVal':2}
]
_goodMainAttr = {
	u'速度2': 4,
	u'攻击加成2': 2,
	u'攻击加成4': 2,
	u'效果命中4': 2,
	u'效果抵抗4': 2,
	u'暴击伤害6': 3,
	u'暴击6': 2
}
_tabBonusList = [
	[u'speedAdditionVal',4,1000],
	[u'speedAdditionVal',4,300]
]
_specialBonus = [
	[u'speedAdditionVal', 4.5, 100, [u'速度2'], 500],
	[u'speedAdditionVal', 5, 200, [u'速度2'], 3000],
	[u'speedAdditionVal', 5.5, 500, [u'速度2'], 5000],
	[u'critRateAdditionVal', 4.5, 100, [u'攻击加成2',u'攻击加成4',u'暴击伤害6'], 200],
	[u'critRateAdditionVal', 5, 200, [u'攻击加成2',u'攻击加成4',u'暴击伤害6'], 400],
]
#计算一速
def _calSpeed(data):
	ret = 0
	key = data[u'attrs'][0][0]+str(data[u'pos'])
	if u'rattr' not in data: return ['speed', 0, data[u'pos']]
	tabs = {}
	for val in data[u'rattr']:
		if val[0] not in tabs: tabs[val[0]] = 0
		tabs[val[0]] += val[1]
	if u'speedAdditionVal' in tabs : ret = tabs[u'speedAdditionVal']
	if key != u'速度2' and data[u'pos'] == 2 : ret = 0
	return ['speed', ret * 3, data[u'pos']]

# 计算资源
def _calAsset(data):
	ret = 0
	ret += int(data['goyu'])
	ret += int(data['strength'] / 2)
	ret += int(data['money'] / 1000)
	return ['AssetVal', ret]
# 计算套装
_importantAttrs = [u'speedAdditionVal', u'critRateAdditionVal', u'critPowerAdditionVal']
def _calSuit(data):
	ret = 0
	name = ''
	if u'rattr' not in data: return ['subValSuit', 0, name]
	tabs = {}
	for val in data[u'rattr']:
		if val[0] not in tabs: tabs[val[0]] = 0
		tabs[val[0]] += val[1]
	mattr = data[u'attrs'][0][0]
	for attr in _importantAttrs:
		if attr not in tabs or tabs[attr] < 4: continue
		return ['subValSuit', int(tabs[attr] * 1000), '{}{}-{}'.format(attr, data[u'suitid'], data[u'pos'])]
	return ['subValSuit', 0, name]
# 只算高速度和高暴击
def _calSpecial(data):
	ret = 0
	name = ''
	if u'rattr' not in data: return ['subValSpeical', 0, name]
	tabs = {}
	for val in data[u'rattr']:
		if val[0] not in tabs: tabs[val[0]] = 0
		tabs[val[0]] += val[1]
	key = data[u'attrs'][0][0]+str(data[u'pos'])
	for special in _specialBonus:
		tmp = ret
		if special[0] in tabs and special[1] <= tabs[special[0]]:
			ret = special[2]
			name = special[0]
			if key in special[3]: ret += special[4]
		ret = max(tmp, ret)
	return ['subValSpeical', ret, name]
# 按速攻爆 速命生算
def _calEffective(data):
	ret = 0
	if u'rattr' not in data: return ['subValEffect', 0, "suit0"]
	for effective in _effectives:
		v = 0
		for val in data[u'rattr']:
			if val[0] in effective : v+=effective[val[0]]
		if v < effective['need'] : v = 0
		v *= _getGoodMainBonus(data)
		ret = max(ret, v)
	skey = str(data[u'suitid']) in _suits and _suits[str(data[u'suitid'])][1] or 'suit0'
	return ['subValEffect', ret, skey]
# 有用的副属性都算
def _calUsable(data):
	v = 0
	if u'rattr' not in data: return ['subVal', 0]
	for val in data[u'rattr']:
		if val[0] in _usableAttrList: v += _usableAttrList[val[0]]
	if v < 80 : v = 0
	return ['subVal',v]

def printEquip(ordersn, serverid):
	source="https://yys.cbg.163.com/cgi/api/get_equip_detail"
	data={'serverid':serverid, 'ordersn':ordersn, 'view_loc':'search_cond|tag_key:{"sort_key": "price", "tag": "user", "sort_order": "DESC"}'}
# response=requests.get("https://yys.cbg.163.com/cgi/mweb/equip/13/202001042101616-13-FCZS7JPBRUNRC?view_loc=search_cond%7Ctag_key%3A%7B%22sort_key%22%3A%20%22price%22,%20%22tag%22%3A%20%22user%22,%20%22sort_order%22%3A%20%22DESC%22%7D&tag=user")
	jstr=''
	# try:
	# 	with open(str("./detail/"+ordersn+".json"), "r") as f:
	# 		jstr=f.read()
	# except:
	# 	a=1		
	if jstr == '':
		jstr = requests.post(source, data).text
	# print(jstr)
# matchObj=re.match('[^\()]*\((.*)\)$', response.text)
	data=json.loads(jstr, encoding='utf-8')['equip']
	analyseEquipData(data)
	# with open('./detail/'+ordersn+str(serverid)+'.json', 'w') as f:
	# 	f.write(json.dumps(data))
	print ordersn,serverid	
	# printUserData(data)
	return data
# printEquip('202010242301616-34-YIIPLD50XSVGL', 34)
def analyseEquipData(data):
	_statis.clear()
	detail=json.loads(data['equip_desc'])
	equip=detail['inventory']
	data['detail'] = detail
	for _,val in equip.iteritems():
		calEquipVal(val)
	_statis['AssetVal'] = _calAsset(detail)[1]
	_statis['speedSum3'] = sum(_statis['speed'].values()) + 57
	_statis['speedSum-2'] = (sum(_statis['speed'].values()) + 57 -_statis['speed'][2])*100
	_statis['sumSuit'] = {}
	# for key, v in _statis['subValSuit'].iteritems():
	# 	if len(key) < 3 : continue
	# 	params = key.split('-')
	# 	if params[0] not in _statis['sumSuit'] : _statis['sumSuit'][params[0]] = 0
	# 	_statis['sumSuit'][params[0]] += v

	data['statis'] = _statis.copy()
def dumpUserData(data):
	detail=json.loads(data['equip_desc'])
	equip=detail['inventory']
	subval=''
	for t,val in data['statis'].iteritems():
		subval+='{}-{}\n\t'.format(t,json.dumps(val))
	gallery='ssr={}/{} sp={}/{}'.format(detail['hero_history']['ssr']['got'],detail['hero_history']['ssr']['all'],detail['hero_history']['sp']['got'],detail['hero_history']['sp']['all'])
	s=u'玩家:{name} 公示期结束:{fair_show_end_time} {desc_sumup_short} 收藏:{collect_num} ordersn:{ordersn}\n\t价格:{price}\t金币:{money} 体力:{strength} 勾玉:{goyu} 图鉴:{gallery}\n\t御魂得分:{subVal}\t总数:{num}'
	return s.format(name=detail['name'],fair_show_end_time=data['fair_show_end_time'],desc_sumup_short=data['desc_sumup_short'], ordersn=data['game_ordersn'],
		collect_num=data['collect_num'],price=data['price'],money=detail['money'],strength=detail['strength'],goyu=detail['goyu'],gallery=gallery,
		subVal=subval,num=len(equip))
def printUserData(data):
	detail=json.loads(data['equip_desc'])
	equip=detail['inventory']
	print u'玩家:',detail['name'],u' 公示期结束:',data['fair_show_end_time'], data['desc_sumup_short'],u'收藏',data['collect_num'],'ordersn',data['game_ordersn']
	tab='    '
	print tab,u'价格',data['price'] / 100.0,
	print tab,u'金币',detail['money'],u'体力',detail['strength'],u'勾玉',detail['goyu'], u'图鉴-ssr',detail['hero_history']['ssr']['got'],'/',detail['hero_history']['ssr']['all'],'sp',detail['hero_history']['sp']['got'],'/',detail['hero_history']['sp']['all']

	for t,val in data['statis'].iteritems():
		print tab,t,val
	print tab,u'御魂总数',len(equip),'======='
# print(matchObj.group(1))