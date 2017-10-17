import os

def run(**args):
    print "[*] In exec_cmd module."
    res = os.popen(args[0]).readlines()
    return str(res)
