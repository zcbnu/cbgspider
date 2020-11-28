# -*- coding: utf-8 -*-
import requests
import json
import re
import array
import os
import get_equip
import time
import io
# import cookie_login
# import browsercookie
#globals
minPrice = '1500'
maxPrice = '4000'
pass_fair_show=False
order_by_price=True
use_cache=True

# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fplatform_type%3D2%26view_loc%3Dequip_list; NTES_PASSPORT=yd.sxMsqWRa906nyfC0pRQOCq3XNyDiDvJC5EfznA04YpvFRpWZ9_iFDK2GaSymyXYpIkfaXAEw1D1Pldif_91PZ80efDXxJ1t4m12gM4EOkSyyVsH6QPhtAeWasEogRYHyy1orQ4r01XG2v11Rmz0PPQ.NrvhUWMJ4rm6U_Dcnr9xS7fneW6axT9; P_INFO=zcbnu@sina.com|1605947747|1|cbg|00&99|bej&1605322018&cbg#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; sid=higIuQPKDTRmrd03lqkgOf2PVXK0-wRCLI9oDiEU; login_id=381c84d1-2cb3-11eb-bd30-ab2b7bae71b0; is_log_active_stat=1; NTES_SESS=4dt2uituEt1GO9qhKlsD5TWmjmewsKsofyPgdt90.hje68YH69PjrGYa._V2iKeKvvyeKthBjpwUP1jS7jbL1rsLe3EoG8uk5_3mPSaEN5V3zLPrmtiwCJjYSMMq39jlrQRVMUfTEtbv1yhH.jQTHLRYQeH1vZE9jtPDnWvdnDJ7eD_8UAFkd_yrWxevwHRr.yN6sU1k3RHWG; S_INFO=1606058304|1|##|zcbnu@sina.com; ANTICSRF=c42bb0405b6d90c2bc7611e57e025ba4"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fplatform_type%3D2%26view_loc%3Dequip_list; NTES_PASSPORT=yd.sxMsqWRa906nyfC0pRQOCq3XNyDiDvJC5EfznA04YpvFRpWZ9_iFDK2GaSymyXYpIkfaXAEw1D1Pldif_91PZ80efDXxJ1t4m12gM4EOkSyyVsH6QPhtAeWasEogRYHyy1orQ4r01XG2v11Rmz0PPQ.NrvhUWMJ4rm6U_Dcnr9xS7fneW6axT9; P_INFO=zcbnu@sina.com|1605947747|1|cbg|00&99|bej&1605322018&cbg#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=ZFpcWCZrcsBBQ43szvoAcsNlZOkiSWiRGzl9wr2qU7_hGTk4G2l_fIkyU.5KH3h3AAzh3r7j_ipClJ_Rb_SXJfvXhstMITxoY.s1lRytdY5sLXlf1rHp8Q_kROO6s2_0f0..d5ro9n6oL1aRdHTjxZ7eVbOKb67oB1Na6UhiUwS5DCb5MmkDPj9GCbPtshS6xzdGvCJosu4aI; S_INFO=1606329085|1|##|zcbnu@sina.com; ANTICSRF=d5adbf1d0120b63713f549239bda40e1; sid=f6FiXoRjifiigmH8F2Dxy2_zYeRoiUap34BmfvHk; login_id=6d452dd9-2f4c-11eb-b4c9-f129057b287c"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fplatform_type%3D2%26view_loc%3Dequip_list; NTES_PASSPORT=yd.sxMsqWRa906nyfC0pRQOCq3XNyDiDvJC5EfznA04YpvFRpWZ9_iFDK2GaSymyXYpIkfaXAEw1D1Pldif_91PZ80efDXxJ1t4m12gM4EOkSyyVsH6QPhtAeWasEogRYHyy1orQ4r01XG2v11Rmz0PPQ.NrvhUWMJ4rm6U_Dcnr9xS7fneW6axT9; P_INFO=zcbnu@sina.com|1605947747|1|cbg|00&99|bej&1605322018&cbg#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=bSnI2WLlVfUxu_ZzYIe.X7.whi.NxPUQEMiLu8X4grvtNK67NXivTd6ogA0nhctcyyMtc8rsvex9i_v1fvmD_TaDtWCIdKQGqAWji1oCRq0WODiTj8hx2.v61FFZWXvHT3ptQp0UqeR8fgn7Z3zkl.ZqKudSWdXUKCEBn4YnBaU3AV2Pd64TnWe26UC2YfMnIMRNa9_GWJ7kd; S_INFO=1606404850|1|##|zcbnu@sina.com; ANTICSRF=62a0dfcf51c2c7f773f4a448c739d1cc; sid=YFEBFiFb1CyLC1-l_VmGS26eKAGibmT6X4UCj5Oy; login_id=d4d475d4-2ffc-11eb-ad76-4842d94a4758"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fplatform_type%3D2%26view_loc%3Dequip_list; NTES_PASSPORT=yd.sxMsqWRa906nyfC0pRQOCq3XNyDiDvJC5EfznA04YpvFRpWZ9_iFDK2GaSymyXYpIkfaXAEw1D1Pldif_91PZ80efDXxJ1t4m12gM4EOkSyyVsH6QPhtAeWasEogRYHyy1orQ4r01XG2v11Rmz0PPQ.NrvhUWMJ4rm6U_Dcnr9xS7fneW6axT9; P_INFO=zcbnu@sina.com|1605947747|1|cbg|00&99|bej&1605322018&cbg#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=AgQZF8U3kdB1cM5tjS02u8.5tRGP_efJ3hB42kZ_0aPWUGQvUZBPoCQe0l1NsdWdiihWdkaFP3KqBDPLyPzbDopbWwYtCGnEJlwOBLeY9J1w7bBoOksK6VPQLrr.wZPjoS9SLWDqr9YiLwgOf6zHUpxpb5wqjvPY2LSLw.ifQEFr5xR6ET8vUVD_hKEJBLxnVh9UpqDEwXvxC; S_INFO=1606496388|1|##|zcbnu@sina.com; ANTICSRF=0c556f040e4370cbf76b2dcfe1c0abb2; sid=bC7V5TdpOwEcxE5g2KQHemois2TQh3Yf-tC495EW; login_id=f539ddf3-30d1-11eb-931a-a56747cf50ed "
cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fplatform_type%3D2%26view_loc%3Dequip_list; NTES_PASSPORT=yd.sxMsqWRa906nyfC0pRQOCq3XNyDiDvJC5EfznA04YpvFRpWZ9_iFDK2GaSymyXYpIkfaXAEw1D1Pldif_91PZ80efDXxJ1t4m12gM4EOkSyyVsH6QPhtAeWasEogRYHyy1orQ4r01XG2v11Rmz0PPQ.NrvhUWMJ4rm6U_Dcnr9xS7fneW6axT9; P_INFO=zcbnu@sina.com|1605947747|1|cbg|00&99|bej&1605322018&cbg#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=t._hXK6ssMxIoLYT8UoNDKC5TnByEZHjp6uomgMeaUc.7LHE7Muc9bHqaWpOQD.DYY6.DgUncJ1yu3cTCc8I395I.VAZbLj4iWVKuTqAfipVGIu9KgQ1zscHTNNhVMcx9jzZ7FZH87AnjEs2Qap6YNtfJsGjoF00vccyiIvoaCQeqcTKNIfDPG2TBEWj6syDc6f75y34VBE0b; S_INFO=1606527860|1|##|zcbnu@sina.com; ANTICSRF=aa173cdb25f83a039cff001bdeabeb84; sid=157WrXs5lvkmsA3LmyCSr2OHris2-MlM5Q6hEaur; login_id=3c2d9368-311b-11eb-9eea-454b6a6d16f5"
# cookie=browsercookie.chrome()
def _parseCookie(cookies):
	ret = {}
	for line in cookies.split(';'):
		name,value = line.strip().split('=',1)
		ret[name] = value
	return ret

def getPageData(page=1):
	global isLogin
	now = int(time.time() * 1000)
	source="https://recommd.yys.cbg.163.com/cgi-bin/recommend.py?callback={jquery}&act=recommd_by_role&search_type=role&count=100&view_loc=search_cond&platform_type=2&{order_by_price}%20DESC{pass_fair_show}&price_min={minPrice}00&price_max={maxPrice}00&page={page}&_={now}"
	source=source.format(minPrice=minPrice,maxPrice=maxPrice,now=now,page=page,
		pass_fair_show=pass_fair_show and '&pass_fair_show=0' or '',
		order_by_price=order_by_price and '&order_type=price' or '',
		jquery='jQuery33103657342171597797_1604497946770'
		)
	# session=requests.session()
	# session=cookie_login.loginsession()
	# response=session.get(source)
	# response=requests.get(source, cookies=requests.utils.dict_from_cookiejar(cookie))
	# response=requests.get(source, cookies=cookie)
	response=requests.get(source, cookies=_parseCookie(cookie))
	# print(response.status_code)
	# print(response.text)
	matchObj=re.match('[^\()]*\((.*)\)$', response.text)
	data=json.loads(matchObj.group(1))
	return data	

global _allData
_allData = []

def getPageDetail(func):
	doit = True
	index = 1
	while doit:
		data = getPageData(index)
		doSave=True
		for v in data['result']:
			doPrint(v, index, doSave)
			doSave=False
		index += 1
		doit = data['pager']['total_pages'] != data['pager']['cur_page']
		# print data['pager']
		if index % 10 == 0:
			print("saving current page ", index)
			saveCache()

def doPrint(result, index, doSave):
	d = {}
	# print result['game_ordersn']
	ordersn = result['game_ordersn']
	if use_cache and ordersn in _cache and _hasSortKey(_cache[ordersn]):
		d['sort'] = _getSortVal(_cache[ordersn])
		d['game_ordersn'] = ordersn
		d['cache_mark'] = True
		d['serverid'] = _cache[ordersn]['serverid']
		d['expire_remain_seconds'] = result['expire_remain_seconds']
		# print _sortKey, _getSortVal(_cache[ordersn]), "from cache"
	else:
		print('printEquip',ordersn,result['serverid'])
		d = get_equip.printEquip(ordersn, result['serverid'])
		d['sort'] = 0
		if _hasSortKey(d):
			d['sort'] = _getSortVal(d)
		d['game_ordersn'] = ordersn
		if ordersn not in _cache: _cache[ordersn] = {}
		_cache[ordersn][_sortKey] = d['sort']
		_cache[ordersn]['statis'] = d['statis']
		_cache[ordersn]['serverid'] = result['serverid']
		print(d['sort'], "FromData")
	_allData.append(d)
	# if doSave and (index+1) % 10 == 0: 
		# printRank()
		# saveCache()

def _hasSortKey(data):
	if _sortKey in data: return True
	keys = _sortKey.split('.')
	ret = data
	for k in keys:
		if k not in ret : return False
		ret = ret[k]
	return True
# print(matchObj.group(1))
def _getSortVal(data):
	if _sortKey in data: return data[_sortKey]
	keys = _sortKey.split('.')
	ret = data
	for k in keys:
		if k in ret: ret = ret[k]
		else: return 0
		# else: ret = ret[int(k)]
	return ret
def printRank(sortFunc=None, reverse=True):
	global _allData
	ret = {}
	if sortFunc != None:
		for data in _allData: 
			data['sort'] = sortFunc(data)
			# print data['sort'], data['game_ordersn']
	ret = sorted(_allData, key=lambda v:int(v['sort']), reverse=reverse)
	rankList=[]
	print(u'装备属性排行======')
	with io.open(_sortKey+maxPrice+'rank.txt', 'w', encoding='utf-8') as f:
		index=1
		for i in ret:
			if 'cache_mark' in i:
				v = get_equip.printEquip(i['game_ordersn'], i['serverid'])
				v['sort'] = _getSortVal(v)
				v['game_ordersn'] = i['game_ordersn']
				ret[index-1] = v

			else:
				v = i
			get_equip.printUserData(v)
			f.write(u'\n第{}名======\n'.format(index))
			f.write(get_equip.dumpUserData(v))
			index+=1
			rankList.append(v)
			if index > 150: break
	_allData = ret
	return rankList
def sortFunc(data):
	ret = 0
	# print data
	base = data.has_key('statis') and data['statis'] or data['sort']
	# if not data.has_key(u'statis') : return ret
	# if not isinstance(base[u'speed'], dict): return 0
	# ret = int((sum(base[u'speed'].values()) - min(base[u'speed'].values())) * 100)
	# if base[u'speed'].has_key('2'): return base[u'speed']['2'] * 1000
	# if base[u'speed'].has_key(2) : return base[u'speed'][2] * 1000
	return base['suitSum']['speed']['zhaocai-speed']
	# return ret
#load cache			
_cache={}
# _sortKey="statis.subValSpeical._3"
# _sortKey="statis.subValSpeical.critRateAdditionVal"
# _sortKey="statis"
# _sortKey="statis.suitSum.crit.poshi-crit"
# _sortKey="statis.speedSum3"
# _sortKey="statis.speedSum-2"
_sortKey="statis.subValEffect._4"
# _sortKey="statis.AssetVal"
# _sortKey="statis.subVal._"
if os.path.exists('cache.txt'):
	with open('cache.txt', 'r') as f:
		_cache=json.loads(f.read())

def saveCache():
	with open('cache.txt', 'w') as f:
		f.write(json.dumps(_cache))
def sortAndPrint(rankList, sortKeys):
	for sortKey in sortKeys:
		print( u'排行榜：', sortKey)
		with io.open(sortKey+maxPrice+'rank.txt', 'w', encoding='utf-8') as f:
			ret = sorted(rankList, key=lambda i: findKey(i, sortKey), reverse=True)
			index = 1
			for l in ret:
				print( sortKey,u'排行','第{}名=========='.format(index))
				get_equip.printUserData(l)
				f.write(u'\n第{}名======\n'.format(index))
				f.write(get_equip.dumpUserData(l))
				index +=1
				if index >= 50: break;
getPageDetail(doPrint)
ranks = printRank()
saveCache()
def findKey(data, key):
	kl = key.split('.')
	ret = data
	for k in kl:
		if k in ret : ret = ret[k]
		elif k == 'max': ret = max(ret.values())
		elif k == 'delta': ret = sum(ret.values()) - min(ret.values()) 
		else: return 0
	if isinstance(ret, dict):
		return sum(ret.values())
	return ret 
sortAndPrint(ranks, [
	"statis.speed.2",
	"statis.speed.delta",
	"statis.speed.max",
	"statis.suitSum.crit.poshi-crit",
	"statis.suitSum.speed.zhaocai-speed",
	"statis.speedSum-2",
	"statis.speedSum3",
	"statis.subValSpeical.critRateAdditionVal",
	"statis.AssetVal",
	"detail.pvp_score",
	"statis.equipnum",
	'collect_num',
	'statis.suitSum.crit',
	'statis.suitSum.criDmg',
	'statis.suitSum.speed',
])
# print _cache["202010211701616-3-WSXGZM6LMLBZDI"], _hasSortKey(_cache["202010211701616-3-WSXGZM6LMLBZDI"])
# printRank(lambda v: v['expire_remain_seconds'], False)