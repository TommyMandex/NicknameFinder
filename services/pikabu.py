import requests
import sys

nickname = sys.argv[1]

url = "https://pikabu.ru/@" + nickname

headers = requests.utils.default_headers()
headers.update(
	{
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0;\ Windows NT 6.0)"
	}
)

r = requests.get(url,headers=headers)
if r.status_code == 200:
    print(url)
else:
    sys.exit(1)
