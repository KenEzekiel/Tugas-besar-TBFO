def isletter(c: str) -> True:
    if ((65 <= ord(c) and ord(c) <= 90) or (97 <= ord(c) and ord(c) <= 122)):
        return True
    
def isNumber(c: str) -> bool:
    if ((48 <= ord(c) and ord(c) <= 57)):
        return True
    else:
        return False

def isDollarUnderscoreLetter (c: str) -> bool:
    if (isletter(c) or ord(c) == 36 or ord(c) == 95):
        return True
    else:
        return False

var_transition_table = {'Start': {'DUL': 'p1' }, 'p1': {'number': 'p1', 'DUL': 'p1'}}

def check_variable_name_valid(string: str) -> bool:
    curr_state = 'Start'
    for c in string:
        if isNumber(c):
            c = 'number'
        elif isDollarUnderscoreLetter(c):
            c = 'DUL'
            
        if c in var_transition_table[curr_state]:
            curr_state = var_transition_table[curr_state][c]
        else:
            print("syntax error: variable name")
            return False
    return True