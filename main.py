from cfg import CFG
from cnf import CNF
import cyk
import inputreader

cfg = CFG()

cfg.load('cfg.txt')
cnf = cfg.to_cnf()
cnf.dump("cnf.txt")

cnf = CNF()
cnf.load("cnf.txt")

w = inputreader.inputread("input.txt")
cyk.CYKCheck(w)
