import os

def run(**args):
    print "[*] In exec_cmd module."
    res = os.popen("dir").readlines()
    return str(res)
