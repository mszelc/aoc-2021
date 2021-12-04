import sys
from pprint import pprint

def sumBoard(b, s):
    sum = 0
    for x in b:
        for y in x:
            if y not in s:
                sum += int(y)

    return sum

def checkBoard(b, s, sets):
    #print('Checking set {}'.format(s))
    #print('Board:')
    #pprint(b)
    ins = []
    for x in s:
        for i in range(0,len(b)):
            if x in b[i]:
                ins.append(5*i + b[i].index(x) + 1)
                continue

    sins = set(ins)
    for x in sets:
        if x.issubset(sins):
            return True

    return False


fh = open(sys.argv[1], 'r')
a =  fh.readlines()

sets = [set([1,2,3,4,5]),
        set([6,7,8,9,10]),
        set([11,12,13,14,15]),
        set([16,17,18,19,20]),
        set([21,22,23,24,25]),
        set([1,6,11,16,21]),
        set([2,7,12,17,22]),
        set([3,8,13,18,23]),
        set([4,9,14,19,24]),
        set([5,10,15,20,25])]
        #set([1,7,13,19,25]),
        #set([5,9,13,17,21])]

nums = a[0].split(',')
boards = {}
n = 0
boards['0'] = []
for val in a[2:]:
    if val == '\n':
        n += 1
        boards[str(n)] = []
    else:
        boards[str(n)].append([x for x in val.strip().split(' ') if x])

ans = 0
winners = {'b':[], 's':[], 'n':0}
board_iter = list(range(0,len(boards)))
for i in range(5,len(nums)):
    n = nums[:i]
    for j in board_iter:
        if checkBoard(boards[str(j)], n, sets):
            #ans = sumBoard(boards[str(j)], n)
            #print('{0} * {1} = {2}'.format( \
            #   n[-1],sumBoard(boards[str(j)],n),int(n[-1]) * sumBoard(boards[str(j)],n)))
            #break
            winners['b'] = boards[str(j)]
            winners['s'] = n
            winners['n'] += 1
            del[boards[str(j)]]
            del[board_iter[board_iter.index(j)]]
            print('Deleted board ' + str(j))
            if len(boards) < 1:
                ans = 1
                break
    if ans:
        break

b = winners['b']
s = winners['s']
ans = sumBoard(b,s)
print('{0} * {1} = {2}'.format( \
    s[-1],sumBoard(b,s),int(s[-1]) * sumBoard(b,s)))
