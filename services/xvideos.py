import requests
import sys

nickname = sys.argv[1]

url = "https://www.xvideos.com/profiles/" + nickname

r = requests.get(url)
if (r.status_code == 200) or (r.status_code == 403):
    print(url)
else:
    sys.exit(1)
