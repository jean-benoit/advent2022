with open('input08.txt') as f:
    lines = f.read().splitlines()
SIZE = len(lines)

def visible_trees(tree, i, j, i_incr, j_incr):
    score = 0
    while i > 0 and i < SIZE -1 and j > 0 and j < SIZE - 1:
        i += i_incr
        j += j_incr
        score +=1
        if int(lines[i][j]) >= tree:
            return score
    return score

max_score = 0
for i in range(1, SIZE-1):
    for j in range(1, SIZE-1):
        tree = int(lines[i][j])
        score = (
            visible_trees(tree, i, j, -1, 0) *
            visible_trees(tree, i, j, 1, 0) *
            visible_trees(tree, i, j, 0, -1) *
            visible_trees(tree, i, j, 0, 1)
        )
        max_score = max(score, max_score)

print(max_score)