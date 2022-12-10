with open('input08.txt') as f:
    lines = f.read().splitlines()
SIZE = len(lines)
visible = 0

def is_visible(tree, i, j, i_incr, j_incr):
    while i > 0 and i < SIZE -1 and j > 0 and j < SIZE - 1:
        i += i_incr
        j += j_incr
        if int(lines[i][j]) >= tree:
            return False
    return True

for i in range(1, SIZE-1):
    for j in range(1, SIZE-1):
        tree = int(lines[i][j])
        if any([
            is_visible(tree, i, j, -1, 0),
            is_visible(tree, i, j, 1, 0),
            is_visible(tree, i, j, 0, -1),
            is_visible(tree, i, j, 0, 1),
        ]):
            visible +=1

print((SIZE*4-4) + visible)