import sys

a = []
with open(sys.argv[1], 'r') as fh:
    for val in fh.readlines():
        a.append(int(val))

count = 0
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        count += 1

print(count)

count = 0
pSum = sum(a[0:3])
for i in range(1, len(a)-2):
    nSum = sum(a[i:i+3])
    if nSum > pSum:
        count += 1
    pSum = nSum

print(count)
