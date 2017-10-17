import win32gui
import win32ui
import win32con
import win32api

import PIL.Image


def bmp2jpg(bmp, jpg):
    PIL.Image.open(bmp).save(jpg)
    
def get_screenshot():
    hdesktop = win32gui.GetDesktopWindow()

    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)

    mem_dc = img_dc.CreateCompatibleDC()
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)

    mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)
    bmp = "C:\\Users\\test\\Desktop\\screenshot.bmp"
    screenshot.SaveBitmapFile(mem_dc, bmp)

    # bmp2jpg
    jpg = bmp[0:-4] + ".jpg"
    bmp2jpg(bmp, jpg);

    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())

    ff = open(jpg, "r")
    data = ff.read()
    return data


def run(**args):
    print "[*] In screenshot module."
    data = get_screenshot()
    #data = "done"
    return data
