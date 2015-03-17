from django.conf import settings
import requests

def get_token():
    
    with open('token.txt', 'r') as file:
        token = file.read()   
    return token

def login():                                                                                                                                  

    try:
        access_token = get_token()
    except:
        APP_ID = settings.APP_ID
        APP_SECRET = settings.APP_SECRET
        REDIRECT_URL = settings.REDIRECT_URL
        SCOPE = settings.SCOPE

        url = 'https://www.facebook.com/dialog/oauth?client_id=' + APP_ID + '&redirect_uri=' + REDIRECT_URL + '&scope=' + SCOPE
        print url
  
        code = raw_input('enter the code: ')
        code = code.split('&expire')[0]

        url2 = 'https://graph.facebook.com/v2.2/oauth/access_token?client_id=' + APP_ID + '&redirect_uri=' + REDIRECT_URL + '&client_secret=' + APP_SECRET + '&code=' + code
  
        r = requests.get(url2)
        if r.status_code != 200:
            raise Exception("Not success")
        access_token = r.text[13:]
  
        # store access token
        with open('token.txt', 'w') as file:
            file.write(access_token)

    return access_token

