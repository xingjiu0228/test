import os

def run(args):
    print "[*] In exec_cmd module."
    res = os.popen(args).readlines()
    return str(res)

print run("dir c:\\")
