def max_joltage_for_bank(bank: str, k: int) -> int:
    """
    Given a string of digits `bank` and integer k,
    return the largest possible k-digit number (as int)
    you can form by picking digits in order.
    """
    n = len(bank)
    to_remove = n - k
    stack = []

    for ch in bank:
        # While we can still remove digits, and the last chosen digit
        # is smaller than the current one, pop it.
        while to_remove > 0 and stack and stack[-1] < ch:
            stack.pop()
            to_remove -= 1
        stack.append(ch)

    # If we still have removals left, remove from the end
    if to_remove > 0:
        stack = stack[:-to_remove]

    # Take first k digits (stack may be longer if we didn’t trim)
    result_str = "".join(stack[:k])
    return int(result_str)


banks = open('input.txt').read().strip().split('\n')

part1,part2 = 0,0
for bank in banks:
  part1 += max_joltage_for_bank(bank,2)
  part2 += max_joltage_for_bank(bank,12)

print(part1)
print(part2)
