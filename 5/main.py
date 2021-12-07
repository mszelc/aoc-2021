import sys
from pprint import pprint

def sortLine(a):
    line = a.split(' -> ')
    [p1, p2] = [x.split(',') for x in line]
    v = h = None
    if int(p1[0]) == int(p2[0]):
        y = sorted([int(p1[1]),int(p2[1])])
        v = {'const': int(p1[0]),'start': y[0], 'end': y[1]}
    elif int(p1[1]) == int(p2[1]):
        x = sorted([int(p1[0]),int(p2[0])])
        h = {'const': int(p1[1]), 'start': x[0], 'end': x[1]}
    else:
        #print("Skipping line {}".format(a))
        return None, None

    return h, v

fh = open(sys.argv[1], 'r')
a =  fh.readlines()

hs = []
vs = []
for val in a:
    h,v = sortLine(val)
    if h:
        hs.append(h)
    if v:
        vs.append(v)


hs = sorted(hs, key=lambda y: y['const'])
vs = sorted(vs, key=lambda x: x['const'])

intersects = []

for hLine in hs:
    for vLine in vs:
        if vLine['start'] <= hLine['const'] <= vLine['end'] and hLine['start'] <= vLine['const'] <= hLine['end']:
            if (vLine['const'],hLine['const']) not in intersects:
                intersects.append((vLine['const'],hLine['const']))

#pprint(intersects)

for i in range(0,len(hs)-1):
    if hs[i]['const'] == hs[i+1]['const']:
        if hs[i+1]['start'] <= hs[i]['end'] <= hs[i+1]['end']:
            if hs[i]['start'] <= hs[i+1]['start']:
                for x in range(hs[i+1]['start'],hs[i]['end']+1):
                    if (x,hs[i]['const']) not in intersects:
                        intersects.append((x,hs[i]['const']))
            else:
                for x in range(hs[i]['start'],hs[i]['end']+1):
                    if (x,hs[i]['const']) not in intersects:
                        intersects.append((x,hs[i]['const']))
        elif hs[i]['start'] <= hs[i+1]['end'] <= hs[i]['end']:
            if hs[i+1]['start'] <= hs[i]['start']:
                for x in range(hs[i]['start'],hs[i+1]['end']+1):
                    if (x,hs[i]['const']) not in intersects:
                        intersects.append((x,hs[i]['const']))
            else:
                for x in range(hs[i+1]['start'],hs[i+1]['end']+1):
                    if (x,hs[i]['const']) not in intersects:
                        intersects.append((x,hs[i]['const']))

for i in range(0,len(vs)-1):
    if vs[i]['const'] == vs[i+1]['const']:
        if vs[i+1]['start'] <= vs[i]['end'] <= vs[i+1]['end']:
            if vs[i]['start'] <= vs[i+1]['start']:
                for y in range(vs[i+1]['start'],vs[i]['end']+1):
                    if (vs[i]['const'],y) not in intersects:
                        intersects.append((vs[i]['const'],y))
            else:
                for y in range(vs[i]['start'],vs[i]['end']+1):
                    if (vs[i]['const'],y) not in intersects:
                        intersects.append((vs[i]['const'],y))
        elif vs[i]['start'] <= vs[i+1]['end'] <= vs[i]['end']:
            if vs[i+1]['start'] <= vs[i]['start']:
                for y in range(vs[i]['start'],vs[i+1]['end']+1):
                    if (vs[i]['const'],y) not in intersects:
                        intersects.append((vs[i]['const'],y))
            else:
                for y in range(vs[i+1]['start'],vs[i+1]['end']+1):
                    if (vs[i]['const'],y) not in intersects:
                        intersects.append((vs[i]['const'],y))

pprint(intersects)
print(len(intersects))