#!/usr/bin/env python3
import sys
sys.path.insert(1, '../imports/')
sys.path.insert(1, 'imports/')

import utils
# user_agent(), email(), password(), get_flag_ids()
import requests as r
import json
from bs4 import BeautifulSoup
from pwntools import *



# MODIFY THIS PART !!!
IP_ADDRESS = sys.argv[1]
SERVICE = "TEST"
PORT = 1234
TARGET_URL = f'http://{IP_ADDRESS}:{PORT}'
# MODIFY THIS PART !!!



valid_users = utils.get_flag_ids()[SERVICE][IP_ADDRESS]
#print(flag_ids)

headers = { 
    'User-Agent': utils.user_agent(),
    }

for user in valid_users:
    #s = remote(IP_ADDRESS, PORT)
    s = r.Session()
    res = s.get(TARGET_URL + '/login.php', headers=headers)
    soup = BeautifulSoup(res,features="html5lib")
    #soup.div[0].text
    flags = ['DUMMY_FLAG']
    print(flags)

