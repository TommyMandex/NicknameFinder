import requests
import sys

nickname = sys.argv[1]

url = "https://instagram.com/" + nickname

r = requests.get(url)
if r.status_code == 200:
    print(url)
else:
    sys.exit(1)
