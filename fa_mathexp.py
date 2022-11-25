def is_letter(c: str) -> True:
    if ((65 <= ord(c) and ord(c) <= 90) or (97 <= ord(c) and ord(c) <= 122)):
        return True
    
def is_number(c: str) -> bool:
    if ((48 <= ord(c) and ord(c) <= 57)):
        return True
    else:
        return False

def is_dollar_underscore_letter (c: str) -> bool:
    if (is_letter(c) or ord(c) == 36 or ord(c) == 95):
        return True
    else:
        return False

def is_between_ops(c : str) -> bool:
    if ((c == '/') or (c == '%') or (c == '&') or (c == '|') or (c == '^')):
        return True
    else:
        return False
    
mathexp_transition_table = {'Start': {'_': 'Start', 'DUL': 'var', 'number': 'literal', '.': 'literal_with_point_only', '+': 'after_hugging_operator', '-': 'after_hugging_operator', '~': 'after_hugging_operator'},
                        'var': {' ': 'after_obj', 'number': 'var', 'DUL': 'var', 'between_ops': 'after_between_ops', '+': 'after_between_ops', '-': 'after_between_ops', '=': 'wait_equal', '!': 'wait_equal', '>': 'wait_gt', '<': 'wait_lt', '*': 'wait_power'},
                        'literal': {' ': 'after_obj', 'number': 'literal', '.': 'literal_with_point', 'between_ops': 'after_between_ops', '+': 'after_between_ops', '-': 'after_between_ops', '=': 'wait_equal', '!': 'wait_equal', '>': 'wait_gt', '<': 'wait_lt', '*': 'wait_power'},
                        'literal_with_point_only': {'number': 'literal_with_point'},
                        'literal_with_point': {' ': 'after_obj', 'number': 'literal_with_point', 'between_ops': 'after_between_ops', '+': 'after_between_ops', '-': 'after_between_ops', '=': 'wait_equal', '!': 'wait_equal', '>': 'wait_gt', '<': 'wait_lt', '*': 'wait_power'},
                        'after_obj': {' ': 'after_obj', 'between_ops': 'after_between_ops', '+': 'after_between_ops', '-': 'after_between_ops', '=': 'wait_equal', '!': 'wait_equal', '>': 'wait_gt', '<': 'wait_lt', '*': 'wait_power'},
                        'wait_power': {'*': 'after_between_ops', ' ': 'after_between_ops', '~': 'after_hugging_operator', '+': 'after_hugging_operator', '-': 'after_hugging_operator', 'DUL': 'var', 'number': 'literal'},
                        'wait_equal': {'=': 'wait_strict_equal'},
                        'wait_strict_equal': {'=': 'after_between_ops', ' ': 'after_between_ops', '~': 'after_hugging_operator', '+': 'after_hugging_operator', '-': 'after_hugging_operator', 'DUL': 'var', 'number': 'literal'},
                        'wait_gt': {'>': 'wait_rshift', ' ': 'after_between_ops', '~': 'after_hugging_operator', '+': 'after_hugging_operator', '-': 'after_hugging_operator', 'DUL': 'var', 'number': 'literal'},
                        'wait_rshift': {'>': 'after_betweenops', ' ': 'after_between_ops', '~': 'after_hugging_operator', '+': 'after_hugging_operator', '-': 'after_hugging_operator', 'DUL': 'var', 'number': 'literal'},
                        'wait_lt': {'<': 'after_between_ops', ' ': 'after_between_ops', '~': 'after_hugging_operator', '+': 'after_hugging_operator', '-': 'after_hugging_operator', 'DUL': 'var', 'number': 'literal'},
                        'wait_equal': {'=': 'after'},
                        'wait_equal': {'=': 'after'},
                        'after_between_ops': {' ': 'after_between_ops', 'DUL': 'var', 'number': 'literal', '.': 'literal_with_point_only', '+': 'after_hugging_operator', '-': 'after_hugging_operator', '~': 'after_hugging_operator'},
                        'after_hugging_operator': {' ': 'after_hugging_operator', 'DUL': 'var', 'number': 'literal', '.': 'literal_with_point_only'},
                        }

def check_mathexp(string: str) -> bool:
    curr_state = 'Start'
    for c in string:
        if is_dollar_underscore_letter(c):
            c = 'DUL'
        elif is_number(c):
            c = 'number'
        elif is_between_ops(c):
            c = 'between_ops'

        print(curr_state)
        print(c)
        if c in mathexp_transition_table[curr_state]:
            curr_state = mathexp_transition_table[curr_state][c]
        else:
            print("syntax error: variable name")
            return False
    if (curr_state == 'literal' or curr_state == 'literal_with_point' or curr_state == 'var'):
        return True
    else:
        print(f"Masih berada di state {curr_state}")
        return False