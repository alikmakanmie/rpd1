from data import *
from bs4 import BeautifulSoup
from rich.panel import Panel
from rich import print as prints
import requests
import random
import re
import json
import time
import sys

cp = 0 
ok = 0
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

def jeda(t):
    for x in range(t+1):
        print('\rTunggu %s Detik  live=%s    ' % (str(t), ok), end=''); sys.stdout.flush()
        t -= 1
        if t == 0: break
        else: time.sleep(1)

class Main2:
    counter = 1

    def __init__(self, user, pw, cok):
        self.r = requests.session()
        self.metodes = random.choice(["https://i.instagram.com", "https://www.instagram.com", "https://api.instagram.com"])
        self.device = random.choice(["samsung", "infinix", "oppo", "vivo", "realme", "redmi", "xiaomi", "nokia"])
        self.uas = random.choice([f"instagram ({self.device})"])
        self.infourl = f'{self.metodes}/{user}'
        self.user = user
        self.eo = "Helo Semua Ini Adalah Akun Hasil CreateBot"
        self.pw = pw
        self.cok = cok.strip()
        self.dtk = random.randint(1, 50)
        self.apsi = random.randint(2, 30)
        self.mnt = random.randint(1, 3)
        self.ad = random.choice([f"{self.dtk} detik", f"{self.mnt} menit"])
        self.eu = random.choice(["Selamat Menikmati", "Sambil Ngopi Biar Enak", "Jangan Terlalu Sering Create", "Selamat Yahh", "Kamu Keren Bang", "Emang Keren Sih"])
        self.step()
        
    def step(self):
        try:
            req = self.r.get("https://accountscenter.instagram.com/password_and_security/two_factor/", headers=hed, cookies={"cookie": self.cok}).text 
            ID = re.search('"clientID":"(.*?)"', str(req)).group(1)
            
            data = GetData(req)
            data.update({
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
                'variables': json.dumps({
                    "input": {
                        "client_mutation_id": ID, 
                        "actor_id": data['av'], 
                        "account_id": data['av'], 
                        "account_type": "INSTAGRAM", 
                        "device_id": "device_id_fetch_ig_did", 
                        "fdid": "device_id_fetch_ig_did"
                    }
                }),
                'server_timestamps': True,
                'doc_id': '6282672078501565'
            })
            res1 = self.r.post("https://accountscenter.instagram.com/api/graphql/", data=data, headers=header, cookies={"cookie": self.cok})
            key = re.search('"key_text":"(.*?)"', str(res1.text)).group(1)
            xxx = key.replace(" ", "")
            otp = self.r.get(f"https://2fa.live/tok/{xxx}").json()["token"]
            self.Auten(otp, req, xxx, key)
        except Exception as e:
            print(e)

    def Auten(self, otp, req, xxx, key):
        req1 = self.r.get("https://accountscenter.instagram.com/password_and_security/two_factor/", headers=hed, cookies={"cookie": self.cok}).text 
        aid = re.findall('"clientID":"(.*?)"', str(req1))[0]
        data = DataGet(req)
        data.update({
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": "useFXSettingsTwoFactorEnableTOTPMutation",
            "variables": json.dumps({
                "input": {
                    "client_mutation_id": aid, 
                    "actor_id": data["av"], 
                    "account_id": data["av"], 
                    "account_type": "INSTAGRAM", 
                    "verification_code": otp, 
                    "device_id": "device_id_fetch_ig_did", 
                    "fdid": "device_id_fetch_ig_did"
                }
            }),
            "server_timestamps": True,
            "doc_id": "7032881846733167"
        })
        ps = self.r.post("https://accountscenter.instagram.com/api/graphql/", data=data, headers=head, cookies={"cookie": self.cok})
        if '"success":true' in str(ps.text):
            self.Kode(req1, key, aid)
            time.sleep(5)
        elif '"success":false' in str(ps.text):
            return "gagal\n"

    def Kode(self, req1, key, aid):
        data = KodeGet(req1)
        data.update({
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'useFXSettingsTwoFactorFetchRecoveryCodesMutation',
            'variables': json.dumps({
                "input": {
                    "client_mutation_id": aid, 
                    "actor_id": data['av'], 
                    "account_id": data['av'], 
                    "account_type": "INSTAGRAM", 
                    "fdid": "device_id_fetch_ig_did"
                }
            }),
            'server_timestamps': True,
            'doc_id': '24140213678960162',
        })
        ps = self.r.post("https://accountscenter.instagram.com/api/graphql/", data=data, headers=headers, cookies={"cookie": self.cok})
        js = ps.json()
        if '"success":true' in str(ps.text):
            recovery_codes = js["data"]["xfb_two_factor_fetch_recovery_codes"]["recovery_codes"]
            codes = "\n".join(code.replace(" ", "\t") for code in recovery_codes)
         #   self.fetch_follower_data()  # Call to fetch follower and following data

            key_with_counter = f"{Main2.counter}. {self.user}"
            prints(Panel(
                f'[white][[green]•[white]] Status              : [green]Sukses\n'
                f'[white][[green]•[white]] Username            : {self.user}\n'
                f'[white][[green]•[white]] Password            : {self.pw}\n'
                f'[white][[green]•[white]] Berhasil Add Profil : a{self.apsi}.jpg{P}\n'
                f'[white][[green]•[white]] Follow              : sukses\n'
                f'[white][[green]•[white]] Hasil Disimpan      : AkunFresh.txt\n'
                f'[white][[green]•[white]] Berhasil Masang Bio : {self.eo}\n'
                f'[white][[green]•[white]] Pesan               : {self.eu}\n'
                f'[white][[green]•[white]] Lama Pembuatan      : {self.ad}\n'
                f'[white][[green]•[white]] Device Login        : {self.device}\n'
                f'[white][[green]•[white]] Url Akun            : {self.infourl}\n'
                f'[white][[green]•[white]] User-Agent          : {self.uas}\n'
                f'[white][[green]•[white]] SecretKey           : {key}\n'
                f'[white][[green]•[white]] Kode A2F            : {codes}\n'
                f'[white][[green]•[white]] Cookie Akun         : {self.cok}\n',
                title=f"[white][ [green]BERHASIL DI BUAT [white] ][white]",
                width=80,
                padding=(0, 4),
                style="#9F9F9F"
            ))
            with open("/sdcard/akunigewel.txt", "a") as file: 
                file.write(f"{self.user}\n{key}\n{codes}\n")
            open(f"/sdcard/cokiig.txt","a").write(f'{self.cok}\n')
                
            Main2.counter += 1
            