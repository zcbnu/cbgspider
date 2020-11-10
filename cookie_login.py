# -*- coding: utf-8 -*-
import requests
import json
import re
import array
import os
import get_equip
import time
import io

def _parseCookie(cookies):
	ret = {}
	for line in cookies.split(';'):
		name,value = line.strip().split('=',1)
		ret[name] = value
	return ret

def login(url, user_name, password, refurl=""):
	session=requests.session()
	data={
		'username':user_name,
		'referered':refurl,
		'back_url':refurl
	}
	# cookie="_ntes_nnid=137aa30d87077e2edf1c82fa8398281e,1595674603386; _ntes_nuid=137aa30d87077e2edf1c82fa8398281e; fingerprint=8yeydgncqbuntcsl; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fuser%3F_mobile_tips%3D1; NTES_PASSPORT=asZ3CpuL88hgh1eZe4hWWbLzjgx0kLRR41UVQryXvlH5wsISwc4gjpIO296WbafaL5wGYrWLvQdmOmFPNprjgmF4ClxrOLu1mEHfm9AoHQMY0ILfkB8MAx4kZZ5QovaOJbMKCjpgCd0AutIVbTxuNDKwmgIOHMCLHhpKYhYUaUrtgubhrXxcqWu8g; P_INFO=zcbnu@sina.com|1604675855|1|cbg|00&99|bej&1604498871&cbg#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; sid=N76mGyJzV1iw-CSzWQ0oiTLaZSzWxpMXejziui7r; login_id=e7e69d54-2122-11eb-abee-77ad657ea100; is_log_active_stat=1; NTES_SESS=cv7G5wot3ABwTMA1YpjPRTqmQeB68vR.SJ9xyleKwVNDsHBnse9N0vB1wd8hX7D7RRJD7lVZNLzp9GNk5NYEG0SEDbP_vHMjTdb69k1PaT8bQE906lXziINBk..3beN20ihW.zaG9shuW_rG4wh4Prej4oDQhUlxMev6dAZI90WnjMw0KiPiJNfSvt0QVZuq4JasSpGjbonmv; S_INFO=1604802172|1|##|zcbnu@sina.com; ANTICSRF=9a4e1063fced23fbc1667e2d64ad0a03"
	cookie="_ntes_nnid=137aa30d87077e2edf1c82fa8398281e,1595674603386; _ntes_nuid=137aa30d87077e2edf1c82fa8398281e; fingerprint=8yeydgncqbuntcsl; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fuser%3F_mobile_tips%3D1; NTES_PASSPORT=asZ3CpuL88hgh1eZe4hWWbLzjgx0kLRR41UVQryXvlH5wsISwc4gjpIO296WbafaL5wGYrWLvQdmOmFPNprjgmF4ClxrOLu1mEHfm9AoHQMY0ILfkB8MAx4kZZ5QovaOJbMKCjpgCd0AutIVbTxuNDKwmgIOHMCLHhpKYhYUaUrtgubhrXxcqWu8g; P_INFO=zcbnu@sina.com|1604675855|1|cbg|00&99|bej&1604498871&cbg#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; sid=_Qlr0Bt9bVjHpylWwDcsA5idqNd_RAIZAHzMILtf; login_id=4e4eee47-2169-11eb-843f-487b964f6a45; is_log_active_stat=1; NTES_SESS=_evlkXj.sFRopahMCZKUzVRa0BnZFkq_gif0CWq1VsO3QkujQqfOaEupVDS6BG3GPPi3GWsMOT85fLOgvOA4LaF43IceEk2xRDIzfgpcURSIH4fazWB8YXOughhJIqOmaUdP1RMh9UOIBy_Tr_DAB34rPrKywuGCeQsuNjn8cqM5mBpmr3zlyLAaOfFfAHPEOiUQF5LxI9jwE; S_INFO=1604804934|1|##|zcbnu@sina.com; ANTICSRF=db97d61669ef71325bb06a1eccdaa9e7"
	source="{url}?username={username}&referered={refurl}&back_url={back_url}".format(
		url=url,
		username=user_name,
		refurl=refurl,
		back_url=refurl)
	response=session.get(source, cookies=_parseCookie(cookie))
	# cookie = requests.utils.dict_from_cookiejar(response.cookies)
	print response.text
	# response=session.get("https://recommd.yys.cbg.163.com/cgi-bin/recommend.py?callback=jQuery3310811396570582887_1604802173940&act=recommd_by_role&search_type=role&count=15&view_loc=search_cond&platform_type=2&pass_fair_show=0&price_min=300000&price_max=300000&order_by=&page=1&_=1604802173941")
	return session

def loginsession():
	
	url="https://yys.cbg.163.com/cgi/login"
	username="zcbnu@sina.com"
	password="@nOrange01"
	refurl="https://yys.cbg.163.com/cgi/mweb/pl/role?search_type=role&platform_type=2&pass_fair_show=0&price_min=300000&price_max=300000"
	return login(url,username,password,refurl)

def postlogin():
	data={
		'username':'zcbnu@sina.com',
		'product':'cbg',
		'persistCookie':'asZ3CpuL88hgh1eZe4hWWbLzjgx0kLRR41UVQryXvlH5wsISwc4gjpIO296WbafaL5wGYrWLvQdmOmFPNprjgmF4ClxrOLu1mEHfm9AoHQMY0ILfkB8MAx4kZZ5QovaOJbMKCjpgCd0AutIVbTxuNDKwmgIOHMCLHhpKYhYUaUrtgubhrXxcqWu8g',
		'userip':'1.91.86.78',
	}
	response=requests.post("https://reg.163.com/chgcookie.jsp",data)
	print response.text

# postlogin()