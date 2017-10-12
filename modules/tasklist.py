import ctypes
 
CreateToolhelp32Snapshot = ctypes.windll.kernel32.CreateToolhelp32Snapshot
Process32First = ctypes.windll.kernel32.Process32First
Process32Next = ctypes.windll.kernel32.Process32Next
CloseHandle = ctypes.windll.kernel32.CloseHandle


process_list = []

TH32CS_SNAPPROCESS = 0x00000002
class PROCESSENTRY32(ctypes.Structure):
     _fields_ = [("dwSize", ctypes.c_ulong),
                 ("cntUsage", ctypes.c_ulong),
                 ("th32ProcessID", ctypes.c_ulong),
                 ("th32DefaultHeapID", ctypes.c_ulong),
                 ("th32ModuleID", ctypes.c_ulong),
                 ("cntThreads", ctypes.c_ulong),
                 ("th32ParentProcessID", ctypes.c_ulong),
                 ("pcPriClassBase", ctypes.c_ulong),
                 ("dwFlags", ctypes.c_ulong),
                 ("szExeFile", ctypes.c_char * 260)]
                  
 
def get_process_info():
     h = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
     pe = PROCESSENTRY32()
     pe.dwSize = ctypes.sizeof(PROCESSENTRY32)
     if Process32First(h, ctypes.byref(pe)):
        while True:
            #yield pe.th32ProcessID, pe.szExeFile
            process_list.append("%4d: %s\r\n" % (pe.th32ProcessID, pe.szExeFile))
            if not Process32Next(h,  ctypes.byref(pe)):
                break
     CloseHandle(h)
    
def run(**args):
    print "[*] In tasklist module."
    get_process_info()
    return str(process_list)
