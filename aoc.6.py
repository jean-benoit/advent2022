with open('input06.txt') as f:
    data = f.read()
PATTERN_LENGTH = 4
for i in range(PATTERN_LENGTH,len(data)+1):
    if len(set(data[i-PATTERN_LENGTH:i])) == PATTERN_LENGTH:
        print(i) # 1262, 3444
        break