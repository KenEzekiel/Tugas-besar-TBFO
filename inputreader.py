import pprint
import re



with open("./terminals.txt", 'r') as a:
    terminals = a.read().split()
with open("./variables.txt", 'r') as b:
    non_terminals = b.read().split()

def inputread (filename):
    with open("./" + filename, 'r') as f:
        w = f.read()
    terminals.append(' ')
    regex = "|".join(map(lambda x : "(" + x + ")", terminals))

    iter = re.finditer(regex, w)
    parsed = list(map(lambda x: x.group(0), iter))

    print(parsed)
    new_parsed = []
    for i in parsed:
        if i == " ":
            i = "space"
        new_parsed.append(i)
    
    # print(new_parsed)

    return parsed