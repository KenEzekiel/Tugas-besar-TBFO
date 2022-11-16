import pprint
import re


space_reg = r'((?:return)|(?:var)|(?:let)|(?:const)|(?:delete)|(?:function)|(?:case))(?:\s+)((?:variable)|(?:mathexp))'


def preprocessing(w: str):
    w = re.sub(r"else\s+if", "elsexxif", w)
    w = re.sub(space_reg, r'\1xx\2', w)
    w = re.sub(r'comment\n', 'commentwww', w)
    w = re.sub(r'\s+', '', w)
    w = w.replace('xx', ' ')
    w = w.replace('www', '\n')

    return w


def inputread(w: str, terminals: list):
    # if re.match(r"^\s*$", w):
    #     return [" "]

    regex = "|".join(map(lambda x: "(" + x + ")", terminals))

    iter = re.finditer(regex, w)
    parsed = list(map(lambda x: x.group(0), iter))

    # print(parsed)
    return parsed
