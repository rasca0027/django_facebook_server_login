from django.cong import settings
import facebook_login.utils
import requests
from facebookads.api import FacebookAdsApi
from facebookads import objects

my_app_id = settings.APP_ID
my_app_secret = settings.APP_SECRET
my_access_token = facebook_login.utils.get_token()

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
