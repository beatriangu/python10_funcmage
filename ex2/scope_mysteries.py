#!/usr/bin/env python3
"""
ex2 - scope_mysteries.py
Closures, lexical scoping, and nonlocal state.
"""

from __future__ import annotations

from typing import Callable


def mage_counter() -> Callable[[], int]:
    """
    Return a function that counts how many times it has been called.
    Each call increments the internal counter and returns the new value.
    """
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


def spell_accumulator(start: int) -> Callable[[int], int]:
    """
    Return a function that accumulates spell power over time.
    """
    total = start

    def add(delta: int) -> int:
        nonlocal total
        total += delta
        return total

    return add


def enchantment_factory(element: str) -> Callable[[str], str]:
    """
    Return a function that enchants a spell name with a fixed element.
    """
    def enchant(spell: str) -> str:
        return f"{element} {spell}"

    return enchant


def memory_vault() -> Callable[[str], int]:
    """
    Return a function that records keys and counts how many times
    each key has been stored.
    """
    vault: dict[str, int] = {}

    def store(key: str) -> int:
        vault[key] = vault.get(key, 0) + 1
        return vault[key]

    return store


def main() -> None:
    print("=== Memory Depths ===")

    counter = mage_counter()
    print(
        "mage_counter:",
        counter(),
        counter(),
        counter(),
    )

    accumulator = spell_accumulator(10)
    print(
        "spell_accumulator:",
        accumulator(5),
        accumulator(-2),
        accumulator(7),
    )

    fire_enchant = enchantment_factory("fire")
    ice_enchant = enchantment_factory("ice")
    print(
        "enchantment_factory:",
        fire_enchant("ball"),
        "|",
        ice_enchant("shield"),
    )

    vault = memory_vault()
    print(
        "memory_vault:",
        vault("rune"),
        vault("rune"),
        vault("sigil"),
        vault("rune"),
    )


if __name__ == "__main__":
    main()
