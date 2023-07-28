# pip3 install cowsay

import cowsay
import sys

if len(sys.argv) == 2:
    # cowsay.cow(f"hello, ",sys.argv[1])
    cowsay.trex(f"hello ", sys.argv[1])
    