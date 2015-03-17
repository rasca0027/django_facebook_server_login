# django_facebook_server_login
A Djaingo app for facebook server side login

## Installation
```
git clone https://github.com/ramusus/django-facebook-api.git
cd django_facebook_server_login
python setup.py install
```

Add to settings.py:
```
# facebook_login configures
APP_ID = ''
APP_SECRET = ''
REDIRECT_URL = ''
SCOPE = '' # example: ads_management,...
```

Add to `urls.py` in your project:
```
urlpatterns = patterns('',
    ...
    url(r'^server_login/', include('facebook_login.urls'))
)
```

## Usage

Command:
```
>>> python manage.py server_login
```

Or:
```
>>> import facebook_login
>>> facebook_login.utils.login()
```

Using web browser:
go to `your_host/server_login/login/` to login
and `your_host/server_login/login_success/` to finish login
or `your_host/<pre-fix>/login_success/`,
or whatever pre-fix you define in urls.py

## Get token

```
>>> import facebook_login
>>> facebook_login.utils.get_token()
```

## Use with facebook api

```
>>> import facebook_login
>>> facebook_login.initialize()
```


