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

# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=FubIs07IDP9PtsWdutjgR7F8wk1euvcbEKkB0RjMfdtNDJLIDjktuVL2fry_G.N.88KN.RdEt6qmkhtiwtpshuCsNUSnVJ4XzrUeki2SlzyU3skueRGq17tLiccOUjtout5c9peuEQ4xQO0Egu.aPPinao9edx.s_HWxsy_ZvbY.ZU0bY.4HPiSlNrEM_EBy3KlDCmhXUHI9V; S_INFO=1605835815|1|##|zcbnu@sina.com; ANTICSRF=be2c608d6978058ccbe20846aaa2e824; sid=XNbirR7ueOYfmV0Nv_xRytzVyWbpvEfglUY7aBHR; login_id=f196df23-2acf-11eb-a3be-ab6922e61ba2"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=nZEAbp0eim4etJacdHD1DBW3hTINWzt921guaPx2dDZO3iTX3xgZlsTmdNCeLhOhSS1OhPD4Zzywg6ZYVZ5Q6lbQO7FjsioB8N7qgYmFW8C7JQglqPLypGZTY__K7xZ9lWjedzuMkb2QcP0w3L8yp9C5V5mWcqMnR4CjZwwFMQ0fXyeIEQTgBPdvf4DsC2JZ01W3bw6B7kXfs; S_INFO=1605886498|1|##|zcbnu@sina.com; ANTICSRF=b4485064f0d69894f3570a18629c01a3; sid=fLdpSQ121-zRLfqewDXDhraxa85VWiM-Fo0vdQSz; login_id=f2b8c002-2b45-11eb-8dd3-096d418ec7ae"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=ba.DoZJkZWfl8Vyw54QDemjDdVjZhwjOHMiLu8X4grvtNK67NXivTd6ogA0nhctcyyMtc8rsvex9i_v1fvmD_TaDtWCIdKQGqAWji1oCRq0WODiTj8hx2.v61FFZWXvHT0wNpsS2SmH3OPDYg3BEaYltkbSXqQ8Mffmh8CgYxYNHhYt8sDay7hVadVTOrszB3MRNa9_GWJ7kd; S_INFO=1605893491|1|##|zcbnu@sina.com; ANTICSRF=bbf07327768c555abab3b3b94dac8f05; sid=Q2PkhYVi3_zyPidkBp3KofOTZK8yTVX0gi3v8Ybh; login_id=3af7ce21-2b56-11eb-977d-314eefde9d49"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; ANTICSRF=b2365cd6e15e37334b876b1d8772285e; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fplatform_type%3D2%26view_loc%3Dequip_list; is_log_active_stat=1; NTES_SESS=h0EzRaoLxOdradnU_IZT9KRxN9_Qg7XxFunazoKeuxHD490e4zw3CZ0YvsPLxXQXWQHTjTyJLzZvwB3ft3rMBCcMQn.6Z91qlttwAlLUeu9E0tja8mLotDyxfHFYo8pYJqe_s60GnsQP_yjdt7wLX1Hl9kMW4RE9SW5brU7gnqrKrz4ztzqN2SstSTaxJKbAS30jjcrfz5OYZ; NTES_PASSPORT=yd.sxMsqWRa906nyfC0pRQOCq3XNyDiDvJC5EfznA04YpvFRpWZ9_iFDK2GaSymyXYpIkfaXAEw1D1Pldif_91PZ80efDXxJ1t4m12gM4EOkSyyVsH6QPhtAeWasEogRYHyy1orQ4r01XG2v11Rmz0PPQ.NrvhUWMJ4rm6U_Dcnr9xS7fneW6axT9; S_INFO=1605947747|0|##|zcbnu@sina.com; P_INFO=zcbnu@sina.com|1605947747|1|cbg|00&99|bej&1605322018&cbg#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; sid=BkP8IHoQrfS6SiX2PNujdM5eKVPT1-C6MLQ8_Pmh; login_id=8d9fa5d7-2bd4-11eb-84f8-06c6902c7fca"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fplatform_type%3D2%26view_loc%3Dequip_list; NTES_PASSPORT=yd.sxMsqWRa906nyfC0pRQOCq3XNyDiDvJC5EfznA04YpvFRpWZ9_iFDK2GaSymyXYpIkfaXAEw1D1Pldif_91PZ80efDXxJ1t4m12gM4EOkSyyVsH6QPhtAeWasEogRYHyy1orQ4r01XG2v11Rmz0PPQ.NrvhUWMJ4rm6U_Dcnr9xS7fneW6axT9; P_INFO=zcbnu@sina.com|1605947747|1|cbg|00&99|bej&1605322018&cbg#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=.Ps4aynbNBHSjj2xksXlMD5eC8NYjxb7cHmq8a6J5vDsEox_E6mDytxi5VRGjIsIllHsIavODBTYmXD9ADgZXyPZsFWhtoKeuVFLm9iWCuRF4ZmyLajTknDx977QF6D1yjV5tKRnFjyVAxcocKKjWB5CxW9u5twgV0tvXi90qOMZCxzPQGE0Y0lEYAfWFsgQKHCEPYXeF2_pt; S_INFO=1605971693|1|##|zcbnu@sina.com; ANTICSRF=363715f93ce23a0b6a012af4f6272d8b; sid=g1cG3_ftW8E5bueV_Aj7Fk9om4FbqLAOMOhTtdUa; login_id=4ea2efae-2c0c-11eb-9e02-83e059ff91fd"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fplatform_type%3D2%26view_loc%3Dequip_list; NTES_PASSPORT=yd.sxMsqWRa906nyfC0pRQOCq3XNyDiDvJC5EfznA04YpvFRpWZ9_iFDK2GaSymyXYpIkfaXAEw1D1Pldif_91PZ80efDXxJ1t4m12gM4EOkSyyVsH6QPhtAeWasEogRYHyy1orQ4r01XG2v11Rmz0PPQ.NrvhUWMJ4rm6U_Dcnr9xS7fneW6axT9; P_INFO=zcbnu@sina.com|1605947747|1|cbg|00&99|bej&1605322018&cbg#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=dX5fhFPa1d5g7nqVo7akAL1KvEkMV5Qz9XqKim3G8SUbFjMNF3qU1PML8CksZvbv99XbvmS.U4HTqEUxRUucE1gcbAfDPjhOoCAQqxLfpokAncq1QmZHBtUMxVVIA3U612qHNgaZ_dlWkHSiQX_bNDhNkjS4b3fZL.jz34d7Zo_oJ9pzgtxYuImGXHOoqxzhtXpFgTEOAeNzP; S_INFO=1606043381|1|##|zcbnu@sina.com; ANTICSRF=866eb58bafea8df44130ba2f3250d1e0; sid=higIuQPKDTRmrd03lqkgOf2PVXK0-wRCLI9oDiEU; login_id=381c84d1-2cb3-11eb-bd30-ab2b7bae71b0"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fplatform_type%3D2%26view_loc%3Dequip_list; NTES_PASSPORT=yd.sxMsqWRa906nyfC0pRQOCq3XNyDiDvJC5EfznA04YpvFRpWZ9_iFDK2GaSymyXYpIkfaXAEw1D1Pldif_91PZ80efDXxJ1t4m12gM4EOkSyyVsH6QPhtAeWasEogRYHyy1orQ4r01XG2v11Rmz0PPQ.NrvhUWMJ4rm6U_Dcnr9xS7fneW6axT9; P_INFO=zcbnu@sina.com|1605947747|1|cbg|00&99|bej&1605322018&cbg#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; sid=higIuQPKDTRmrd03lqkgOf2PVXK0-wRCLI9oDiEU; login_id=381c84d1-2cb3-11eb-bd30-ab2b7bae71b0; is_log_active_stat=1; NTES_SESS=4dt2uituEt1GO9qhKlsD5TWmjmewsKsofyPgdt90.hje68YH69PjrGYa._V2iKeKvvyeKthBjpwUP1jS7jbL1rsLe3EoG8uk5_3mPSaEN5V3zLPrmtiwCJjYSMMq39jlrQRVMUfTEtbv1yhH.jQTHLRYQeH1vZE9jtPDnWvdnDJ7eD_8UAFkd_yrWxevwHRr.yN6sU1k3RHWG; S_INFO=1606058304|1|##|zcbnu@sina.com; ANTICSRF=c42bb0405b6d90c2bc7611e57e025ba4"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fplatform_type%3D2%26view_loc%3Dequip_list; NTES_PASSPORT=yd.sxMsqWRa906nyfC0pRQOCq3XNyDiDvJC5EfznA04YpvFRpWZ9_iFDK2GaSymyXYpIkfaXAEw1D1Pldif_91PZ80efDXxJ1t4m12gM4EOkSyyVsH6QPhtAeWasEogRYHyy1orQ4r01XG2v11Rmz0PPQ.NrvhUWMJ4rm6U_Dcnr9xS7fneW6axT9; P_INFO=zcbnu@sina.com|1605947747|1|cbg|00&99|bej&1605322018&cbg#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=4dt2uituEt1GO9qhKlsD5TWmjmewsKsofyPgdt90.hje68YH69PjrGYa._V2iKeKvvyeKthBjpwUP1jS7jbL1rsLe3EoG8uk5_3mPSaEN5V3zLPrmtiwCJjYSMMq39jlrQRVMUfTEtbv1yhH.jQTHLRYQeH1vZE9jtPDnWvdnDJ7eD_8UAFkd_yrWxevwHRr.yN6sU1k3RHWG; S_INFO=1606058304|1|##|zcbnu@sina.com; ANTICSRF=c42bb0405b6d90c2bc7611e57e025ba4; sid=pN7RREm3UOz_Ym9iJMCZPFvSX8SyB1OHhVchdt2S; login_id=f7356cc0-2cd5-11eb-86a2-df7383d29b9f"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fplatform_type%3D2%26view_loc%3Dequip_list; NTES_PASSPORT=yd.sxMsqWRa906nyfC0pRQOCq3XNyDiDvJC5EfznA04YpvFRpWZ9_iFDK2GaSymyXYpIkfaXAEw1D1Pldif_91PZ80efDXxJ1t4m12gM4EOkSyyVsH6QPhtAeWasEogRYHyy1orQ4r01XG2v11Rmz0PPQ.NrvhUWMJ4rm6U_Dcnr9xS7fneW6axT9; P_INFO=zcbnu@sina.com|1605947747|1|cbg|00&99|bej&1605322018&cbg#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=Clz75MOPZD27RTNtqNMiopMDI3UpnhtpxZJGBzIEkg5ArOhUrIJ5Lfh4kYxF.PAPqqZAPzgV5_joJc5K952dcL0dAlybfOs7eYlnJK4yTexlNdJLnz.jMW5hKSStlI5QLydgSR19BOvrZcys1oxyaAMXWSrz06S0x28yT1n8BosjJdJLgdQFwn_0EQ3iTHVsdZTr0oc7l3UHf; S_INFO=1606143236|1|##|zcbnu@sina.com; ANTICSRF=37ada45b3c36da922f9d8e2d06f8c2ca; sid=vUVA4IWw3D1RLZfJxxu4VshD4AikJ4WooTmMtCxs; login_id=b6a67900-2d9b-11eb-b457-dd990e0816a5"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fplatform_type%3D2%26view_loc%3Dequip_list; NTES_PASSPORT=yd.sxMsqWRa906nyfC0pRQOCq3XNyDiDvJC5EfznA04YpvFRpWZ9_iFDK2GaSymyXYpIkfaXAEw1D1Pldif_91PZ80efDXxJ1t4m12gM4EOkSyyVsH6QPhtAeWasEogRYHyy1orQ4r01XG2v11Rmz0PPQ.NrvhUWMJ4rm6U_Dcnr9xS7fneW6axT9; P_INFO=zcbnu@sina.com|1605947747|1|cbg|00&99|bej&1605322018&cbg#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=HHoQMm.wqtKEj0JM6xhZOh631wEKDxyqlaFANEgl_eBxqC5iqgFBt65W_jD9p2x2ssax2EeTBwd.FmBbhB7zmt3zxKQk6CRYVjKfFbWQZVDKyzFtfEpdU1B5boo0KgBPtcifZwWNrAwsIGGZb3ghi3nISnNRXjie2zir1MkDL_RjcVctq7QLZ.EladYVFbcR1aZq3.mYKSic6; S_INFO=1606232392|1|##|zcbnu@sina.com; ANTICSRF=0b3975ad46881b6ab7096719daa0a306; sid=tSbx5bSylZ2j1aGeaz77gJKh_haWmSilQtfA2eYy; login_id=4bcb867a-2e6b-11eb-929b-b5ca910a7bd5"
cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fplatform_type%3D2%26view_loc%3Dequip_list; NTES_PASSPORT=yd.sxMsqWRa906nyfC0pRQOCq3XNyDiDvJC5EfznA04YpvFRpWZ9_iFDK2GaSymyXYpIkfaXAEw1D1Pldif_91PZ80efDXxJ1t4m12gM4EOkSyyVsH6QPhtAeWasEogRYHyy1orQ4r01XG2v11Rmz0PPQ.NrvhUWMJ4rm6U_Dcnr9xS7fneW6axT9; P_INFO=zcbnu@sina.com|1605947747|1|cbg|00&99|bej&1605322018&cbg#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=TUFMZuvg7CBPz6N3FZcw4Gjc8h1NsOiYTdEF_XPrM2k9mVb8mPEkn1bNMohlC090GGd90X2YkU.OEaksKk3pan6p9qLR1VAS7oqWEsNLj7hqwpEnWXC.DykbsuufqPktnAWZdEBa69X9GAMebF.Nf88u7j6sPr02YuJ0tZbqgR7.2t3Nxe56qbB6rtv4jZYApdjm6OaSqv8Z1; S_INFO=1606234790|1|##|zcbnu@sina.com; ANTICSRF=8ea7126997b83671e90c4982c73aad09; sid=v4XlPG2yr70a8hviwYSKT3rtD-fGmQ-Jd7N2veCJ; login_id=e12768cf-2e70-11eb-8e1a-b86174445dc1"
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
		else: return 0
	if isinstance(ret, dict):
		return sum(ret.values())
	return ret 
sortAndPrint(ranks, [
	"statis.speed.2",
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