import requests
from base64 import urlsafe_b64encode
from encryption.utils import encrypt, decrypt
from random import randrange

ROUTE_ARRAY = ['http://127.0.0.1:8000', 'http://127.0.0.1:8001', 'http://127.0.0.1:8002']
FIRST_ROUTE = ROUTE_ARRAY[0]
PROXY_URI = "http://127.0.0.1:8000/?a={}&b={}&c={}&d={}&e={}&f={}&g={}"

IS_SECRET_CONFIGURED = False
SECRET = None


def configure_secret():
    global SECRET, IS_SECRET_CONFIGURED
    base_secret = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/534.{}{} (KHTML, like Gecko) Chrome/10{}.0.0.0 Safari/534.{}{}'
    num1, num2 = randrange(1, 9), randrange(1, 9)
    num3 = randrange(1, 9)
    SECRET = base_secret.format(num1, num2, num3, num1, num2) 
    IS_SECRET_CONFIGURED = True


def make_post_request(url: str,is_form, is_json, extra_headers: dict) -> str:
    url = urlsafe_b64encode(encrypt(url, SECRET).encode()).decode()
    if is_form:
        is_form = urlsafe_b64encode(encrypt(str(is_form), SECRET).encode()).decode()
    else:
        is_form = urlsafe_b64encode(encrypt("False", SECRET).encode()).decode()
    if is_json:
        is_json = urlsafe_b64encode(encrypt(str(is_json), SECRET).encode()).decode() 
    else:
        is_json = urlsafe_b64encode(encrypt("False", SECRET).encode()).decode() 
    extra_headers = urlsafe_b64encode(encrypt(str(extra_headers), SECRET).encode()).decode()
    routes = urlsafe_b64encode(encrypt(str(ROUTE_ARRAY), SECRET).encode()).decode()
    method =  urlsafe_b64encode(
                                     encrypt('POST', SECRET).encode()).decode()
    first_route = urlsafe_b64encode(
                                     encrypt(FIRST_ROUTE, SECRET).encode()).decode()
    proxy_url = PROXY_URI.format(routes,
                                first_route, url,
                                method,
                                is_form,
                                is_json,
                              extra_headers
    )
    return proxy_url


def make_get_request(url: str,extra_headers: dict=None) -> str:
    url = urlsafe_b64encode(encrypt(url, SECRET).encode()).decode()
    is_form = urlsafe_b64encode(
                                     encrypt('False', SECRET).encode()).decode()
    is_json = urlsafe_b64encode(
                                     encrypt('False', SECRET).encode()).decode()
    if extra_headers:
        extra_headers = urlsafe_b64encode(encrypt(str(extra_headers), SECRET).encode()).decode()
    else:
        extra_headers = urlsafe_b64encode(
                                     encrypt('False', SECRET).encode()).decode()
    routes = urlsafe_b64encode(encrypt(str(ROUTE_ARRAY), SECRET).encode()).decode()
    method =  urlsafe_b64encode(
                                     encrypt('GET', SECRET).encode()).decode()
    first_route = urlsafe_b64encode(
                                     encrypt(FIRST_ROUTE, SECRET).encode()).decode()
    proxy_url = PROXY_URI.format(routes,
                                first_route, url,
                                method,
                                is_form,
                                is_json,
                              extra_headers
    )
    return proxy_url
while True:
    if not IS_SECRET_CONFIGURED:
        print('[*] Configuring Secret')
        configure_secret()
        req = requests.get(FIRST_ROUTE + '/favicon.ico',
                           headers={'User-Agent': SECRET})
        if req.status_code != 200:
            print('[*] Something went wrong configure_secret, %s', req.status_code)
        SECRET += "gzip, deflate, br"
    url = input('enter url: \n').strip()
    method = input('Enter Method: \n').strip().lower()
    if method == 'get':
        proxy_url = make_get_request(url)                             
        req = requests.get(proxy_url)
        if req.status_code == 200:
            print(decrypt(req.text, SECRET))
   # print(req.text)
