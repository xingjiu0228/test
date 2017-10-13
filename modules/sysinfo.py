import sys
import socket
import uuid
import getpass  
import platform
import psutil


def get_mac_address(): 
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
    return "-".join([mac[e:e+2] for e in range(0,11,2)])


def run(**args):
    print "[*] In sysinfo module."
    host_name = platform.node()
    ip = socket.gethostbyname(socket.gethostname())
    mac = get_mac_address()
    user = getpass.getuser()
    os = str(platform.platform()) + ", " + str(platform.architecture()[0])
    path = sys.path[0]
    pc_mem =psutil.virtual_memory()
    info = "Host Name: " + host_name + "; " + "IP: " + ip + "; MAC: " + mac\
           + "; User: " + user + "; OS: " + os + "; Path: " + path + "; RAM: "\
           + str(pc_mem.available/1024/1024) + "/" + str(pc_mem.total/1024/1024) + " KB"
    return str(info)

print run()


