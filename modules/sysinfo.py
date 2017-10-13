import os

def run(**args):
    print "[*] In sysinfo module."
    host_name = os.environ['COMPUTERNAME']
    return str(host_name)


