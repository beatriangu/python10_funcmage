#!/usr/bin/env python3
"""
scope_mysteries.py
Exercise 2 - Lexical scoping and closures (FuncMage).
"""


def mage_counter() -> callable:
    """
    Return a function that counts how many times it has been called.
    Each call returns the current count (starting from 1).
    """
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    """
    Return a function that accumulates power over time.
    Each call adds the given amount to the total power.
    """
    total = initial_power

    def accumulate(amount: int):
        nonlocal total
        total += amount
        return total

    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    """
    Return a function that applies the given enchantment.
    Format: "enchantment_type item_name"
    """
    def enchant(item_name: str):
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict:
    """
    Return a dictionary with 'store' and 'recall' functions.
    Uses closure to maintain private memory storage.
    """
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        if key in memory:
            return memory[key]
        return "Memory not found"

    return {
        "store": store,
        "recall": recall,
    }


def main() -> None:
    print("Testing mage counter...")
    counter = mage_counter()
    print("Call 1:", counter())
    print("Call 2:", counter())
    print("Call 3:", counter())

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(10)
    print(accumulator(5))
    print(accumulator(3))

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("spell", "Fireball")
    print(vault["recall"]("spell"))
    print(vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
