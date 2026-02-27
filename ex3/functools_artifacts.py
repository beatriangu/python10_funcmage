#!/usr/bin/env python3
"""
functools_artifacts.py
Exercise 3 - Functools treasures (FuncMage).

Demonstrates:
- functools.reduce with multiple operations
- functools.partial to create specialized functions
- functools.lru_cache for memoized fibonacci
- functools.singledispatch for type-based spell behavior
"""

from functools import lru_cache, partial, reduce, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    Reduce spell powers using functools.reduce.

    Supported operations: "add", "multiply", "max", "min"
    Returns the reduced value.

    For an empty list, returns 0 for "add" and 1 for "multiply".
    For "max"/"min" on empty list, returns 0.
    """
    if not spells:
        if operation == "multiply":
            return 1
        return 0

    if operation == "add":
        return reduce(add, spells)

    if operation == "multiply":
        return reduce(mul, spells)

    if operation == "max":
        return reduce(lambda a, b: a if a > b else b, spells)

    if operation == "min":
        return reduce(lambda a, b: a if a < b else b, spells)

    print("Error: unsupported operation.")
    return 0


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """
    Create specialized enchantments using functools.partial.

    base_enchantment must accept: (power, element, target)

    Returns a dict with:
    - 'fire_enchant'
    - 'ice_enchant'
    - 'lightning_enchant'

    Each partial sets power=50 and the respective element.
    """
    if not callable(base_enchantment):
        print("Error: partial_enchanter expects a callable.")
        return {}

    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """
    Return the nth Fibonacci number using lru_cache for memoization.

    Fibonacci:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2)
    """
    if n < 0:
        return 0
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    """
    Create and return a single-dispatch spell system.

    Behaviors:
    - int: damage spell
    - str: enchantment spell
    - list: multi-cast spell
    """

    @singledispatch
    def dispatch(value):
        return "Unknown spell type"

    @dispatch.register
    def _(value: int) -> str:
        return f"Damage spell deals {value} damage!"

    @dispatch.register
    def _(value: str) -> str:
        return f"Enchantment applied: {value}"

    @dispatch.register
    def _(value: list) -> str:
        return f"Multi-cast spell: {len(value)} casts -> {value}"

    return dispatch


def base_enchantment(power: int, element: str, target: str) -> str:
    """Example enchantment function used by partial_enchanter."""
    return f"{element.title()} enchantment ({power}) on {target}"


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print("Min:", spell_reducer(spells, "min"))

    print("\nTesting partial enchanter...")
    enchants = partial_enchanter(base_enchantment)
    if enchants:
        print(enchants["fire_enchant"]("Dragon"))
        print(enchants["ice_enchant"]("Shield"))
        print(enchants["lightning_enchant"]("Golem"))

    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(25))
    print(dispatch("Flaming"))
    print(dispatch([5, 10, 15]))


if __name__ == "__main__":
    main()
