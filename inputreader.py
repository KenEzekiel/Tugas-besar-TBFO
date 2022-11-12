import pprint
import re


with open("./terminals.txt", 'r') as a:
    terminals = a.read().split()
with open("./variables.txt", 'r') as b:
    non_terminals = b.read().split()

space_reg = r'((?:return)|(?:var)|(?:let)|(?:const)|(?:delete)|(?:function)|(?:case))(?:\s+)((?:variable)|(?:mathexp))'


def inputread(filename):
    with open("./" + filename, 'r') as f:
        w = f.read()
    if re.match(r"^\s*$", w):
        return [" "]

    # preprocessing
    w = re.sub(r"else\s+if", "elsexxif", w)
    w = re.sub(space_reg, r'\1xx\2', w)
    w = re.sub(r'comment\n', 'commentwww', w)
    w = re.sub(r'\s+', '', w)
    w = w.replace('xx', ' ')
    w = w.replace('www', '\n')

    terminals.append(' ')
    terminals.append(r'\n')
    regex = "|".join(map(lambda x: "(" + x + ")", terminals))
    w = re.sub(r'[ \t]+', ' ', w)

    iter = re.finditer(regex, w)
    parsed = list(map(lambda x: x.group(0), iter))

    # print(parsed)

    new_parsed = []
    for i in parsed:
        if i == " ":
            i = "space"
        new_parsed.append(i)

    # print(new_parsed)

    return parsed
