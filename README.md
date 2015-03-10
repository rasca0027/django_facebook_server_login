# django_facebook_server_login
A Djaingo app for facebook server side login

## Installation
```
git clone https://github.com/ramusus/django-facebook-api.git
python setup.py install
```

Add to settings.py:
```
# facebook_login configures
APP_ID = ''
APP_SECRET = ''
REDIRECT_URL = ''
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
and `your_host/server_login/login_success/` to finish
or just edit the `urls.py`, of course.

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


