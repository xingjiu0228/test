import os

def run(**args):
    print "[*] In exec_cmd module."
    res = os.popen("netstat -ano").readlines()
    return str(res)
