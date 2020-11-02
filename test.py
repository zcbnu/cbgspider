# -*- coding: utf-8 -*-
import requests
import json
import re
import array
import os
import get_equip
import time
import io

#globals
minPrice = '1300'
maxPrice = '3000'
pass_fair_show=False
order_by_price=False
use_cache=True

def getPageData(page=1):
	now = int(time.time() * 1000)
	source="https://recommd.yys.cbg.163.com/cgi-bin/recommend.py?callback=jQuery331027196140331386687_1604131827758&act=recommd_by_role&search_type=role&count=15&view_loc=search_cond&platform_type=2&{order_by_price}%20DESC{pass_fair_show}&price_min={minPrice}00&price_max={maxPrice}00&page={page}&_={now}"
	source=source.format(minPrice=minPrice,maxPrice=maxPrice,now=now,page=page,
		pass_fair_show=pass_fair_show and '&pass_fair_show=0' or '',
		order_by_price=order_by_price and '&order_type=price' or ''
		)
	response=requests.get(source)
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
		doit = not data['paging']['is_last_page']

def doPrint(result, index, doSave):
	d = {}
	ordersn = result['game_ordersn']
	if use_cache and ordersn in _cache and _hasSortKey(_cache[ordersn]):
		d['sort'] = _getSortVal(_cache[ordersn])
		d['game_ordersn'] = ordersn
		d['cache_mark'] = True
		d['serverid'] = _cache[ordersn]['serverid']
	else:
		print 'printEquip',ordersn,result['serverid']
		d = get_equip.printEquip(ordersn, result['serverid'])
		d['sort'] = _getSortVal(d)
		d['game_ordersn'] = ordersn
		if ordersn not in _cache: _cache[ordersn] = {}
		_cache[ordersn][_sortKey] = d['sort']
		_cache[ordersn]['statis'] = d['statis']
		_cache[ordersn]['serverid'] = result['serverid']
	print(d['sort'])
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
def printRank():
	global _allData
	ret = sorted(_allData, key=lambda v:int(v['sort']), reverse=True)
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
#load cache			
_cache={}
_sortKey="statis.subValEffect._4"
# _sortKey="statis.AssetVal"
if os.path.exists('cache.txt'):
	with open('cache.txt', 'r') as f:
		_cache=json.loads(f.read())

def saveCache():
	with open('cache.txt', 'w') as f:
		f.write(json.dumps(_cache))

getPageDetail(doPrint)
printRank()
saveCache()