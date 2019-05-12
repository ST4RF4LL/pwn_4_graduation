import angr,claripy
elf = './angr3_o2'
p = angr.Project(elf,auto_load_libs=False)

flag = claripy.BVS("flag",24*8)

def correct(state):
    try:
        return b'Correct' in state.posix.dumps(1)
    except:
        return False
def wrong(state):
    try:
        return b'Wrong' in state.posix.dumps(1)
    except:
        return False

FIND_ADDR = 0x40062A
AVOID_ADDR = 0x40060B

state = p.factory.entry_state(args=[elf,flag])
# state = p.factory.entry_state(args=[elf,flag],add_options={angr.options.LAZY_SOLVES})
for flag_chr in flag.chop(8):
    state.add_constraints(state.solver.And(flag_chr>=0x20,flag_chr<=0x7f))
sm = p.factory.simulation_manager(state)
sm.explore(find=correct,avoid=wrong)
# sm.explore(find=FIND_ADDR,avoid=AVOID_ADDR)
found = sm.found[0]
print(found.solver.eval(flag,cast_to=bytes))
