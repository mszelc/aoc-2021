import sys
from copy import deepcopy

def getCommons(a):
    b = list(a[0])
    half = float(len(a)/2)
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

    #print(int(gstring,2)*int(estring,2))
    return gstring, estring

a = []
with open(sys.argv[1], 'r') as fh:
    for val in fh.readlines():
        a.append(val.strip())

#a = ['00100',
#     '11110',
#     '10110',
#     '10111',
#     '10101',
#     '01111',
#     '00111',
#     '11100',
#     '10000',
#     '11001',
#     '00010',
#     '01010']

most, least = getCommons(a)
mc = most[0]
lc = least[0]
print(int(most,2)*int(least,2))

a1 = a2 = a
for i in range(0,len(most)):
    a1c = deepcopy(a1)
    a2c = deepcopy(a2)
    if len(a1) > 1:
        for val in a1:
            if val[i] != mc:
                if len(a1) > 1:
                    a1c.remove(val)
    if len(a2) > 1:
        for val in a2:
            if val[i] != lc:
                if len(a2) > 1:
                    a2c.remove(val)
    a1 = a1c
    a2 = a2c
    most, _ = getCommons(a1)
    _, least = getCommons(a2)
    try:
        mc = most[i+1]
        lc = least[i+1]
    except IndexError:
        break

print(int(a1[0],2)*int(a2[0],2))




