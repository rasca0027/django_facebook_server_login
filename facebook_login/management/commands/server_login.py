from django.core.management.base import BaseCommand, CommandError
import facebook_login.utils

class Command(BaseCommand):
    
    help = 'Login and save access tokens for facebook'

    def handle(self, *args, **options):
        
        facebook_login.utils.login()
            

        

