import angr,claripy

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

def main():
    p = angr.Project('angr3_o',auto_load_libs=False)
    argv1 = claripy.BVS("argv1",24*8)
    state = p.factory.entry_state(args=['./angr3_o',argv1])
    # state = p.factory.entry_state(args=['./angr3',argv1],add_options={angr.options.LAZY_SOLVES})
    for flag_chr in argv1.chop(8):
        state.add_constraints(state.solver.And(flag_chr>=0x30,flag_chr<=0x39))
    sm = p.factory.simulation_manager(state)
    # sm.explore(find=FIND_ADDR,avoid=AVOID_ADDR)
    sm.explore(find=correct,avoid=wrong)
    found = sm.found[0]
    print(found.solver.eval(argv1,cast_to=bytes))



if __name__ == "__main__":
    main()