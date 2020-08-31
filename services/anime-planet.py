import requests
import sys


nickname = sys.argv[1]

url = "https://anime-planet.com/users/" + nickname

r = requests.get(url)
if len(r.history) != 1:
    sys.exit(1)
else:
    print(url)
