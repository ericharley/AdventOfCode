from z3 import *
import operator

lines = open("input.txt","r").readlines()

def parse_line(line):
    inst, *param = line.split(" ")
    return (inst, tuple(param))


insts = list(map(parse_line, lines))

# the same 18 line subroutine gets run 14 times
# except for 3 parameters that change each time
P, Q, DZ = [], [], []
subs = [insts[idx * 18 : (idx + 1) * 18] for idx in range(14)]
for sub in subs:
    P.append(int(sub[5][1][1]))
    Q.append(int(sub[15][1][1]))
    DZ.append(int(sub[4][1][1]))


def solve(op):
    solutions = []
    best = None
    while True:
        solver = Solver()
        # the only unknowns are the 14 digits
        ds = [Int(f"d{i}") for i in range(14)]
        for d in ds:
            solver.add(And(d >= 1, d <= 9))
        # convenience variable to get the numerical answer
        num = sum(d * 10 ** (13 - i) for i, d in enumerate(ds))
        if best:
            solver.add(op(num, best))
        z = 0
        # we can think of z as really a list of base 26 digits
        for d, p, q, dz in zip(ds, P, Q, DZ):
            x = z % 26  # the last digit of z
            z /= dz  # remove the last digit of z
            z = If(x != d - p, 26 * z + d + q, z)  # if cond, add the digit d+q to z
        solver.add(z == 0)

        if solver.check() == sat:
            best = solver.model().eval(num).as_long()
        else:
            return best
    return None


for op in [operator.gt, operator.lt]:
    print(solve(op))
