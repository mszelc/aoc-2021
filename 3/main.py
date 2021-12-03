import sys

a = []
with open(sys.argv[1], 'r') as fh:
    for val in fh.readlines():
        a.append(val.strip())
