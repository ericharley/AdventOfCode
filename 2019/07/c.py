#!/usr/bin/env python3

import sys
from itertools import permutations


class computer:
    def __init__(self, program, input_):
        self.program = program
        self.input = input_
        self.first_in = True
        self.done = False
        self.eip = 0

    def get_param(self, mode, value):
        if mode == "0":
            return self.program[value]
        else:
            return value

    def compute(self, signal):
        while True:
            inst = self.program[self.eip]
            op = inst % 100
            mode3, mode2, mode1 = f"{inst // 100:03d}"
            assert mode3 == "0"
            if op == 1:
                self.program[self.program[self.eip + 3]] = self.get_param(
                    mode1, self.program[self.eip + 1]
                ) + self.get_param(mode2, self.program[self.eip + 2])
                self.eip += 4
            elif op == 2:
                self.program[self.program[self.eip + 3]] = self.get_param(
                    mode1, self.program[self.eip + 1]
                ) * self.get_param(mode2, self.program[self.eip + 2])
                self.eip += 4
            elif op == 3:
                if self.first_in:
                    self.program[self.program[self.eip + 1]] = self.input
                    self.first_in = False
                else:
                    self.program[self.program[self.eip + 1]] = signal
                self.eip += 2
            elif op == 4:
                self.eip += 2
                return self.program[self.program[self.eip - 1]]
            elif op == 5:
                if self.get_param(mode1, self.program[self.eip + 1]) != 0:
                    self.eip = self.get_param(mode2, self.program[self.eip + 2])
                else:
                    self.eip += 3
            elif op == 6:
                if self.get_param(mode1, self.program[self.eip + 1]) == 0:
                    self.eip = self.get_param(mode2, self.program[self.eip + 2])
                else:
                    self.eip += 3
            elif op == 7:
                self.program[self.program[self.eip + 3]] = int(
                    self.get_param(mode1, self.program[self.eip + 1])
                    < self.get_param(mode2, self.program[self.eip + 2])
                )
                self.eip += 4
            elif op == 8:
                self.program[self.program[self.eip + 3]] = int(
                    self.get_param(mode1, self.program[self.eip + 1])
                    == self.get_param(mode2, self.program[self.eip + 2])
                )
                self.eip += 4
            elif op == 99:
                self.done = True
                return None
            else:
                print("Error")
                sys.exit()


def amplify(phase_seq):

    sig = 0
    for phase in phase_seq:
        comp = computer(list(map(int, program_str.split(","))), phase)
        sig = comp.compute(sig)

    return sig


def feedback_amplify(phase_seq):

    sig = 0
    last_valid = None
    comps = [
        computer(list(map(int, program_str.split(","))), phase) for phase in phase_seq
    ]
    while not any([comp.done for comp in comps]):
        for i in range(5):
            sig = comps[i].compute(sig)
            if sig is not None:
                last_valid = sig
    return last_valid


with open(sys.argv[1], "r") as f:
    program_str = f.read().strip()

max_thrust = max([amplify(comb) for comb in permutations([0, 1, 2, 3, 4])])
print(f"Part 1: {max_thrust}")

max_feedback_thrust = max(
    [feedback_amplify(comb) for comb in permutations([5, 6, 7, 8, 9])]
)
print(f"Part 2: {max_feedback_thrust}")

