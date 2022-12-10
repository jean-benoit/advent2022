from collections import defaultdict

with open('input07.txt') as f:
    lines = f.read().splitlines()

fs = defaultdict(int)
path = ''
for l in lines:
    if not l.startswith('$'):
        if not l.startswith('dir'):
            p = path.split('/')
            while p:
                fs['/'.join(p)] += int(l.split(' ')[0])
                p.pop()
    elif l == '$ cd ..':
        path = '/'.join(path.split('/')[:-1])
    elif l.startswith('$ cd') and not l.startswith('$ cd /'):
        path += f'/{l[5:]}'

# 1792222
print(sum([s for s in fs.values() if s <= 100000]))