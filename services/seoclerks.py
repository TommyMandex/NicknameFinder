import requests
import sys


nickname = sys.argv[1]

url = "https://www.seoclerks.com/user/" + nickname

r = requests.get(url)
if r.history:
    sys.exit(1)
else:
    print(url)
