# turn your terminal into a disco party

import random
import time
import sys
import os
import signal


class effects:

    UNDERLINE = "\033[4m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"


# handler for if ctrl+c is pressed to exit loop
def handler(signum, frame):
    print("\n")
    quit()


signal.signal(signal.SIGINT, handler)

floorLength = 12
floorWidth = 16

frame = 0
offsetBool = False
while True:
    if frame%5 == 0:
        frame = 0
        offsetBool+=1
    
    ll = ""
    for l in range(floorLength):
        wl = ""
        for w in range(floorWidth):
            if (((w+l+int(offsetBool))%2))==0:
                # random color from "\033[90m" to "\033[97m"
                wl += f"\033[9{str(random.randint(0, 7))}m" + "□ " + effects.ENDC # print even tile
            else:
                wl += f"\033[9{str(random.randint(0, 7))}m" + "■ " + effects.ENDC # print odd tile

        ll += "\n" + wl
    sys.stdout.write("\r" + str(ll))

    time.sleep(0.2)
    frame+=1
    os.system("clear") # clear terminal for new frame Ubuntu; use "cls" for windows
