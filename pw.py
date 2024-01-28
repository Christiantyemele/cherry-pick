#!/home/christian/PycharmProjects/cherry-pick/venv/bin/python3
# an insecure password locker
import pyperclip
import sys
PASSWORDS = {'email': 'yemelechristian2@gmail.com' 'SDFSF',
             'blog': 'wrsadfufhaFWEwrr',
             'luggage': '24344'
}


# check if the required number of arguments are being passed
if len(sys.argv) < 2:
    for i in sys.stdin:
     print('Usage: python pw.py [account] - copy account password')

account = sys.argv[1]


if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('password for ' + account + ' copied to clipboard')

else:
    print(f'There is no account named , {account}\ndo you want to create and account ,{account}\nif yes ' 
          f'type in yes else no')
    response = input()
    if response == 'no':
        exit()
    elif response == 'yes':
        password = input(f'enter password for , {account}')
        PASSWORDS[account] = password
        print(f'account {account} has been added to database')
        print(f'confirm this is the account\'s password' , {PASSWORDS[account]})
    else:
        print('I can\'t understand your respond')






