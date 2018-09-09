from os import path, remove
import socket
import sys

def get_autoload_folder(username):
    return r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % username

def get_startup_file_name():
    return path.normpath(get_autoload_folder(socket.gethostname()) + '\\' + path.basename(module_path()))

def we_are_frozen():
    return hasattr(sys, "frozen")

def module_path():
    return sys.executable if we_are_frozen() else __file__

def managament_startup():
    startup_file = get_startup_file_name()
    if (path.exists(startup_file)):
        remove(startup_file)
    else:
        add_to_startup()

def add_to_startup():
    import getpass
    from shutil import copy

    file_path = module_path()
    
    try:
        autoload_folder_user = get_autoload_folder(getpass.getuser())
        copy(file_path, autoload_folder_user)
    except:
    	autoload_folder_host = get_autoload_folder(socket.gethostname())
    	copy(file_path, autoload_folder_host)

if __name__ == '__main__':
    managament_startup()