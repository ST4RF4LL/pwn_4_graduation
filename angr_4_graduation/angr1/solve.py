import  angr
p = angr.Project('./angr1',auto_load_libs=False)
FIND_ADDR = 0x40079B
AVOID_ADDR = [0x4007A7,0x4006D6]
state = p.factory.entry_state()
sm = p.factory.simulation_manager(state)
sm.explore(find=FIND_ADDR,avoid=AVOID_ADDR)
print(sm.found[0].posix.dumps(0)[:12])