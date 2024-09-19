import re,os, sys
import json
import time 
import random 
import requests
from socialagent import socialagent

ugen = socialagent()

ua = ugen.chrome()

#     HEADER KEY       #
hed = {
  "host": "accountscenter.instagram.com",
  "user-agent": ua,
  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "referer": "https://www.instagram.com/",
  "accept-encoding": "gzip, deflate",
  "accept-language": "id-id,id;q=0.9,en-us;q=0.8,en;q=0.7"
}

header = {
  'Host': 'accountscenter.instagram.com',
  'content-length': '1355',
  'sec-ch-ua': '"Android WebView";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
  'x-ig-app-id': '1217981644879628',
  'sec-ch-ua-mobile': '?1',
  'user-agent': ua,
  'x-fb-friendly-name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
  'x-fb-lsd': 'BmZIkyKP1iWrCryVjZ4-xB',
  'sec-ch-ua-platform-version': "",
  'content-type': 'application/x-www-form-urlencoded',
  'x-asbd-id': '129477',
  'sec-ch-ua-full-version-list': '',
  'sec-ch-ua-model': "",
  'sec-ch-prefers-color-scheme': 'light',
  'sec-ch-ua-platform': '"Android"',
  'accept': '*/*',
  'origin': 'https://accountscenter.instagram.com',
  'x-requested-with': 'mark.via.gp',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://accountscenter.instagram.com/password_and_security/two_factor/',
  'accept-encoding': 'gzip, deflate',
  'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
}

# HEADERS KODE OTP  #
head ={
  'Host': 'accountscenter.instagram.com',
  'content-length': '1391',
  'sec-ch-ua': '"Android WebView";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
  'x-ig-app-id': '1217981644879628',
  'sec-ch-ua-mobile': '?1',
  'user-agent': ua,
  'x-fb-friendly-name': 'useFXSettingsTwoFactorEnableTOTPMutation',
  'x-fb-lsd': 'BmZIkyKP1iWrCryVjZ4-xB',
  'sec-ch-ua-platform-version': "",
  'content-type': 'application/x-www-form-urlencoded',
  'x-asbd-id': '129477',
  'sec-ch-ua-full-version-list':  '',
  'sec-ch-ua-model': "",
  'sec-ch-prefers-color-scheme': 'light',
  'sec-ch-ua-platform': '"Android"',
  'accept': '*/*',
  'origin': 'https://accountscenter.instagram.com',
  'x-requested-with': 'mark.via.gp',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://accountscenter.instagram.com/password_and_security/two_factor/',
  'accept-encoding': 'gzip, deflate',
  'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
}

headers = {
      'authority': 'accountscenter.instagram.com',
      'accept': '*/*',
      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'https://accountscenter.instagram.com',
      'referer': 'https://accountscenter.instagram.com/password_and_security/two_factor/',
      'sec-ch-prefers-color-scheme': 'dark',
      'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
      'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-model': '"SM-J250F"',
      'sec-ch-ua-platform': '"Android"',
      'sec-ch-ua-platform-version': '"7.1.1"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
      'x-asbd-id': '129477',
      'x-fb-friendly-name': 'useFXSettingsTwoFactorFetchRecoveryCodesMutation',
      'x-fb-lsd': 'YZDfCPh7Blp_k7UqlJtLTU',
      'x-ig-app-id': '1217981644879628',
    }
def GetData(req):
  av = re.findall('"actorID":"(.*?)"',str(req))[0]
  __hs = re.search('"haste_session":"(.*?)"',str(req)).group(1)
  __hsi = re.search('"hsi":"([^"]+)"',str(req)).group(1)
  dtsg = re.search('"DTSGInitialData",\[\],{"token":"([^"]+)"}',str(req)).group(1)
  jazoest = re.search('&jazoest=([^"]+)"',str(req)).group(1)
  lsd = re.search('"LSD",\[\],{"token":"([^"]+)"}',str(req)).group(1)
  spinr = re.search('"__spin_r":(\d+)',str(req)).group(1)
  spinb = re.search('"__spin_b":"(.*?)"',str(req)).group(1)
  spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
  return{'av':av,"__user":0,"__a":1,"__req":10,"__hs":__hs,"dpr":3,"__ccg":"EXCELLENT","__rev":spinr,"__hsi":__hsi,"__comet_req":24,"fb_dtsg":dtsg,"jazoest":jazoest,"lsd":lsd,"__spin_r":spinr,"__spin_b":spinb,"__spin_t":spint}
 
def DataGet(req):
  av = re.findall('"actorID":"(.*?)"',str(req))[0]
  __hs = re.search('"haste_session":"(.*?)"',str(req)).group(1)
  __hsi = re.search('"hsi":"([^"]+)"',str(req)).group(1)
  dtsg = re.search('"DTSGInitialData",\[\],{"token":"([^"]+)"}',str(req)).group(1)
  jazoest = re.search('&jazoest=([^"]+)"',str(req)).group(1)
  lsd = re.search('"LSD",\[\],{"token":"([^"]+)"}',str(req)).group(1)
  spinr = re.search('"__spin_r":(\d+)',str(req)).group(1)
  spinb = re.search('"__spin_b":"(.*?)"',str(req)).group(1)
  spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
  return{'av':av,"__user":0,"__a":'1a',"__req":10,"__hs":__hs,"dpr":3,"__ccg":"EXCELLENT","__rev":spinr,"__hsi":__hsi,"__comet_req":24,"fb_dtsg":dtsg,"jazoest":jazoest,"lsd":lsd,"__spin_r":spinr,"__spin_b":spinb,"__spin_t":spint}

def KodeGet(req1):
  av = re.findall('"actorID":"(.*?)"',str(req1))[0]
  __hs = re.search('"haste_session":"(.*?)"',str(req1)).group(1)
  __hsi = re.search('"hsi":"([^"]+)"',str(req1)).group(1)
  dtsg = re.search('"DTSGInitialData",\[\],{"token":"([^"]+)"}',str(req1)).group(1)
  jazoest = re.search('&jazoest=([^"]+)"',str(req1)).group(1)
  lsd = re.search('"LSD",\[\],{"token":"([^"]+)"}',str(req1)).group(1)
  spinr = re.search('"__spin_r":(\d+)',str(req1)).group(1)
  spinb = re.search('"__spin_b":"(.*?)"',str(req1)).group(1)
  spint = re.search('"__spin_t":(.*?),',str(req1)).group(1)
  return{'av':av,"__user":0,"__a":1,"__req":15,"__hs":__hs,"dpr":1.5,"__ccg":"EXCELLENT","__rev":spinr,"__hsi":__hsi,"__comet_req":24,"fb_dtsg":dtsg,"jazoest":jazoest,"lsd":lsd,"__spin_r":spinr,"__spin_b":spinb,"__spin_t":spint}