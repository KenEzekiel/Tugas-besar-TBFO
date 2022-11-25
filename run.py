import argparse
import os
import inputreader
from fa import tokenize_with_fa, SyntaxError
from cyk import CYK
from colorama import Fore, Style
import time

os.system('color')

cyk = CYK("./data/cnf.txt")
func_cyk = CYK("./data/func_cnf.txt")
loopnswitch_cyk = CYK("./data/loopnswitch_cnf.txt")

with open("./data/function_terminals.txt", 'r') as a:
    function_terminals = a.read().split()

with open("./data/terminals.txt", 'r') as a:
    terminals = a.read().split()
    terminals.append(' ')
    terminals.append(r'\n')

with open("./data/loopnswitch_terminals.txt", 'r') as a:
    loopnswitch_terminals = a.read().split()


def print_duration(duration):
    print(f"{Fore.YELLOW}Duration: {duration:.5f}s{Style.RESET_ALL}")


def check_file(filename: str, count=None):
    with open(filename, 'r') as f:
        raw = f.read()
    print(f"{Fore.CYAN}Test file: {os.path.basename(filename)}")
    if count is not None:
        print(f"Test number: {count}")
    print(Style.RESET_ALL, end='')

    start = time.time()
    try:
        fa_parsed = tokenize_with_fa(raw, terminals)
        function_check(fa_parsed)
    except SyntaxError as e:
        fail("Syntax Error\n")
        fail(e.message)
        print_duration(time.time() - start)
        print("\n")
        return

    processed = inputreader.preprocessing(fa_parsed)
    words = inputreader.inputread(processed, terminals)
    valid = cyk.check(words)
    if valid:
        success("Accepted")
    else:
        fail("Syntax Error")
    print_duration(time.time() - start)
    print("\n")


def success(message):
    print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")


def fail(message):
    print(f"{Fore.RED}{message}{Style.RESET_ALL}")


def function_check(w: str):
    func_words = inputreader.inputread(w, function_terminals)
    if not func_cyk.check(func_words):
        raise SyntaxError("Invalid function.")
    
def loopnswitch_check(w: str):
    loopnswitch_words = inputreader.inputread(w, loopnswitch_terminals)
    if not loopnswitch_cyk.check(loopnswitch_words):
        raise SyntaxError("Invalid function.")

parser = argparse.ArgumentParser(
    prog="Javascript Parser",
)
parser.add_argument(
    'file_or_folder', help='File or folder to parse')

args = parser.parse_args()

is_folder = os.path.isdir(args.file_or_folder)
print('\n')
if is_folder:
    count = 1
    for filename in os.listdir(args.file_or_folder):
        check_file(os.path.join(args.file_or_folder, filename), count)
        count += 1
else:
    check_file(args.file_or_folder)
