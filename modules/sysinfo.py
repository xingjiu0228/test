<<<<<<< HEAD
import os

def run(**args):
    print "[*] In sysinfo module."
    host_name = os.environ['COMPUTERNAME']
    return str(host_name)


=======
import os


host_name = os.environ['COMPUTERNAME']
>>>>>>> 8cea3f937d6c6ee8bc307d096b567a1d2ac754fe
