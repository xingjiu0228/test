import os

def run(**args):
    print "[*] In exec_cmd module."
    res = os.popen(r"dir c:\").readlines()
    return str(res)

print run()
