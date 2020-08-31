import requests
import sys


nickname = sys.argv[1]

url = "https://gitlab.com/" + nickname

r = requests.get(url)
if r.history: # if redirect
    sys.exit(1)
else:
    print(url)
