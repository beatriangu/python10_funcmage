#!/usr/bin/env python3
"""
ex1 - higher_magic.py
Higher-order functions and function composition.
"""

from __future__ import annotations

from typing import Callable


def spell_combiner(
    spell_a: Callable[[int], int],
    spell_b: Callable[[int], int],
) -> Callable[[int], int]:
    """
    Combine two spells into one.
    Applies spell_a, then spell_b to the result.
    """
    def combined(value: int) -> int:
        return spell_b(spell_a(value))

    return combined


def power_amplifier(
    factor: int,
) -> Callable[[Callable[[int], int]], Callable[[int], int]]:
    """
    Amplify the result of a spell by a given factor.
    """
    def decorator(
        spell: Callable[[int], int],
    ) -> Callable[[int], int]:
        def amplified(value: int) -> int:
            return spell(value) * factor

        return amplified

    return decorator


def conditional_caster(
    condition: Callable[[int], bool],
    spell: Callable[[int], int],
) -> Callable[[int], int]:
    """
    Cast spell only if condition is True.
    Otherwise return original value.
    """
    def conditional(value: int) -> int:
        if condition(value):
            return spell(value)
        return value

    return conditional


def spell_sequence(
    spells: list[Callable[[int], int]],
) -> Callable[[int], int]:
    """
    Apply a list of spells sequentially.
    """
    def composed(value: int) -> int:
        result = value
        for spell in spells:
            result = spell(result)
        return result

    return composed


def add_five(value: int) -> int:
    return value + 5


def double(value: int) -> int:
    return value * 2


def greater_than_ten(value: int) -> bool:
    return value > 10


def main() -> None:
    print("=== Higher Realm ===")

    combined = spell_combiner(add_five, double)
    print("Combined spell (3):", combined(3))

    amplified = power_amplifier(3)(add_five)
    print("Amplified spell (4):", amplified(4))

    conditional = conditional_caster(greater_than_ten, add_five)
    print("Conditional spell (8):", conditional(8))
    print("Conditional spell (12):", conditional(12))

    sequence = spell_sequence([add_five, double, add_five])
    print("Spell sequence (2):", sequence(2))


if __name__ == "__main__":
    main()
