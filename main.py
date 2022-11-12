from cfg import CFG
from cnf import CNF

cfg = CFG()

cfg.load('cfg.txt')
cnf = cfg.to_cnf()
cnf.dump("cnf.txt")

cnf = CNF()
cnf.load("cnf.txt")
