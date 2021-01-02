import base64
import requests

url = "http://natas11.natas.labs.overthewire.org"
cipher = b"ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw="
cipher = base64.decodebytes(cipher)

key = b"qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw"
cookie_payload = b"{\"showpassword\":\"yes\",\"bgcolor\":\"#ffffff\"}"

print(cookie_payload)


def xor_encrypt(key, cookie):
    data = ""
    for x in range(len(key)):
        data += str(chr(cookie[x] ^ key[x % len(key)]))

    data = base64.encodebytes(data.encode('utf-8'))
    return data


encoded_cookie_payload = xor_encrypt(key, cookie_payload)

print(encoded_cookie_payload.decode("UTF-8"))

s = requests.Session()
s.auth = ('natas11', 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK')
s.cookies['data'] = encoded_cookie_payload.decode("UTF-8").rstrip()
r = s.get(url)

print(r.text)

# input für loadData = ("showpassword"=>"no", "bgcolor"=>"#ffffff")
# guckt ob wir cookie mit key 'data' mitgesendet haben
# falls ja, wird $tempdata = json_decode(xor_encrypt(base64_decode(cookie))
# tempdata muss array sein [showpassword="yes",bgcolor="#ffffff"]
# cookie: {"data":{{showpassword:"yes"},{bgcolor="#ffffff"}}}
