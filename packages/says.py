import sys
from saying import hello, goodbye


if len(sys.argv) == 2:
    hello("jewel")
    goodbye("world")

