from django.core.management.base import BaseCommand, CommandError
import facebook_login.utils

class Command(BaseCommand):
    
    help = 'Login and save access tokens for facebook'

    def handle(self, *args, **options):
        
        try:
            print facebook_login.utils.get_token()
        except:
            facebook_login.utils.login()
            

        

