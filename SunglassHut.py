
import requests
import pandas as pd
A = int(input('Start Page: '))
B = int(input('End Page: '))
url = "https://www.sunglasshut.com/wcs/resources/plp/10152/byCategoryId/3074457345626651837"

result = []
for x in range(A,B):
    print(f'Page {x}')
    querystring = {"isProductNeeded":"true","isChanelCategory":"false","pageSize":"100","responseFormat":"json","currency":"USD","viewTaskName":"CategoryDisplayView","storeId":"10152","DM_PersistentCookieCreated":"true","pageView":"image","catalogId":"20602","top":"Y","beginIndex":"0","langId":"-1","categoryId":"3074457345626651837","orderBy":"default","currentPage":f"{x}","":""}

    headers = {
        "cookie": "aka-cc=BJ; aka-ct=SA; aka-zp=; mt.v=2.1114217790.1659870989551; dtCookie=-20^; rxVisitor=1659871006107N3HVU920BMTH4MN34LVGFEIA6LI3H9VR; ftr_ncd=6; __wid=388406365; bm_mi=710CC1CC9721B4A24E2C14AB0B6A6B54~YAAQrvUWAmdv4WSCAQAAKosGeBDf1iFZFRTASh34OHiuIjxGOPSQlQI7SwOKVkCnCMlGCKctUzmDLzz9Qry9c2D0BHnatSRRquIx5CZUNFJfJKyywswGtdbYfzewMaAnpZZTArEFU3pHi3Gk9OHXNR1+TtiNRXLxq0M79uC6QvRykO4rl9vh+i2lSoEPAZqJHHkmBechKlfmC+nDZeo6SfitPO4WxwjSzsIJZjj2TTIw8wQ0B0/8MNze0PNvymLkqjnOuybaAkE6pG9fzFGoyO78zQobJmF2vskirjNLr0NBerITrrioJzpZVKBzaH+zO9L9kI+cEy1+r+pD1LmgXWaZ~1; SGPF=3bBjTbbq_iGDB9ry7Uy-z3ExqwXq98z_GkYYiVkg7Iur2XepSV34BNg; dtSa=-; dtLatC=5150; sgh-desktop-facet-state-search=; sgh-desktop-facet-state-plp=categoryid:undefined^|gender:true^|brands:partial^|polarized:true^|price:true^|frame-shape:partial^|color:true^|face-shape:false^|fit:false^|materials:false^|lens-treatment:false; tealium_data2track_Tags_AdobeAnalytics_TrafficSourceJid_ThisHit=208071DIR; tealium_data_tags_adobeAnalytics_trafficSourceJid_stackingInSession=208071DIR; tealium_data2track_Tags_AdobeAnalytics_TrafficSourceMid_ThisHit=direct; tealium_data_tags_adobeAnalytics_trafficSourceMid_thisSession=direct; tealium_data_session_timeStamp=1659871076666; userToken=undefined; TrafficSource_Override=1; AMCVS_125138B3527845350A490D4C^%^40AdobeOrg=1; s_ecid=MCMID^%^7C84530353444511024643730342343399722830; ak_bmsc=8E8861F451DEC13B4CAB49918EC35EC4~000000000000000000000000000000~YAAQrvUWArNv4WSCAQAAqL8GeBC03Y+dRDPTLkU/2JyN6YuQViYakY49ovBMzkxfpZfxW6eZoAAhs9/MuR6zx0XgXJrjmlltkALJIjfT7JSQXx8PI2RIOw5mEoGsRdhRZluOiTiGTfpngFhoxozV9xOX645XkX0Bm79CrUqPoKJRrj9wKfLsQwURaf+xW/npU3EuOzxY/b4c3fDihHdkOKUCPgBV1xJxDNMiuYAysGokU6ReFLRnVmWJ6UvLVukzwL4ERLhBWdtWXsFfIwAQScC/8m39PuogYSPNFz7ia0WTTVv3tCzVDvRxfvocSZ5NEcBQJ9+pmC34C7/h7SJFYcOofbuVZor9JwW6rW3dMMjuR4mlN3ZH4nhN3VfEenXb+hw0iHxM6KwArZcjsVCP0LC9p2leYZHtka2dKsVSiOdTchBvU1yUdttj7XdvaXSHdx9EQEnSTUNz/ErWVkiNELkDXVGeXLNOMcjI6YLw57uByoSEzXru5IVH65HuM16N6P6infNaPfqzjK/5wG/rfkAOnzoc; forterToken=4f720b76863d45f389731e60f0653055_1659871073535_47213_UDF43_6; AMCV_125138B3527845350A490D4C^%^40AdobeOrg=-1303530583^%^7CMCIDTS^%^7C19212^%^7CMCMID^%^7C84530353444511024643730342343399722830^%^7CMCAAMLH-1660475878^%^7C6^%^7CMCAAMB-1660475878^%^7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y^%^7CMCOPTOUT-1659878278s^%^7CNONE^%^7CMCAID^%^7CNONE^%^7CvVersion^%^7C3.3.0; s_cc=true; _cs_mk=0.1546098913998053_1659871088711; CONSENTMGR=consent:true^%^7Cts:1659871100063; __utma=110589831.240130778.1659871108.1659871108.1659871108.1; __utmc=110589831; __utmz=110589831.1659871108.1.1.utmcsr=(direct)^|utmccn=(direct)^|utmcmd=(none); __utmt=1; __utmb=110589831.1.10.1659871108; _gcl_au=1.1.1372798890.1659871109; _pin_unauth=dWlkPU1XVm1aVEZsWTJJdE9HWTFNaTAwTW1ZeExXRmpaamN0TTJSbVpXTXlNRE5tWlRsbA; _ga_6P80B86QTY=GS1.1.1659871111.1.0.1659871111.60; _ga=GA1.1.1239313371.1659871111; _uetsid=ab559df0164211ed9920ed38c9920a9c; _uetvid=ab59a420164211edbfb6f99ef9ef6eb5; _scid=bfe6b9d2-a20b-435a-b658-475d405b22e9; cto_bundle=XQShFV9sTnN6Q0tEY2xKVHh5NFJiWDhVRlJ2NFNMR2N5dVNPYXhvN1FCSjRtbkRweXlVcEE4TUl0RkRLQ1JzYkt3UlBacjVzbVZuJTJGcVNnR0dpZEppNjNkWUElMkZPeHl6RTZIQlMyOFViaWZYd2Q0cFJJdGMlMkYxa0dyNzJEM0k1R2p6UEZDQ01VVWYxT1JFTzhOSFJUekloZmh4akElM0QlM0Q; _fbp=fb.1.1659871116950.1296187071; _tt_enable_cookie=1; _ttp=cf46870e-fb24-4fd9-9e55-f28e501e96f8; MGX_UC=JTdCJTIyTUdYX1AlMjIlM0ElN0IlMjJ2JTIyJTNBJTIyOWE4MzZlMTQtMWE1Mi00ODVlLTgyYjMtMmJiYTQ4ZWNkMzU1JTIyJTJDJTIyZSUyMiUzQTE2NjAzOTY3MDc4ODklN0QlMkMlMjJNR1hfUFglMjIlM0ElN0IlMjJ2JTIyJTNBJTIyYjNkZGJmNDMtOTc1MS00M2NmLWEwZGUtNDQxZjU5YmNjNTFlJTIyJTJDJTIycyUyMiUzQXRydWUlMkMlMjJlJTIyJTNBMTY1OTg3MjkxNzM3OSU3RCUyQyUyMk1HWF9DSUQlMjIlM0ElN0IlMjJ2JTIyJTNBJTIyNGYzMzEzMmYtOTVjYy00MDE3LWE2NDYtMjNmYzdlNGQ2ZDlkJTIyJTJDJTIyZSUyMiUzQTE2NjAzOTY3MDc5NDIlN0QlMkMlMjJNR1hfVlMlMjIlM0ElN0IlMjJ2JTIyJTNBMSUyQyUyMnMlMjIlM0F0cnVlJTJDJTIyZSUyMiUzQTE2NTk4NzI5MTczNzklN0QlMkMlMjJNR1hfRUlEJTIyJTNBJTdCJTIydiUyMiUzQSUyMm5zX3NlZ18wMDAlMjIlMkMlMjJzJTIyJTNBdHJ1ZSUyQyUyMmUlMjIlM0ExNjU5ODcyOTE3Mzc5JTdEJTdE; _sctr=1^|1659826800000; outbrain_cid_fetch=true; rxvt=1659872927523^|1659871006116; dtPC=-20^-vDFTCDCKPBTIIDTLQRMJACITKHGUPNRGQ-0e2; bm_sv=CE6A2DCD25DB696CF813A209FFC0C92D~YAAQp/UWAsx5Y12CAQAAbToIeBAwkMHbzgnrw1fQqWMP5TZLVwv7v9TAdavyu+jkPRVuOirhUBXidbRiDAKh6+FQ5xh/2lzAzNByUjGfd3gdVS7nW9p8IKguFBucnC0oth4GgTf+lxDIk0Shk6Gl18JD/KKCMGDa4vhJ5EoaMawtFph2qNVro03C/7f1lYFHVci9Feh7+qWDdaTWdRZj0D9rAbbDk4J+keoFxLc3XEDwiY/XZKoOkDq1M/CYz84yVVXq0S0=~1; utag_main=v_id:01827806a0f7001bcaec6453f5590506e003c06600838^n:1^e:10^s:0^t:1659873030159^:1659871076601^%^3Bexp-session^n:1^%^3Bexp-session^:sunglasshut.com^:1^:1^%^3Bexp-session^:us-east-1^%^3Bexp-session",
        "authority": "www.sunglasshut.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://www.sunglasshut.com/us/mens-sunglasses",
        "sec-ch-ua": "^\^.Not/A",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\^Windows^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    
    for p in data["plpView"]["products"]["products"]["product"]:
        result.append(p)
        
df =pd.json_normalize(result)
df.to_csv('sunGlassHut.csv')