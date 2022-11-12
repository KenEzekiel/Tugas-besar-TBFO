import pprint
import re

with open("./input.txt", 'r') as f:
    w = f.read()

with open("./terminals.txt", 'r') as a:
    terminals = a.read().split()
with open("./variables.txt", 'r') as b:
    non_terminals = b.read().split()
terminals.append(' ')
regex = "|".join(map(lambda x : "(" + x + ")", terminals))

iter = re.finditer(regex, w)
parsed = list(map(lambda x: x.group(0), iter))

print(parsed)
exit()
ret = re.findall(regex, w)

print(ret)
charbuffer = ""
parsed = []
for char in w:
    if char == " ":
        print("space")
        continue
    charbuffer += char
    if next(char) != " ":
        continue
    if charbuffer in terminals:
        parsed.append(charbuffer)
        charbuffer = ""
    print("c:", char)
    print("charbuf:", charbuffer)
    
print(parsed)