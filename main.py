from cfg import CFG

cfg = CFG()

cfg.load('cfg.txt')
cnf = cfg.to_cnf()
cnf.dump("cnf.txt")

cfg = CFG()
cfg.load('func_cfg.txt')
cnf = cfg.to_cnf()
cnf.dump("func_cnf.txt")
