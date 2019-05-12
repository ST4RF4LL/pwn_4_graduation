import  angr
p = angr.Project('./angr2_2',auto_load_libs=False)
# angr2_1
# FIND_ADDR = 0x4009B0
# AVOID_ADDR = 0x4009D1
# angr 2_2
FIND_ADDR = 0x400930
AVOID_ADDR = [0x400a63,0x400A63]
state = p.factory.entry_state()
sm = p.factory.simulation_manager(state)
sm.explore(find=FIND_ADDR,avoid=AVOID_ADDR)
print(sm.found[0].posix.dumps(0)[:13])

# AngR_W1Th_fL4
# AnGr_W1Th_bcF
# 