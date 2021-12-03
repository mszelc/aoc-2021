import sys
from copy import deepcopy

a = []
with open(sys.argv[1], 'r') as fh:
    for val in fh.readlines():
        a.append(val.strip())

b = list(a[0])
half = int(len(a)/2)
blen = len(a[0])
first = True
for val in a:
    if first:
        for i in range(0,blen):
            b[i] = int(b[i])
        first = False
        continue
    for i in range(0,blen):
        b[i] += int(val[i])

gstring = ''
estring = ''
for val in b:
    if val > half:
        gstring += '1'
        estring += '0'
    elif val < half:
        gstring += '0'
        estring += '1'
    else:
        gstring += '1'
        estring += '0'

print(int(gstring,2)*int(estring,2))

a1 = deepcopy(a)
a2 = deepcopy(a)
for i in range(0,blen):
    gbit = gstring[i]
    ebit = estring[i]
    for val in a:
        try:
            if val[i] != gbit:
                if len(a1) > 1:
                    a1.remove(val)
            if val[i] != ebit:
                if len(a2) > 1:
                    a2.remove(val)
        except ValueError:
            continue

print(int(a1[0],2)*int(a2[0],2))