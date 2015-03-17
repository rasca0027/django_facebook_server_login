import facebook_login.utils
from django.conf import settings
from facebookads import FacebookSession
from facebookads import FacebookAdsApi

def initialize():

    token = facebook_login.utils.login()

    session = FacebookSession(settings.APP_ID, settings.APP_SECRET, token)
    api = FacebookAdsApi(session)
    FacebookAdsApi.set_default_api(api)
    
