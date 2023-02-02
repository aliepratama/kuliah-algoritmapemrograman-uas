"""
+ ------------------------------------------------ +
|  Nama Lengkap    : Muhammad Ali Pratama Putra    |
|  NIM             : 5220411416                    |
|  Prodi           : Informatika                   |
+ ------------------------------------------------ +
"""

import json
import os

dir = os.getcwd().replace('\\', '/')
with open(f'{dir}/config.json') as config_file:
    config = json.load(config_file)

def get_string(key):
    return config.get(key)
def getStyleColor():
    return list(config['style_color'].items())