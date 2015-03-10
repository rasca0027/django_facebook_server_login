import facebook_login.utils
from django.conf import settings
from facebookads import FacebookSession
from facebookads import FacebookAdsApi

def set_api():
    try:
        token = facebook_login.utils.get_token()
    except:
        print "Please login first. Type `python manage.py server_login` to login."

    session = FacebookSession(settings.APP_ID, settings.APP_SECRET, token)
    api = FacebookAdsApi(session)
    FacebookAdsApi.set_default_api(api)
    
