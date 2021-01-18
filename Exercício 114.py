import urllib
import urllib.request

try:
    online = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    ('O site não está online')
else:
    print ('O site está online')
