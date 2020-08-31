import os
import sys
import subprocess

nickname = sys.argv[1]

listdir = os.listdir("services/") #ls dir with scripts

for filename in listdir:
    try:
        output = subprocess.check_output("python3 services/{0} {1}".format(filename,nickname), universal_newlines=True, shell=True)
        output = output[0:len(output)-1] #remove \n
        print("[{0}] found: {1}".format(filename[0:len(filename)-3], output))
    except subprocess.CalledProcessError: #if exit-code non-zero
        print("[{0}] not found".format(filename[0:len(filename)-3]))
