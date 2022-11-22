import re


def process_string(code: str, symbol: str, multiline = False):
    res = code
    iter = re.finditer(f'({symbol}[^${symbol}]*{symbol})', res)

    offset = 0
    for match in iter:
        string: str = match.group(0)
        if not multiline and '\n' in string:
            raise Exception('Invalid string')
        res = res[:match.start() + offset] + \
                '1' + res[match.end() + offset:]
        offset += 1 - len(string)

def tokenize_with_fa(code: str, terminals: list[str]):
    terminals = terminals[::]
    terminals.remove('variable')
    terminals.remove('mathexp')
    terminals.remove('comment')
    terminals.remove('newline')
    terminals.remove(r'\w')

    res = code

    # Process one line string
    res = process_string(res, '`', True)
    res = process_string(res, '"')
    res = process_string(res, "'")

    print(res)


    if '"' in res or "'" in res:
        raise Exception('Invalid string')

    
    iter = re.finditer(r'([0-9]+\.)|(\.[0-9]+)|([0-9]+(\.[0-9]+)*)', res)

    offset = 0
    for match in iter:
        num: str = match.group(0)
        if num == '1':
            continue
        if num.count('.') > 1:
            raise Exception('Invalid number')
        res = res[:match.start() + offset] + \
                '1' + res[match.end() + offset:]
        offset += 1 - len(num)
        
    # make javascript variable regex
    offset = 0
    iter = re.finditer(
        f'(?:^|[^a-zA-Z_$0-9])([a-zA-Z_$0-9]+)', res)
    for match in iter:
        var_str = match.group(1)
        if re.match(r'[0-9][^0-9]+', var_str):
            print(match.group(0))
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
