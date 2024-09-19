from src.Data import * 
from src.prox import *
from run import Main2
from bs4 import BeautifulSoup
from rich.panel import Panel
from rich import print as prints


import sys
import time

cp = 0 
sus = 0
ok = 0
P = '\x1b[1;97m'  # PUTIH
M = '\x1b[1;91m'  # MERAH
H = '\x1b[1;92m'  # HIJAU
K = '\x1b[1;93m'  # KUNING

def tunggu(t):
    for x in range(t + 1):
        print(f'\r{P}[{H}Auto Create Instagram{P}] Berhasil :> {H}{ok}{P} Checkpoint :> {K}{cp} {P}Suspend :> {M}{sus} {P}Delay :>{K} {t}{P}', end='')
        sys.stdout.flush()
        t -= 1
        if t == 0:
            break
        else:
            time.sleep(1)
    # Bersihkan baris setelah countdown selesai
    print('\r' + ' ' * 100 + '\r', end='')  # Baris kosong untuk membersihkan tampilan

# Contoh penggunaan
#tunggu(10)
user = open('ua.txt','r').read().splitlines()

def clear():
  os.system("clear")
  

def Username():
  dev = log()
#  es = input('[?] Masukan Bio Untuk Akun : ')
  mail, ses = Mail()
  name = Names()
  ua = random.choice(user)
  Post = POST(ua)
  
  while True:  # Tambahkan loop agar mencoba ulang
    try:
      data = {
        'email': '',
        'first_name': name,
        'client_id': dev,
        'seamless_login_enabled': '1',
        'opt_into_one_tap': 'false',
      }
      pos = requests.post("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/", data=data, headers=Post).text 
      js = json.loads(pos)
      if "username_suggestions" in js:
        respon = js["username_suggestions"]
        step1(mail, name, respon, dev, Post, ua, ses)
        break  # Berhasil, keluar dari loop
      else:
        continue  # Gagal, ulangi dari awal
    except Exception as e:
      print(e)
  
def step1(mail,name,respon,dev,Post,ua,ses):
  pas = pw()
  try:
    
    data = {
      'enc_password': '#PWD_INSTAGRAM_BROWSER:0:%s:%s'%(round(time.time()),pas),
      'email': mail,
      'first_name': name,
      'username': respon[0],
      'client_id': dev,
      'seamless_login_enabled': '1',
      'opt_into_one_tap': 'false',
    }
    pos = requests.post("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/",headers=Post,data=data, allow_redirects=False).text 
    js = json.loads(pos)
  except Exception as e:
    print(e)
  ttl(mail,name,respon,dev,pas,Post,ua,ses)

def ttl(mail,name,respon,dev,pas,Post,ua,ses):
  day  = random.randint(1,29)
  bln = random.randint(1,12)
  thn = random.choice(['2000','2001','2002','2003','2004'])
  try:
    data = {
      'day': day,
      'month': bln,
      'year': thn
    }
    pr = requests.post('https://www.instagram.com/api/v1/web/consent/check_age_eligibility/',headers=Post, data=data).text 
    jsk = json.loads(pr)
  except Exception as e:
    print(e)
  Code(mail,name,respon,dev,pas,day,bln,thn,Post,ua,ses)
def Code(mail,name,respon,dev,pas,day,bln,thn,Post,ua,ses):
  try:
    data = {
      'device_id': dev,
      'email': mail
    }
    ps = requests.post("https://www.instagram.com/api/v1/accounts/send_verify_email/",headers=Post,data=data).text 
    jsb = json.loads(ps)
    #print("\n[*] Email: %s"%(mail))
    #print("[*] sedang mengirim kode"); time.sleep(0.01)
    while True:
      mass=Email(ses).inbox()
      if mass:
        topic = mass['topic'].split()[0]
        #print("[*] Kode: %s"%(topic))
        break
  except Exception as e:
    print(e)
  confirm(mail,name,respon,topic,dev,pas,day,bln,thn,Post,ua)
  
  
def confirm(mail,name,respon,topic,dev,pas,day,bln,thn,Post,ua):
  try:
    
    data = {
      'code': topic,
      'device_id': dev,
      'email': mail
    }
    pk = requests.post("https://www.instagram.com/api/v1/accounts/check_confirmation_code/",headers=Post, data=data).text 
    jh = json.loads(pk)
    
    if 'signup_code' in jh:
      sign_up = jh["signup_code"]
      Create(mail,name,respon,sign_up,dev,pas,day,bln,thn,Post,ua)
    else: 
      sys.exit(1)
  except Exception as e:
    print(e)
  
def Create(mail,name,respon,sign_up,dev,pas,day,bln,thn,Post,ua):
  global ok, cp, sus
  usernam = respon[0]
  data = {
    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:%s:%s'%(round(time.time()),pas),
    'day': day,
    'email': mail,
    'first_name': name,
    'month': bln,
    'username': usernam,
    'year': thn,
    'client_id': dev, 
    'seamless_login_enabled': '1',
    'tos_version': 'row',
    'force_sign_up_code': sign_up
  }
  
  pos = requests.post("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/",headers=Post, data=data,allow_redirects=True)
  if 'user_id' in str(pos.text):
    cok = str(pos.cookies)
    tok = re.findall('csrftoken=([^ ]+)',cok)[0]
    cokie = re.findall(r'<Cookie ([^=]+)=([^ ]+) for .instagram.com/>', cok)
    coki = '; '.join([f"{name}={value}" for name, value in cokie])
    up = posting(tok,coki)
    if "https://www.instagram.com/accounts/suspended/" in str(up):
      sus+=1
 #     prints(Panel(
  #  f'\r[white][[red]•[white]] Status : [red]Suspend  [white]\n'
#    f'\r[[red]•[white]] Username : {usernam}\n'
#    f'\r[white][[red]•[white]] Password : {pas}',
#    title=f"\r[red][ SUSPEND ][red]",
  #  width=80,
   # padding=(0, 4),
  #  style="#9F9F9F"
#))
  #    print(f"\r[*] Username: {usernam}\n[*] Password: {pas}\n[*] UserAgent: {ua}\n[*] Cookies: {coki}")
 #     print("[?] Akun Di Nonaktifkan\n")
      
    else:
      #print("[*] CREATE AKUN SUKSES             ")
   #   print(f"\r[*] Username: {usernam}\n[*] Password: {pas}\n[*] UserAgent: {ua}\n[*] Cookies: {coki}")
    #  print("[+] Berhasil Upload Photo\n")
      user = usernam
      pw = pas
      cok = coki
      Main2(user,pw, cok)
      ok+=1
   #   Bio(cok, tok)
      bot_follow(cok, tok)
     
      open("ok.txt","a").write(usernam+"|"+pas+"|"+coki+"\n")
  else: 
#    prints(Panel(f'[white][[red]•[white]] Status : [yellow]Checkpoint  [white]\n[[red]•[white]] Username : {usernam}\n[white][[red]•[white]] Password : {pas}',
       #     title=f"[red][ INVALID][red]", width=80, padding=(0, 4), style="#9F9F9F"))
   # print("\r[*] Create Checkpoint             ")
  #  print("[*] Username: %s\n[*] Password: %s\n[*] UserAgent: %s\n"%(usernam,pas,ua))
   # prints(Panel(
#    f'\r[white][[yellow]•[white]] Status : [yellow]Checkpoint  [white]\n'
#    f'\r[[yellow]•[white]] Username : {usernam}\n'
#    f'\r[white][[yellow]•[white]] Password : {pas}',
#    title=f"\r[white][ [yellow]INVALID [white]][yellow]",
#    width=80,
#    padding=(0, 4),
#    style="#9F9F9F"
#))
    open("cp.txt","a").write(usernam+"|"+pas+"\n")
 #   cp+=1
  tunggu(10)
#import requests
#import re
def Bio(cok, tok):
    bios = f"Helo Semua Ini Adalah Akun Hasil CreateBot"
    header = {
      'authority': 'www.instagram.com',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
      'cache-control': 'max-age=0',
      'dpr': '1.5',
      'sec-ch-prefers-color-scheme': 'dark',
      'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
      'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-model': '"SM-J250F"',
      'sec-ch-ua-platform': '"Android"',
      'sec-ch-ua-platform-version': '"7.1.1"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'none',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
      'viewport-width': '980',
    }
  
    req= requests.get('https://www.instagram.com/accounts/edit/', cookies={"cookie":cok}, headers=header).text 
    
  
    headers = {
      'authority': 'www.instagram.com',
      'accept': '*/*',
      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'https://www.instagram.com',
      'referer': 'https://www.instagram.com/accounts/edit/',
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
      'x-csrftoken': f"{tok}",
      'x-ig-app-id': '1217981644879628',
      'x-ig-www-claim': 'hmac.AR14eYoEFF2NWxaAbiIIbG3rGSSgS2VCHbfRjFoPoLm-5s0z',
      'x-instagram-ajax': '1015039620',
      'x-requested-with': 'XMLHttpRequest',
    }
  
    data = {
      'biography': f'{bios}',
      'chaining_enabled': 'on',
      'email': self.mail,
      'external_url': '',
      'first_name': re.findall('"full_name":"(.*?)"',str(req))[0],
      'phone_number': '',
      'username': re.findall('"username":"(.*?)"',str(req))[0],
    }
    res = requests.post('https://www.instagram.com/api/v1/web/accounts/edit/', cookies={"cookie":cok}, headers=headers, data=data).text
    if '"status":"ok"' in str(res):
      print(f'{P}[{H}•{P}] Memasang Bio     : {H}{bios}')
      #print(f"[*] Bio: {self.bio}\n[*] token: {tok}\n[*] cookies: {cok}\n")
      gg = ""
    else: pass
def bot_follow(cok, tok):
    def get_instagram_id(username):
        url = f"https://www.instagram.com/{username}/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                script_tag = soup.find("script", text=re.compile('profilePage_'))
                if script_tag:
                    match = re.search(r'profilePage_(\d+)', script_tag.text)
                    if match:
                        return match.group(1)
            return None
        except Exception as e:
            print(f"Error mendapatkan ID: {e}")
            return None

    # List username viral yang ingin di-follow (maksimal 30)
    username_list = [
        "instagram", "natgeo", "cristiano", "leomessi", "therock", 
        "kimkardashian", "kyliejenner", "selenagomez", "arianagrande", 
        "neymarjr", "nike", "victoriassecret", "fcbarcelona",
        "championsleague", "taylorswift", "beyonce", "justinbieber", 
        "katyperry", "shakira", "mileycyrus", "alikmakanmie"
            ]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0.1; HUAWEI GRA-L09 Build/HUAWEIGRA-L09C150B196) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (21/5.0.1; 480dpi; 1080x1794; HUAWEI; HUAWEI GRA-L09; HWGRA; hi3635; hu_HU; 98288242)',
        'x-ig-app-id': '1217981644879628'
    }

    # Proses follow untuk setiap username
    for username in username_list:
        user_id = get_instagram_id(username)
        if user_id:
            try:
                HD3 = {
                    "Host": "www.instagram.com",
                    "content-length": "108",
                    "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                    "x-ig-app-id": "1217981644879628",
                    "x-ig-www-claim": "hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03Dg4v5",
                    "sec-ch-ua-mobile": "?1",
                    "x-instagram-ajax": "1007404816",
                    "user-agent": headers['User-Agent'],
                    "viewport-width": "360",
                    "content-type": "application/x-www-form-urlencoded",
                    "accept": "*/*",
                    "x-requested-with": "XMLHttpRequest",
                    "x-asbd-id": "198387",
                    "sec-ch-ua-full-version-list": '"Chromium";v="110.0.5481.153", "Not A(Brand";v="24.0.0.0", "Google Chrome";v="110.0.5481.153"',
                    "x-csrftoken": f'{tok}',
                    "sec-ch-prefers-color-scheme": "light",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://www.instagram.com",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://www.instagram.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                    "cookie": f'{cok}'
                }
                Pay = {
                    "container_module": "profile",
                    "nav_chain": "PolarisProfileRoot:profilePage:1:via_cold_start",
                    "user_id": user_id
                }
                API = requests.post(f'https://www.instagram.com/api/v1/friendships/create/{user_id}/', headers=HD3, data=Pay)
                if API.status_code == 200:
                   d = "kss"
                   # print(f"Berhasil Follow: {user_id}")
                else:
                  jff = '8#'
                  #  print(f"Gagal Follow: {user_id}, Status code: {API.status_code}")
            except Exception as e:
                eie = "kas"
               # print(f"Terjadi kesalahan saat mencoba follow {username}: {e}")
        else:
            eo = "sks"
  #       a   print(f"ID Instagram tidak ditemukan untuk: {username}")
# Contoh penggunaan
#cok = "your_cookie_here"
#t#ok = "your_token_here"

#bot_follow(cok, tok)
def posting(tok,coki):
  #global img
  try:
 #   p_pic = img# ganti sama alamat file foto yang mau di unggah
    ahe = random.randint(2,99)
    p_pic_s = f'a{ahe}.jpg'
    headers = {
      "Host": "www.instagram.com",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
      "Accept": "/",
      "Accept-Language": "en-US,en;q=0.5",
      "Accept-Encoding": "gzip, deflate, br",
      "Referer": "https://www.instagram.com",
      "X-CSRFToken": '%s'%(tok), # ganti csrftoken sesuai cookie yang valid
      "X-Instagram-AJAX": "1013618137",
      "X-Requested-With": "XMLHttpRequest",
      "Content-Length": str(p_pic_s),
      "DNT": "1",
      "Connection": "keep-alive",
    }
    files = {'profile_pic': open(p_pic_s,'rb')}
    values = {
      "Content-Disposition": "form-data",
      "name": "profile_pic",
      "filename":"profilepic.jpg",
      "Content-Type": "image/jpeg"
      }

    r = requests.post('https://www.instagram.com/accounts/web_change_profile_picture/', files=files, data=values, headers=headers, cookies={'cookie':coki}).text
    return r
    #  open('Create/ok.txt','a').write(usernam+'|'+pas+'|'+coki+"\n")
  except Exception as e:
    print(e)
