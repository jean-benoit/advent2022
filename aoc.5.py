import re

def readStacks(lines):
    stacks = [[] for i in range(9)]
    for line in [l[1::4] for l in lines[7::-1]]:
        for i, c in enumerate(line):
            if c != ' ':
                stacks[i].append(c)
    return stacks

def readMoves(lines):
    moves = []
    digits_re = re.compile(r'(\d+).*(\d+).*(\d+)')
    for l in lines[10:]:
        d0, d1, d2 = [int(d) for d in digits_re.search(l).groups()]
        moves.append([d0, d1-1, d2-1])
    return moves

with open('input05.txt') as f:
    lines = f.read().splitlines()
stacks = readStacks(lines)
moves = readMoves(lines)

## 5.1
def res_5_1():
    for m in moves:
        for i in range(m[0]):
            stacks[m[2]].append(stacks[m[1]].pop())
## 5.2
def res_5_2():
    for m in moves:
        load = stacks[m[1]][-m[0]:]
        stacks[m[1]] = stacks[m[1]][:-m[0]]
        stacks[m[2]] += load
res_5_2()


res = ''.join([s[-1] for s in stacks])
#QMBMJDFTD
#NBTVTJNFJ
print(res)