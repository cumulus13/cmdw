
# stdin handle is -10
# stdout handle is -11
# stderr handle is -12
from __future__ import print_function
import sys
import os

def getSize():
    if sys.platform == 'win32':
        from ctypes import windll, create_string_buffer
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
    
        if res:
            import struct
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
        else:
            sizex, sizey = 80, 25 # can't determine actual size - return default values
    else:
        sizex = 0
        sizey = 0
        data = os.popen('stty size', 'r').read().split()
        if len(data) == 2:
            sizex, sizey = data
        else:
            if not data:
                sizex = sizey = 0
            else:
                sizex = data
        sizex = int(sizex)
        sizey = int(sizey)
    return sizex, sizey
    # print sizex, sizey

def getWidth():
    return getSize()[0]

def getHeight():
    return getSize()[1]

def getTerminalSize():
    import platform
    current_os = platform.system()
    tuple_xy=None
    if current_os == 'Windows':
        tuple_xy = _getTerminalSize_windows()
        if tuple_xy is None:
            tuple_xy = _getTerminalSize_tput()
            # needed for window's python in cygwin's xterm!
        if current_os == 'Linux' or current_os == 'Darwin' or  current_os.startswith('CYGWIN'):
            tuple_xy = _getTerminalSize_linux()
        if tuple_xy is None:
            print("default")
            tuple_xy = (80, 25)      # default value
        return tuple_xy
    
def _getTerminalSize_windows():
    res=None
    try:
        from ctypes import windll, create_string_buffer

        # stdin handle is -10
        # stdout handle is -11
        # stderr handle is -12

        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
    except:
        return None
    if res:
        import struct
        (bufx, bufy, curx, cury, wattr,
                             left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
        sizex = right - left + 1
        sizey = bottom - top + 1
        return sizex, sizey
    else:
        return None
    
def _getTerminalSize_tput():
    # get terminal width
    # src: http://stackoverflow.com/questions/263890/how-do-i-find-the-width-height-of-a-terminal-window
    try:
        import subprocess
        proc=subprocess.Popen(["tput", "cols"],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        output=proc.communicate(input=None)
        cols=int(output[0])
        proc=subprocess.Popen(["tput", "lines"],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        output=proc.communicate(input=None)
        rows=int(output[0])
        return (cols,rows)
    except:
        return None        

def _getTerminalSize_linux():
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,'1234'))
        except:
            return None
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (env['LINES'], env['COLUMNS'])
        except:
            return None
    return int(cr[1]), int(cr[0])

if __name__ == "__main__":
    sizex,sizey=getTerminalSize()
    print('width =',sizex,'height =',sizey)
        
#if __name__ == '__main__':
    #print getSize()
    #sizex = getWidth()
    #print "_"*int(sizex)
