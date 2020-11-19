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
minPrice = '1500'
maxPrice = '3000'
pass_fair_show=False
order_by_price=True
use_cache=True

# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; ANTICSRF=f507de50e267c7fd9e87ba52b1b006b4; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; is_log_active_stat=1; NTES_SESS=jpHULmkHVdGRnySepayvk7VsdkxEqt6X98GP0ioB8T1ZJYRBJ0rMWQRwDObqT6K6FK1yLyl2q0QDrzMAsMvHzWIHKGnxQY9uSssrVSqcB8Y3RsLPagqisZlTA17wiafw2ToW9k9Kx8eDYsAktJIZvPa_RJByXfA76hItC8oj97a2eC0WFs735t7Wa9K2ngzISMRLLIvA0d4wQ; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; S_INFO=1605409233|0|##|zcbnu@sina.com; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; sid=xuRZIAGhmFza_lIuUiBU7Fy6eHWpjcCCGuZ_bMsD; login_id=ba7a927d-26ee-11eb-b141-5f7c4a15c9fd"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=nZl_bxxUzAVC1olxM4k4aQsqCyX3Czcvw1guaPx2dDZO3iTX3xgZlsTmdNCeLhOhSS1OhPD4Zzywg6ZYVZ5Q6lbQO7FjsioB8N7qgYmFW8C7JQglqPLypGZTY__K7xZ9l4r0j1.Z7SEUQkjPbpW2Z6B2bhObUe1oLtS7IDmvUaB9_jU7eEjTPHapTIFprV1ej1W3bw6B7kXfs; S_INFO=1605416729|1|##|zcbnu@sina.com; ANTICSRF=f228966c4af8fef88931265dbe6a414b; sid=U5R1chsEARYd6XAAfk45S8Harimz-X6R2qjuPDES; login_id=2e6cda07-2700-11eb-afb2-87f16f09631f"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=izNZslJg.eNVt4bnSoT8yFkYnbOEmCPszWIvZQAPjxTu0UVp0AITEqVcjBOgw9u933Wu9Qx8TdN_IfT7eThyfEKyu2JYqUS5DB2rI7cJ4DO2ayIErQwN.mTV7kkl2ATFEUiJaaZvjjusURTtGm9xCxPAoO2QoErLUgJsiCOoZYtT5p0DZEY_yUfPWN5DI7nSmW40K_f52bpnq; S_INFO=1605420687|1|##|zcbnu@sina.com; ANTICSRF=1957a7548a39d9a5d8dff6c48a44f164; sid=wPJCSJD2ttmIKtB86gmEYCuH-pseBRkNbb8F1zhR; login_id=65cc2dd7-2709-11eb-9d83-0f46eba7ebf3"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=FFZXC0cb.QP07fl3tEVpIVYNibh3ytWbXKkB0RjMfdtNDJLIDjktuVL2fry_G.N.88KN.RdEt6qmkhtiwtpshuCsNUSnVJ4XzrUeki2SlzyU3skueRGq17tLiccOUjtouAxih8xthEBjT4zveeeZ.gIl5wJvsdE3Iy_MlyXmQknBPCvrb.HOICgCVvu3dETxQKlDCmhXUHI9V; S_INFO=1605438505|1|##|zcbnu@sina.com; ANTICSRF=9a9c4efc7d713dafbe121777909d8d04; sid=6Hs6oxgSs_dCT4sstRKtdyrmIdyV6q-NmfopTKv3; login_id=e240369c-2732-11eb-9467-f64f867fb1f2"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=mjP7RYmpl2S0LJSAOLABHuTtuEMWtkQepFhDQKVbLTy8RcNfRVhy3uNILz45rY8YMMF8YKTaytEXhAy_ByjlA3ol8k2wucUdZzkvh_I2JZ4kPlh3vKrEngyN_ppSkVy73A_F6dbgRtF7ywd.bDmcEEH3QnkEoKWiRw2aGOFC2B2l_Q.GpY3VqsGC70J6PulV4FJRoXAdk.fGu; S_INFO=1605443426|1|##|zcbnu@sina.com; ANTICSRF=a506ef29638a339805b20f547bcd16be; sid=GGBfWItvpBXpjY54_oSSeb6qGQ55Al9XM-huizPe; login_id=5723077a-273e-11eb-bef1-68cb009e0442"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=pVpZp_1Tn.bUDX9kJkpGBoHciG4WCElVCcGs4JvFBu8Rl.DwlvG8Q0DnBTMAdgRgKKcRgJuC8NZjGr8hx8earQ2aR9150.bVOT9tGhn1HOM9WaGQtJdZ_f8DhYYP9v8IQkEyMHg2KbI.Y4KcXSPOue453UOAwQglK9kbC_bnC1AcoLfZ.LvBdxQHRTCFACsMWcHl2jrV97wX0; S_INFO=1605452095|1|##|zcbnu@sina.com; ANTICSRF=87cd00640d16513907cd072d0c42b6db; sid=w7_SSP5HoiKJ7ecBb4IDXmhxy3MiVWfBKto-bvqo; login_id=865500e1-2752-11eb-bcbe-447e5c9c60ab"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=t0.NQrUEIUSsbabVCL5Z2M6VeRFq7AGqn6uomgMeaUc.7LHE7Muc9bHqaWpOQD.DYY6.DgUncJ1yu3cTCc8I395I.VAZbLj4iWVKuTqAfipVGIu9KgQ1zscHTNNhVMcx9M2alvyh6H4zLX4VrxmztSlGWF7cdWvv6E2.PjZVf1mu3t8Cx6hfHa6f35uhKbVDa6f75y34VBE0b; S_INFO=1605461003|1|##|zcbnu@sina.com; ANTICSRF=57124bdcea6c5ccdcdf6fe232511d811; sid=ic9tZ77Iux7lldTB-DgfCU6kaIPgKwz36pK4_hNs; login_id=440c4902-2767-11eb-910d-72994a498080"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=nZEkm3_bj3tihEO.F..ABVdULIXdkspj.1guaPx2dDZO3iTX3xgZlsTmdNCeLhOhSS1OhPD4Zzywg6ZYVZ5Q6lbQO7FjsioB8N7qgYmFW8C7JQglqPLypGZTY__K7xZ9lBUXAbhM9G3aGxyn0MEzTzfIKoRpDcMyXotJR6kneIV3Ip2JGfNQsEuBSR2rkD77K1W3bw6B7kXfs; S_INFO=1605540500|1|##|zcbnu@sina.com; ANTICSRF=e8963c43e2c374993e663865e2a85dfd; sid=2FFvCVQ0JVrotRdJeRuiNFf2fWpjFrewINGXiUvO; login_id=5baef051-2820-11eb-b358-6df3bf154b54"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=htUGsVgzr8JeovaWWVBDKzPzdkrV6sv3NkwySUzivE3Q490e4zw3CZ0YvsPLxXQXWWkQXUEK3uRAwB3ft3rMBCcMQn.6Z91qlsnTwfY.blPnoMwCTUxRgj30fGGHnz3pC9cS6e3Tf218_pSFVxHYgVdclCbAhg_pe_KxW.9HXGg9q.sb11Ngb8eg0_.gVtkL6kb4cABqnme5Z; S_INFO=1605543184|1|##|zcbnu@sina.com; ANTICSRF=4d6656baa7ddce2eb577142777c2eacd; sid=fSIYlK-UU58O_2GGm4372lX-xb4AwZe3hBtB2vuU; login_id=9bd2dbca-2826-11eb-9b88-9720277d55bd"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=lSbJefEofyNzhRR9_C3fWq6rGsW5Osi73sM_6x.D1pfw5EnP5.MfeYn31mLUFCwCBBswCxprfIGJMbf4ifHAbeTAw8uWYENcXm87M43uqXL8vAMe7xFGQSfn4aaV8.fOeBNWhyHvqmJBeLJ6stBI5QVLP_kAgkaafRd1knM1qnGvJZIiHWoGPOLuErktG7EIbsq5TJbc8ZPKY; S_INFO=1605546020|1|##|zcbnu@sina.com; ANTICSRF=5f01e74d8ebe98021de8be0c7cdb6bd1; sid=ZVb3cX87fcqDQR-CIO7B8up-6H1tvPfru6gs-5Mr; login_id=363a1feb-282d-11eb-864f-5e8394df1ea8"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=q9J7hIx3YXRyGptl5NqPbvaaTXX1CqilvADUIhC5QH1ikrW0kCD17oWvQJn8lTiT__AiThHm1PFEDR1N41Z9R7j9iBeyorwacJBSDNveGcnBg9D7ShlFtu1WNzzYBC1V7xZbcWsm5j8yjI3oUErNGgxAUH1fnmxB882kSUrhKOZxLh4g4wdyWXs7spi_F0d7QAGkjERaBd0so; S_INFO=1605628178|1|##|zcbnu@sina.com; ANTICSRF=9b1ef86f20f78ae84707ce52cdb3d688; sid=bjEa9tuB76KUz5-NWiHx3LP_wZQhOaN8LEfD59sz; login_id=7fcc0e42-28ec-11eb-9436-6b72828dbf07"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=q9J7hIx3YXRyGptl5NqPbvaaTXX1CqilvADUIhC5QH1ikrW0kCD17oWvQJn8lTiT__AiThHm1PFEDR1N41Z9R7j9iBeyorwacJBSDNveGcnBg9D7ShlFtu1WNzzYBC1V7xZbcWsm5j8yjI3oUErNGgxAUH1fnmxB882kSUrhKOZxLh4g4wdyWXs7spi_F0d7QAGkjERaBd0so; S_INFO=1605628178|1|##|zcbnu@sina.com; ANTICSRF=9b1ef86f20f78ae84707ce52cdb3d688; sid=bjEa9tuB76KUz5-NWiHx3LP_wZQhOaN8LEfD59sz; login_id=7fcc0e42-28ec-11eb-9436-6b72828dbf07"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=omy.Tn8S6rY4Sb4KA8A45SZXLrwOnqNqICcrDZfah6xqzSAkzfcxNLAUhesmY1q1EECq1Z6ux5V7cpxFGxITpNQTqJ49LSlgveJwcFU4OvsJ8TcNwZYVbixAF22yJfxWNHKkK3bHWiX585f1nWMr0KcgvhyOd6lLA0WXHdFLPvMjAbT9jqeo0wEgEQ8MPV6dFCOzQ7pgJPk.L; S_INFO=1605632568|1|##|zcbnu@sina.com; ANTICSRF=cf4b384720b45b064e7ec6066bf52daa; sid=qESBaJ_C0mhmVebrvsPAM7spyoWgZe1w1NuQqb2d; login_id=b8c55442-28f6-11eb-a687-c71cec7a315c"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=x8_vPGjPp0NQZhylrzoI4nr2k.3FEMC_l5NW7_aw3J21iAPuiaN2.HPV3KIyRz1znn51z_J92SbsN82tQ2Ek8.Xk1Lj0HAflFKLCNtVjhFILYkN.C_RbvT2PtqqpLa2d.zemMt71vHtyWH52gwq.Ix6bcCzfkvC1Js7gJTh4pUxcWtv1aazusr8truKf5Tsz25hiXs8lLruDH; S_INFO=1605636243|1|##|zcbnu@sina.com; ANTICSRF=7e7f02c643a6d28214b50169d6e5f4b8; sid=xQi22Et3KvGU2TPsda2XKZe5i5eERFCyoy_v9VNy; login_id=473d37d4-28ff-11eb-b717-8a73a8e8bbb9"
# cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=8JWSii4n1_o1ujse.H6HHPT9W1QEEv75gNQIjLFto9YgfD7CfFQYXm7ZokePUlgl66NglL95Y._MQWY32YKwWXqwg0zSmDvbhk0cQ3ZzBhe0dwQXcLU_OaY73RRr0FYEX78GTwcsuR3fLfGQmgRsf9jkyYy3V61ZhJueTysDP7CYtfmlc46MmcKXYQqQKd6mYNBfqMWb0sC4m; S_INFO=1605716057|1|##|zcbnu@sina.com; ANTICSRF=2827be97d4c291d222ed723167efb2aa; sid=YrC_LZado8CRi3TFY0yadVU8S4j3QY3SX2zvwTRK; login_id=1bef3657-29b9-11eb-8ad3-5f5060ab79f2"
cookie="fingerprint=8yeydgncqbuntcsl; urs_share_login_token=zcbnu@sina.com$34ebf23db355bf0a8a7bda4648dc9171; _external_mark=reg.163.com; back_url=https%3A%2F%2Fyys.cbg.163.com%2Fcgi%2Fmweb%2Fpl%2Frole%3Fsearch_type%3Drole%26platform_type%3D2%26six_star_num%3D66%26price_min%3D200000%26price_max%3D200000; NTES_PASSPORT=2XiJx2giXzAGFVvrxEOnpHQVMmfLdqLwGhmybuKv8oIzqC5iqgFBt65W_jD9p2x2szqVLu9s8b0eWeYkl6utBeYF1oZuWs4heSIxejTnIbcKrZPGZrlzqZUFI0R4hkj0_yFXSZycRXLxFE643Rd4tbjrecM.3iViXZFx7NUTJoh7B4pduvZgO94JB; P_INFO=zcbnu@sina.com|1605409233|1|cbg|00&99|null&null&null#bej&null#10#0#0|&0|cbg|zcbnu@sina.com; is_log_active_stat=1; NTES_SESS=Ckg9GTf15vD9p2n1612_Hv_jzLKziGuu6ZJGBzIEkg5ArOhUrIJ5Lfh4kYxF.PAPqqZAPzgV5_joJc5K952dcL0dAlybfOs7eYlnJK4yTexlNdJLnz.jMW5hKSStlI5QL3YWDmCjUHiNDnCqWv0d57PCUeEEBs7BgXCAUczmBpUSxrTehFMtMqMmHVgfxEN5XZTr0oc7l3UHf; S_INFO=1605745499|1|##|zcbnu@sina.com; ANTICSRF=063e5da738458ff29d91a71fcb2dee10; sid=4vDTzrJhNxSh1i9ouoAoXcHhSttDrQtu9Pw8HpH1; login_id=a8b5ad26-29fd-11eb-9911-7530f016f468"
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
	print result['game_ordersn']
	ordersn = result['game_ordersn']
	if use_cache and ordersn in _cache and _hasSortKey(_cache[ordersn]):
		d['sort'] = _getSortVal(_cache[ordersn])
		d['game_ordersn'] = ordersn
		d['cache_mark'] = True
		d['serverid'] = _cache[ordersn]['serverid']
		d['expire_remain_seconds'] = result['expire_remain_seconds']
		print _sortKey, _getSortVal(_cache[ordersn]), "from cache"
	else:
		print 'printEquip',ordersn,result['serverid']
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
			print data['sort'], data['game_ordersn']
	ret = sorted(_allData, key=lambda v:int(v['sort']), reverse=reverse)
	rankList=[]
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
			rankList.append(v)
			if index > 150: break
	_allData = ret
	return rankList
def sortFunc(data):
	ret = 0
	print data
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
		print u'排行榜：', sortKey
		with io.open(sortKey+maxPrice+'rank.txt', 'w', encoding='utf-8') as f:
			ret = sorted(rankList, key=lambda i: findKey(i, sortKey), reverse=True)
			index = 1
			for l in ret:
				print sortKey,u'排行','第{}名=========='.format(index)
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
	return ret 
sortAndPrint(ranks, [
	"statis.speed.2"
	"statis.suitSum.crit.poshi-crit",
	"statis.suitSum.speed.zhaocai-speed",
	"statis.speedSum-2",
	"statis.speedSum3",
	"statis.subValSpeical.critRateAdditionVal",
	"statis.AssetVal"
	"detail.pvp_score",
	"statis.equipnum",
])
# print _cache["202010211701616-3-WSXGZM6LMLBZDI"], _hasSortKey(_cache["202010211701616-3-WSXGZM6LMLBZDI"])
# printRank(lambda v: v['expire_remain_seconds'], False)