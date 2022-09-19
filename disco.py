# turn your terminal into a disco party

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
floorLength = int(os.get_terminal_size()[1])  # terminal lines
floorWidth = int(os.get_terminal_size()[0] / 2)  # terminal columns

frame = 0
offsetBool = False
while True:
    if frame % 5 == 0:
        frame = 0
        offsetBool += 1  # flip bool to offset the board from □ to ■

    ll = ""
    for l in range(floorLength):
        wl = ""
        for w in range(floorWidth):
            if (((w + l + int(offsetBool)) % 2)) == 0:
                # random color from "\033[90m" to "\033[97m"
                wl += (
                    f"\033[9{str(random.randint(0, 7))}m" + "~~" + "\033[0m"
                    # f"\x1b[6;30;4{str(random.randint(0, 7))}m" + "■ " + "\x1b[0m"
                )  # print even tile ("\033[0m" ends color code)
            else:
                wl += (
                    # f"\033[9{str(random.randint(0, 7))}m" + "■ " + "\033[0m"
                    f"\x1b[6;30;4{str(random.randint(1, 7))}m" + "  " + "\x1b[0m"
                )  # print odd tile

        ll += "\n" + wl
    sys.stdout.write("\r" + str(ll))  # write board

    time.sleep(0.2)
    frame += 1
    os.system(
        clear
    )  # clear terminal for new frame, "clear" is used for linux and "cls" for windows