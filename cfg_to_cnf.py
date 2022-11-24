from cfg import CFG

cfg = CFG()

cfg.load('./data/cfg.txt')
cnf = cfg.to_cnf()
cnf.dump("./data/cnf.txt")

cfg = CFG()
cfg.load('./data/func_cfg.txt')
cnf = cfg.to_cnf()
cnf.dump("./data/func_cnf.txt")

cfg = CFG()
cfg.load('./data/loopnswitch_cfg.txt')
cnf = cfg.to_cnf()
cnf.dump("./data/loopnswitch_cnf.txt")
