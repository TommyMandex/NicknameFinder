import os
#import requests
import subprocess

nickname = input("enter nickname: ")

listdir = os.listdir("services/")

for filename in listdir:
    try:
        output = subprocess.check_output("python3 services/{0} {1}".format(filename,nickname), universal_newlines=True, shell=True)
        output = output[0:len(output)-1]
        print("[{0}] found: {1}".format(filename[0:len(filename)-3], output))
    except subprocess.CalledProcessError:
        print("[{0}] not found".format(filename[0:len(filename)-3]))
