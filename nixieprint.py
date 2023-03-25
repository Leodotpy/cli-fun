import random
import sys
import argparse

nixie_tube_digits = {
    0: """ _ 
| |
|_|""",
    1: """   
  |
  |""",
    2: """ _ 
 _|
|_ """,
    3: """ _ 
 _|
 _|""",
    4: """   
|_|
  |""",
    5: """ _ 
|_ 
 _|""",
    6: """ _ 
|_ 
|_|""",
    7: """ _ 
  |
  |""",
    8: """ _ 
|_|
|_|""",
    9: """ _ 
|_|
 _|""",

    "DOT": """   
   
  ."""
}


parser = argparse.ArgumentParser(description='Process some input.')
parser.add_argument('-w', '--hacktogate', action='store_true', help='worldline')
args = parser.parse_args()

if args.hacktogate:
    print("\033[38;2;255;100;0mWORLDLINE:\033[0m")
    prompt = str(format(random.uniform(0, 1.999999), '.6f'))

else:
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
    else:
        try:
            prompt = input("Enter input (only decimals and ints allowed): ")
        except KeyboardInterrupt:
            print("\n")
            quit()

# validate prompt
for i in prompt:
    if i not in ".0123456789":
        print(f"Invalid char: '{i}'")
        quit()

for i in range(len(nixie_tube_digits[1].splitlines())):
    l = ""
    for x in list(prompt):
        if x == ".":
            l += nixie_tube_digits["DOT"].splitlines()[i]
        else:
            l += nixie_tube_digits[int(x)].splitlines()[i]

    print(f"\033[38;2;255;100;0m{l}\033[0m")
