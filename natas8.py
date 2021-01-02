import requests
import base64

level = str(8)
pw = "DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"

url = "http://natas"+level+".natas.labs.overthewire.org/index.php"


secret = "3d3d516343746d4d6d6c315669563362"
secret = bytes.fromhex(secret)
secret = secret[::-1]
secret = base64.decodebytes(secret)

print(secret)

data = (("secret", secret), ("submit", ""))

s = requests.Session()
s.auth = ('natas'+level, pw)

r = s.post(url, data=data)

print(r.text)



# W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl