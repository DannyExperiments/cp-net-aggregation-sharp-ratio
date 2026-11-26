#!/usr/bin/env python3
"""Exact finite replay of the leave-one-out OR profile."""
from fractions import Fraction


def verify(t):
    contexts = range(1 << t)
    profile = [[int(bool(mask & ~(1 << i))) for mask in contexts] for i in range(t)]
    ones = list(map(sum, zip(*profile)))
    unrestricted = sum(min(count, t - count) for count in ones)
    assert unrestricted == t
    assert [mask for mask in contexts if 0 < ones[mask] < t] == [
        1 << i for i in range(t)
    ]
    for omitted, table in enumerate(profile):
        hidden_bit = 1 << omitted
        cost = 0
        for mask in contexts:
            if mask & hidden_bit:
                continue
            mate = mask | hidden_bit
            zero_cost = ones[mask] + ones[mate]
            one_cost = 2 * t - zero_cost
            assert zero_cost != one_cost
            optimum = int(one_cost < zero_cost)
            assert table[mask] == table[mate] == optimum
            cost += min(zero_cost, one_cost)
            if mask == 0:
                assert (zero_cost, one_cost) == (t - 1, t + 1)
            if t == 4 and omitted == 0 and mask in (0, 2):
                visible = "".join(str((mask >> i) & 1) for i in range(1, 4))
                print(f"t=4, hide X1, visible bits {visible}: "
                      f"ones=({ones[mask]},{ones[mate]}), costs=({zero_cost},{one_cost})")
        assert cost == 2 * (t - 1)
        assert sum(a != b for a, b in zip(table, map(bool, contexts))) == 1
        assert sum(sum(a != b for a, b in zip(table, rival)) for rival in profile) == cost
    if t == 4:
        assert 3 * cost > 4 * unrestricted
    print(f"t={t}: OPT={unrestricted}, Algorithm 1={cost}, ratio={Fraction(cost, unrestricted)}")


def main():
    for t in range(3, 13):
        verify(t)
    for t in range(2, 201):
        for minority in range(t // 2 + 1):
            ordered_disagreements = 2 * minority * (t - minority)
            assert ordered_disagreements <= 2 * (t - 1) * minority
    print("PASS: all OR profiles from 3 through 12 inputs and vote inequalities through 200")


if __name__ == "__main__":
    main()
