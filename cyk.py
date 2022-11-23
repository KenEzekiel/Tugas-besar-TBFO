from cnf import CNF


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

        # Cek apakah Start Rule S ada di indeks o, n-1 atau tidak
        return self.start in (Back[0][n-1])
