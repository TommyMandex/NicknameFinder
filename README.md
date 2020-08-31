# NicknameFinder
OSINT tool for search by nickname. These tool is designed to easily connect new services.

### Installation
```bash
git clone https://github.com/restanse/NicknameFinder.git
cd NicknameFinder
pip3 install -r requriments.txt
```

### Usage
```bash
python3 NicknameFinder.py username
```

### Add new services
You can easily add new services to search for a nickname. It is enough to add them to the `services` folder and check some rules: new script must get argument (`sys.argv[1]`) with nickname and if nickname at service found, then display the link to the profile, otherwise return 1 exit-code.
```python3
import sys, requests # and what you need

nickname = sys.argv[1] # get nickname from cli

#your code

if account_exist: # is there account with this nickname
    print("https://link.to.account/accs/nickname")
else: # there is no account
    sys.exit(1)
```
