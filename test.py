# -*- coding: utf-8 -*-
import requests
import json
import re
import array
import os
import get_equip
import time
import io
import cookie_login
#globals
minPrice = '1600'
maxPrice = '3000'
pass_fair_show=False
order_by_price=True
use_cache=True

cookie="_ntes_nnid=137aa30d87077e2edf1c82fa8398281e,1595674603386; _ntes_nuid=137aa30d87077e2edf1c82fa8398281e; fingerprint=8yeydgncqbuntcsl; _external_mark=reg.163.com; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26pass_fair_show%3D0%26price_min%3D300000%26price_max%3D300000; NTES_PASSPORT=c3OvMZBR6Txh.IpXQLxBazjRQYpu8kByVf_O1EWz3FpDNK67NXivTd6ogA0nhctcyDNqVEny31ZrorGI4dETvrGi.FREoySfrJptrAsYp1kW1PWOnYm1WytWilG6B5oK4cg9_oOnpoZ03L6psI2RT8nM8ALsHCwW02lN3af_nAxfvShxEzRXlnSUv; P_INFO=zcbnu@sina.com|1604839177|1|cbg|00&99|bej&1604675855&cbg#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=2ZonOCVFnO_93gGWsQFJwpWxcCx5g.m65S.dsOwCGLqzTPr9Tw.qDBrbG6EpgiziZZSziOL0qAvI.YqcXqnuYD4uzHMmBPaft6H5.cbM3tEHRu.D5OgvFkqrc118HwqUDvUmcLSpHES_j6qkWN1akcVHOFVlEw7k2Ue80hsaalvf1oP0noHV527D7yzZv9WDGS3T4IYfHW97B; S_INFO=1604942335|1|##|zcbnu@sina.com; ANTICSRF=b841ea602ba406b8364eadcb3ae5f705; sid=CKu2TDUg80FFzDdA45H6iEDSOeRujz9agPMryoZe; login_id=a5a939d7-22af-11eb-9e7a-727b640e8170"
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
		print data['pager']
		if index % 10 == 0:
			print "saving current page ", index 
			saveCache()

def doPrint(result, index, doSave):
	d = {}
	print result['expire_remain_seconds']
	ordersn = result['game_ordersn']
	if use_cache and ordersn in _cache and _hasSortKey(_cache[ordersn]):
		d['sort'] = _getSortVal(_cache[ordersn])
		d['game_ordersn'] = ordersn
		d['cache_mark'] = True
		d['serverid'] = _cache[ordersn]['serverid']
		d['expire_remain_seconds'] = result['expire_remain_seconds']
	else:
		print 'printEquip',ordersn,result['serverid']
		d = get_equip.printEquip(ordersn, result['serverid'])
		d['sort'] = _getSortVal(d)
		d['game_ordersn'] = ordersn
		if ordersn not in _cache: _cache[ordersn] = {}
		_cache[ordersn][_sortKey] = d['sort']
		_cache[ordersn]['statis'] = d['statis']
		_cache[ordersn]['serverid'] = result['serverid']
	# print(d['sort'])
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
		else: ret = ret[int(k)]
	return ret
def printRank(sortFunc=None, reverse=True):
	global _allData
	ret = {}
	if sortFunc != None:
		for data in _allData: 
			data['sort'] = sortFunc(data)
			print data['sort'], data['game_ordersn']
	ret = sorted(_allData, key=lambda v:int(v['sort']), reverse=reverse)
	print u'装备属性排行======'
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
			if index > 50: break
	_allData = ret

def sortFunc(data):
	ret = 0
	print data
	base = data.has_key('statis') and data['statis'] or data['sort']
	# if not data.has_key(u'statis') : return ret
	ret = base['speedSum3']
	# if base[u'speed'].has_key('2'): return base[u'speed']['2'] * 1000
	# if base[u'speed'].has_key(2) : return base[u'speed'][2] * 1000
	return ret
#load cache			
_cache={}
# _sortKey="statis.subValSpeical._3"
# _sortKey="statis"
# _sortKey="statis.speedSum3"
_sortKey="statis.subValEffect._4"
# _sortKey="statis.AssetVal"
# _sortKey="statis.subVal._"
if os.path.exists('cache.txt'):
	with open('cache.txt', 'r') as f:
		_cache=json.loads(f.read())

def saveCache():
	with open('cache.txt', 'w') as f:
		f.write(json.dumps(_cache))

getPageDetail(doPrint)
printRank()
saveCache()
# printRank(lambda v: v['expire_remain_seconds'], False)