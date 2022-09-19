# an animated clear command

import random
import time
import sys
import os
import signal


def getClearCMD():
    # for windows
    if os.name == "nt":
        return "cls"

    # for mac and linux(here, os.name is 'posix')
    else:
        return "clear"


# set correct console clear command
clear = getClearCMD()


# handler for if ctrl+c is pressed to exit loop
def handler(signum, frame):
    print("\n")
    quit()


# set handler
signal.signal(signal.SIGINT, handler)

l = int(os.get_terminal_size()[1])  # terminal lines
w = int(os.get_terminal_size()[0])  # terminal columns

for i in range(max(l, w)+min(l,w)):
    for k in range(min(l, w)):
        if i-k > 0 and i-k <= max(l,w):
            sys.stdout.write("\r\n" + f"{' '*(i-k)}\033[94m{'/'*14}\033[0m")
            
    time.sleep(0.001)
    os.system(
        clear
    )  # clear terminal for new frame, "clear" is used for linux and "cls" for windows