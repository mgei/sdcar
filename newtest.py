import sys, tty, termios, time

def getch():
    fd = sys.stdin.fileno() # 0
    old_settings = termios.tcgetattr(fd)
    try:
        #tty.setraw(sys.stdin.fileno())
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

char = 'a'

while True:
    if(char == getch()):
        print("still the same")

    char = getch()
    print("just got it")

    if(char == ""):
        print("empty")
    if(char == "w"):
        print("you press w")
    if(char == "q"):
        print("exit now")
        break
