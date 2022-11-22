import time
from cnf import CNF
from pprint import pprint
import inputreader
import re
from fa import tokenize_with_fa


class CYK:
    def __init__(self, filename):
        self.load_cnf(filename)

    def load_cnf(self, filename):
        cnf = CNF()
        cnf.load(filename)
        self.rules = cnf.rules
        self.start = cnf.start

    def check(self, words):
        n = len(words)
        if n == 0:
            return True

        # Inisialisasi Tabel CYK
        Back = [[set([]) for j in range(n)] for i in range(n)]

        # Isi Tabel CYK
        for j in range(0, n):
            # Iterasi Production Rules
            for left, rule in self.rules.items():
                for right in rule:

                    # Saat ditemukan terminal
                    if len(right) == 1 and right[0] == words[j]:
                        Back[j][j].add(left)

            for i in range(j, -1, -1):

                # Iterasi dari i sampai j + 1
                for k in range(i, j + 1):
                    if k + 1 >= n or len(Back[i][k]) == 0 or len(Back[k + 1][j]) == 0:
                        continue

                    # Iterasi Production Rules
                    for left, rule in self.rules.items():
                        for right in rule:

                            # Saat terminal ditemukan
                            if len(right) == 2 and right[0] in Back[i][k] and right[1] in Back[k + 1][j]:
                                Back[i][j].add(left)
        # pprint(Back)
        # Cek apakah Start Rule S ada di indeks o, n-1 atau tidak
        return self.start in (Back[0][n-1])


def function_check(w: str):
    with open("./function_terminals.txt", 'r') as a:
        function_terminals = a.read().split()
    func_cyk = CYK("func_cnf.txt")
    func_words = inputreader.inputread(w, function_terminals)
    if not func_cyk.check(func_words):
        print("Not a valid function")
        exit()


with open("input.txt", 'r') as f:
    w = f.read()

with open("./terminals.txt", 'r') as a:
    terminals = a.read().split()
w = tokenize_with_fa(w, terminals)
function_check(w)

terminals.append(' ')
terminals.append(r'\n')
cyk = CYK("cnf.txt")

w = inputreader.preprocessing(w)
words = inputreader.inputread(w, terminals)
valid = cyk.check(words)
if valid:
    print("True")
else:
    print("False")
