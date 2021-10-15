import requests as r
import time
import os
import socket

def banner():
    kk=r.get('BANNER LINK').text
    print(kk)

if __name__ == "__main__":
    try:
        pp=r.get('LICENSE LINK EX : https://microsoft.com/licensi.txt').text
        kk=input('[ <!> ] License : ')
        if str(pp) == kk:
            print('[ <!> ] Checking License.')
            time.sleep(3)
            os.system('cls')
            print('[ <!> ] Licensi Valid')
            time.sleep(5)
            banner()
        else:
            print('[ <!> ] Checking License.')
            time.sleep(3)
            os.system('cls')
            print('[ <!> ] Licensi invalid')
            time.sleep(5)
            exit()
    except Exception as e:
        print(e)
    except socket.gaierror:
        print('[!] Check your Connection')
    except r.exceptions.ConnectionError:
        print('[!] Curr !')
    except KeyboardInterrupt:
        print('[!] Ctrl+C Detected, Bye!')
        time.sleep(3)
        os._exit(1)