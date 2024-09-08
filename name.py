import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("I love you, " + sys.argv[1])
