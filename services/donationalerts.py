import sys
import requests

nickname = sys.argv[1]

url = "https://www.donationalerts.com/r/" + nickname

r = requests.get(url)
if r.status_code == 200:
    print(url)
else:
    sys.exit(1)
