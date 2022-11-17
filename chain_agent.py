from base64 import urlsafe_b64decode, urlsafe_b64encode
from ast import literal_eval
from encryption.utils import encrypt, decrypt
import requests

from nodep_py_server import WebRequest,Server
app = Server()


"""
a = Array of stations routes
b = current station
c = last request
d = last request method
e = last request form data or false
f = last requst json data or false
g = last request headers or false

"""
SECRET = None
USER_AGENT = None

@app.get('/favicon.ico')
def configure(request: WebRequest):
    global SECRET, USER_AGENT
    data = request.headers
    if not data.get('User-Agent'):
        print('here!')
        return request.send_error(404)
    USER_AGENT = data.get('User-Agent')
    SECRET = data.get('User-Agent') + data.get('Accept-Encoding')
    return request.raw_html_response(200,'<h1></h1>')


def configure_next_station(station: str):
    req = requests.get(station + '/favicon.ico', headers={'User-Agent': USER_AGENT})

@app.get('/')
def agent_route(request: WebRequest):
    data = request.query
    if any([not data.get('a'), not data.get('b'), not data.get('c'), not data.get('d'),
     not data.get('e'), not data.get('f'), not data.get('g')]) or not SECRET:
        print('here4')
        return request.send_error(status=404)
    a, b, c,d,e,f,g = data.values()

    a ,b, c = urlsafe_b64decode(a).decode(), urlsafe_b64decode(b).decode(), urlsafe_b64decode(c).decode()
    a, b, c = decrypt(a,SECRET), decrypt(b,SECRET), decrypt(c,SECRET)
    try:
        a = literal_eval(a)
    except Exception as e:
        print(e, 'here5')
        return request.send_error(status=404)
    if b not in a:
        print(e, 'here6')
        return request.send_error(status=404)
    if b == a[-1]:
        # if the current station is the last station in the array
        # do the final request and return the result
        d,e,f,g = urlsafe_b64decode(d).decode(), urlsafe_b64decode(e).decode(), urlsafe_b64decode(f).decode(), urlsafe_b64decode(g).decode()
        d,e,f,g = decrypt(d,SECRET), decrypt(e,SECRET), decrypt(f,SECRET), decrypt(g,SECRET)
        try:
            e,f,g = literal_eval(e),literal_eval(f),literal_eval(g)
        except Exception as e:
                    print(e,'7')
                    return request.send_error(status=404)
        method = d
        form_data = e
        json_data = f
        headers = g
        if len(method) == 3 and not method.startswith('P'):
            req = requests.get(c)
            return encrypt(f"{req.text}--@--{req.status_code}", SECRET)
        if form_data:
            if headers:
                req = getattr(requests,method)(data=form_data,headers=headers)
                return encrypt(f"{req.text}--@--{req.status_code}", SECRET)
            req = getattr(requests,method)(data=form_data)
            return encrypt(f"{req.text}--@--{req.status_code}", SECRET)
        if json_data:
            if headers:
                req = getattr(requests,method)(json=json_data,headers=headers)
                return encrypt(f"{req.text}--@--{req.status_code}", SECRET)
            req = getattr(requests,method)(json=json_data)
            return encrypt(f"{req.text}--@--{req.status_code}", SECRET)
        req = getattr(requests,method)(json=json_data)
        return encrypt(f"{req.text}--@--{req.status_code}", SECRET)

    next_station = None
    for index,station in enumerate(a):
        if station == b:
            next_station = a[index+1]
            #find the next station in the array
            break
    configure_next_station(next_station)
    req = requests.get(next_station, params={'a' : data.get('a'), 
    'b' : urlsafe_b64encode(encrypt(next_station,SECRET).encode()).decode(), 'c' : data.get('c'),'d' : d,'e' : e, 'f' : f, 'g' : g})
    return req.text
    

    
    #get next station

app.run('0.0.0.0', 8000)
    
    