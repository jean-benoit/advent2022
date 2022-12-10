from collections import defaultdict

with open('input07.txt') as f:
    lines = f.read().splitlines()

fs = defaultdict(int)
path = ''
total = 0
for l in lines:
    if not l.startswith('$'):
        if not l.startswith('dir'):
            size = int(l.split(' ')[0])
            total += size
            p = path.split('/')
            for i in range(1,len(p)+1):
                fs['/'.join(p[:i])] += size
    elif l == '$ cd ..':
        path = '/'.join(path.split('/')[:-1])
    elif l.startswith('$ cd') and not l.startswith('$ cd /'):
        path += f'/{l[5:]}'

# part1
# 1792222
print(sum([s for s in fs.values() if s <= 100000]))

# part 2
# 1112963
print(min([s for s in fs.values() if s > total - 40000000]))