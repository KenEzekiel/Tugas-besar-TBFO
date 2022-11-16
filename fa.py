import re


def tokenize_with_fa(code: str, terminals: list[str]):
    terminals = terminals[::]
    terminals.remove('variable')
    terminals.remove('mathexp')
    terminals.remove('comment')
    terminals.remove('newline')
    terminals.remove(r'\w')

    # make javascript variable regex
    res = code
    offset = 0
    iter = re.finditer(
        f'(?:^|[^a-zA-Z_$0-9])([a-zA-Z_$0-9]+)', code)
    for match in iter:
        var_str = match.group(1)
        if re.match(r'[0-9][^0-9]+', var_str):
            raise Exception('Invalid variable name')

        if var_str not in terminals:
            res = res[:match.start(1) + offset] + \
                'variable' + res[match.end(1) + offset:]
            offset += len('variable') - len(var_str)
    return res
    # return inside function
    # # get all return statement
    # returns = re.findall(r'return', code)
    # print(returns)
    # # return inside function
    # returns_valid = re.findall(
    #     r'function\s*\w\s*\([\w\W]*\)\s*{[\w\W]*return[\s]*[\w\W]*}', code)
    # print(returns_valid)
    # if len(returns) != len(returns_valid):
    #     return False
    # return True
