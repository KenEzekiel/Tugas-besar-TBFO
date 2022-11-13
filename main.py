from cfg import CFG
from cnf import CNF
import cyk
import inputreader

cfg = CFG()

cfg.load('cfg.txt')
cnf = cfg.to_cnf()
cnf.dump("cnf.txt")

<<<<<<< HEAD
cnf = CNF()
cnf.load("cnf.txt")

w = inputreader.inputread("input.txt")
cyk.CYKCheck(w)
=======
cfg = CFG()
cfg.load('func_cfg.txt')
cnf = cfg.to_cnf()
cnf.dump("func_cnf.txt")
>>>>>>> c6b085f3fffd04f4dbf14f8a21de89f305e1b8e9
