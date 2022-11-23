import re


class SyntaxError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def get_current_line(code: str, idx: int):
    return code[:idx+1].count('\n') + 1


def process_string(code: str):
    res = code
    current = None
    start = None
    i = 0
    num_newline = 0

    strings = ['"', "'", '`']
    for char in code:
        # ketemu penutup string
        if char == current:
            length = i - start
            # mengganti string dengan karakter 1
            res = res[:start] + "1" + ('\n' * num_newline) + res[i+1:]
            # adjustment index menyesuaikan panjang string dan banyak newline
            i -= length - num_newline
            num_newline = 0
            current = None
        elif current is not None:
            if char == '\n':
                num_newline += 1
                if current != '`':
                    raise SyntaxError(
                        f'Invalid string at line {get_current_line(res, i)}, string must not contain new line.')
        elif char in strings:
            current = char
            start = i
        i += 1
    if current is not None:
        raise SyntaxError(
            f'Invalid string at line {get_current_line(res, start)}, string must be closed.')
    return res


def tokenize_with_fa(code: str, terminals: list[str]):
    terminals = terminals[::]
    terminals.remove('variable')
    terminals.remove('number')

    res = code

    multiline_comment = r'\/\*[\w\W]*?\*\/'
    iter = re.finditer(multiline_comment, res)
    for match in iter:
        res = res[:match.start()] + "\n" * res[match.start()                                               :match.end()].count('\n') + res[match.end():]

    # remove comment
    res = re.sub(r'\/\/.*', '', res)

    # Process string -> any string will be replaced by character 1
    res = process_string(res)

    invalid_comment = re.finditer(r'\/\*', res)
    for match in invalid_comment:
        raise SyntaxError(
            f'Invalid comment at line {get_current_line(res, match.start())}, comment must be closed.')

    iter = re.finditer(
        r'([0-9]+(\.[0-9]+)+)|([0-9]+\.)|(\.[0-9]+)|([0-9]+(\.[0-9]+)*)', res)

    # mengubah semua angka/float menjadi karakter 1
    offset = 0
    for match in iter:
        num: str = match.group(0)
        if num == '1':
            continue
        if num.count('.') > 1:
            raise SyntaxError(
                f'Invalid number at line {get_current_line(res, match.start() + offset)}.')
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
            raise SyntaxError(
                f'Invalid variable name at line {get_current_line(res, match.start() + offset)}.')

        if var_str not in terminals:
            res = res[:match.start(1) + offset] + \
                'variable' + res[match.end(1) + offset:]
            offset += len('variable') - len(var_str)

    # mengubah semua 1 menjadi number
    res = re.sub(r'1', 'number', res)
    return res
