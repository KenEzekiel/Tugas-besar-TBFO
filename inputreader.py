import re

# list of place that space is obligatory
space_reg = r'((?:return)|(?:var)|(?:let)|(?:const)|(?:delete)|(?:function)|(?:case))(?:\s+)((?:[({\[]*\s*variable)|(?:[({\[]*\s*number))'


def preprocessing(w: str):
    # between else if, space is also obligatory
    w = re.sub(r"else\s+if", "elsexxif", w)

    # change obligatory spaces by xx
    w = re.sub(space_reg, r'\1xx\2', w)

    # remove all non-obligatory spaces
    w = re.sub(r'\s+', '', w)

    # change xx back to space
    w = w.replace('xx', ' ')

    return w


def inputread(w: str, terminals: list):
    # regex of terminals
    regex = "|".join(map(lambda x: "(" + x + ")", terminals))

    # get all terminals match in word
    iter = re.finditer(regex, w)

    # list of word terminals
    parsed = list(map(lambda x: x.group(0), iter))

    return parsed
