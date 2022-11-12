from cnf import CNF
from pprint import pprint
import inputreader

with open("./terminals.txt", 'r') as a:
    terminals = a.read().split()
with open("./variables.txt", 'r') as b:
    non_terminals = b.read().split()

cnf = CNF()
cnf.load('cnf.txt')
# Grammar dari CNF 
R = cnf.rules
start = cnf.start


# Function to perform the CYK Algorithm
def CYKCheck(w):
    n = len(w)
     
    # Inisialisasi Tabel CYK
    Back = [[set([]) for j in range(n)] for i in range(n)]

 
    # Isi Tabel CYK
    for j in range(0, n):
 
        # Iterasi Production Rules
        for left, rule in R.items():
            for right in rule:
                 
                # Saat ditemukan terminal
                if len(right) == 1 and right[0] == w[j]:
                    Back[j][j].add(left)
 
        for i in range(j, -1, -1):  
              
            # Iterasi dari i sampai j + 1 
            for k in range(i, j + 1):    
                if k + 1 >= n:
                    continue

                # Iterasi Production Rules
                for left, rule in R.items():
                    for right in rule:
                        
                        # Saat terminal ditemukan
                        if len(right) == 2 and right[0] in Back[i][k] and right[1] in Back[k + 1][j]:
                            Back[i][j].add(left)
    
    #pprint(Back)
    # Cek apakah Start Rule S ada di indeks o, n-1 atau tidak
    if start in (Back[0][n-1]):
        print("True")
    else:
        print("False")

 
w = inputreader.inputread("input.txt")
CYKCheck(w)
