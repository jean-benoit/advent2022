with open('input09.txt') as f:
    lines = f.read().splitlines()

DIRECTIONS = {'U':[-1,0], 'D':[1,0], 'L':[0,-1], 'R':[0,1]}
tail = [0,0]
head = [0,0]
tail_positions = set(['0x0'])

def move(direct):
    x, y = DIRECTIONS[direct] 
    head[0] += x
    head[1] += y
    if abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1 :
        tail[0] = head[0] - x
        tail[1] = head[1] - y
    tail_positions.add(f'{tail[0]}x{tail[1]}')

for l in lines:
    dir, quant = l.split(' ')
    for i in range(int(quant)):
        move(dir)

print(len(list(tail_positions)))  # 6018