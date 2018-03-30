lines = [". . ."]

from time import sleep
import sys

for line in lines:          # for each line of text (or each message)
    for c in line:          # for each character in each line
        print(c, end='')    # print a single character, and keep the cursor there.
        sys.stdout.flush()  # flush the buffer
        sleep(0.1)          # wait a little to make the effect look good.
    print('')              # line break (optional, could also be part of the message)
    sys.stdout.write("")
    sys.stdout.write("")
 
