import requests

url = 'http://127.0.0.1:8080/WebGoat'
url1 = 'http://127.0.0.1:8080/WebGoat/start.mvc'
headers = headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36'
}
payload = dict(username='guest', password='guest')
s = requests.Session()
s.get(url)
s.post(url + "/j_spring_security_check;jsessionid=" + s.cookies.get('JSESSIONID'),data=payload, headers = headers)
r = s.get(url1)
print r.content
print "Halleluiah!!!"


