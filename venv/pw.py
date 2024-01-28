#!/home/christian/PycharmProjects/cherry-pick/venv/bin/python3
# an insecure password locker

PASSWORDS = {'email': 'yemelechristian2@gmail.com' 'SDFSF',
             'blog': 'wrsadfufhaFWEwrr',
             'luggage': '24344'
}

import sys
# check if the required number of arguments are being passed
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1]

import pyperclip
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])



