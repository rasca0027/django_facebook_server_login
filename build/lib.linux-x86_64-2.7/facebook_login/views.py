from django.http import HttpResponse
import facebook_login.utils
from django.http import HttpResponseRedirect
from django.conf import settings
import requests

APP_ID = settings.APP_ID
APP_SECRET = settings.APP_SECRET
REDIRECT_URL = settings.REDIRECT_URL

def login(request):
    try:
        output = get_token()
        return HttpResponse(output)
    except:
        url = 'https://www.facebook.com/dialog/oauth?client_id=' + APP_ID + '&redirect_uri=' + REDIRECT_URL + '&scope=ads_management'
        response = HttpResponseRedirect(url)
        
        return response

def login_success(request):

    code = request.GET['code']
    url = 'https://graph.facebook.com/v2.2/oauth/access_token?client_id=' + APP_ID + '&redirect_uri=' + REDIRECT_URL + '&client_secret=' + APP_SECRET + '&code=' + code
    
    r = requests.get(url)
    access_token = r.text[13:]

    with open('token.txt', 'w') as file:
        file.write(access_token)

    return HttpResponse(access_token)


