import operator

with open('_input09.txt') as f:
    lines = f.read().splitlines()

lines = lines[:2]

DIRECTIONS = {'U':[+1,0], 'D':[-1,0], 'L':[0,-1], 'R':[0,1]}
GT = operator.gt
LT = operator.lt

nodes = [[5,11] for i in range(10)]
tail_positions = set(['5x11'])

def move(direct):
    x, y = DIRECTIONS[direct] 
    nodes[0][0] += x
    nodes[0][1] += y
    pull_next_node(0, direct)
    print_map()
    print('')

# def axial_check(a, b, incr, index):
#     alt_index = int(not index)
#     op = GT if incr > 0 else LT
#     if op(b[index], a[index] + incr):
#         b[index] = a[index] + incr
#         b[alt_index] = a[alt_index]
#         return True
#     return False

def pull_next_node(index, dir):
    aa = nodes[index]
    bb = nodes[index+1]
    moved = False
    if dir == 'U':
        if bb[0] < aa[0] - 1:
            bb[0] = aa[0] - 1
            bb[1] = aa[1]
            moved = True
    if dir == 'D':
        if bb[0] > aa[0] + 1:
            bb[0] = aa[0] + 1
            bb[1] = aa[1]
            moved = True
    if dir == 'L':
        if bb[1] > aa[1] + 1:
            bb[1] = aa[1] + 1
            bb[0] = aa[0]
            moved = True
    if dir == 'R':
        if bb[1] < aa[1] - 1:
            bb[1] = aa[1] - 1
            bb[0] = aa[0]
            moved = True

    # checks = [
    #     axial_check(aa, bb, -1, 0),
    #     axial_check(aa, bb, +1, 0),
    #     axial_check(aa, bb, -1, 1),
    #     axial_check(aa, bb, +1, 1),
    # ]
    if moved:
        if index == len(nodes)-2 :
            tail_positions.add(f'{bb[0]}x{bb[1]}')
        if index<len(nodes)-2:
            pull_next_node(index+1,dir)

def print_map():
    mtx = [['.']*26 for i in range(21)]
    for i in range(len(nodes))[::-1]:
        mtx[nodes[i][0]][nodes[i][1]] = str(i)
    for l in mtx[::-1]:
        print(''.join(l))

print_map()

for l in lines:
    dir, quant = l.split(' ')
    print(f'=== {l}')
    for i in range(int(quant)):
        move(dir)
    # print_map()

# < 9854
# > 2559
# < 3332
print(len(list(tail_positions)))