import re


def get_current_line(code: str, idx: int):
    return code[:idx].count('\n') + 1


def process_string(code: str):
    res = code
    current = None
    start = None
    i = 0
    num_newline = 0
    strings = ['"', "'", '`']
    for char in code:
        if char == current:
            length = i - start
            res = res[:start] + "1" + ('\n' * num_newline) + res[i+1:]
            i -= length - num_newline
            current = None
        elif current is not None:
            if char == '\n':
                num_newline += 1
                if current != '`':
                    raise Exception(
                        f'Invalid string at line {get_current_line(res, i + 1)}, string must not contain new line.')
        elif char in strings:
            current = char
            start = i
        i += 1
    if current is not None:
        raise Exception(
            f'Invalid string at line {get_current_line(res, start + 1)}, string must be closed.')
    return res


def tokenize_with_fa(code: str, terminals: list[str]):
    terminals = terminals[::]
    terminals.remove('variable')
    terminals.remove('mathexp')
    terminals.remove('comment')
    terminals.remove('newline')
    terminals.remove(r'\w')

    res = code

    # Process string -> any string will be replaced by character 1
    res = process_string(res)
    print(res)

    iter = re.finditer(
        r'([0-9]+(\.[0-9]+)+)|([0-9]+\.)|(\.[0-9]+)|([0-9]+(\.[0-9]+)*)', res)

    # mengubah semua angka/float menjadi karakter 1
    offset = 0
    for match in iter:
        num: str = match.group(0)
        if num == '1':
            continue
        if num.count('.') > 1:
            raise Exception(
                f'Invalid number at line {get_current_line(res, match.start() + 1)}.')
        res = res[:match.start() + offset] + \
            '1' + res[match.end() + offset:]
        offset += 1 - len(num)

    # make javascript variable regex
    offset = 0
    iter = re.finditer(
        f'(?:^|[^a-zA-Z_$0-9])([a-zA-Z_$0-9]+)', res)
    for match in iter:
        var_str = match.group(1)
        if var_str == '1':
            continue
        if re.match(r'[0-9][^0-9]+', var_str):
            raise Exception(
                f'Invalid variable name at line {get_current_line(res, match.start() + 1)}.')

        if var_str not in terminals:
            res = res[:match.start(1) + offset] + \
                'variable' + res[match.end(1) + offset:]
            offset += len('variable') - len(var_str)

    # mengubah semua 1 menjadi number
    res = re.sub(r'1', 'number', res)
    return res
