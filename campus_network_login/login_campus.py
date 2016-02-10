import requests
import sys

xidian='http://10.255.44.33/cgi-bin/srun_portal'

def login():
    action='login'
    username='01125xxx'
    password='xxxxxxxxxxxxx'
    ac_id='6'
    type='1'
    wbaredirect=''
    mac=''
    user_ip=''

    form={'action':action,
          'username':username,
          'password':password,
          'ac_id':ac_id,
          'type':type,
          'wbaredirect':wbaredirect,
          'mac':mac,
          'user_ip':user_ip
          }

    try:
        requests.post(xidian,form)
    except requests.ConnectionError:
        print('false!')

def logout():
    logout={'action':'logout'}
    requests.post(xidian,logout)

if __name__=='__main__':
    logout()
    print('succeed!')

