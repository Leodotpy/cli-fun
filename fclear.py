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


# set sorrect console clear command
clear = getClearCMD()


# handler for if ctrl+c is pressed to exit loop
def handler(signum, frame):
    print("\n")
    quit()


# set handler
signal.signal(signal.SIGINT, handler)

# set terminal/disco floor board lenght and width
l = int(os.get_terminal_size()[1])  # terminal lines
w = int(os.get_terminal_size()[0])  # terminal columns

frame = 0
offsetBool = False
for i in range(max(l, w)):
    for k in range(min(l, w)):
        sys.stdout.write("\r\n" + f"{' '*i}/")
    

    
        
    # sys.stdout.write("\r" + str(ll))  # write board

    time.sleep(0.006)
    os.system(
        clear
    )  # clear terminal for new frame, "clear" is used for linux and "cls" for windows