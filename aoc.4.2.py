with open('input04.txt') as f:
    lines = f.read().splitlines()

res = 0

for l in lines:
    a, b, c, d = [int(i) for i in '-'.join(l.split(',')).split('-')]
    s0, s1 = set(range(a,b+1)), set(range(c,d+1))
    if s0 & s1:
        res += 1

# 914
print(res)
