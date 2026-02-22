#!/usr/bin/env python3
"""
ex3 - functools_artifacts.py
Functional tools: reduce, partial, lru_cache, singledispatch.
"""

from __future__ import annotations

from functools import lru_cache, partial, reduce, singledispatch
from operator import add
from typing import Any, Callable


def power_reduce(powers: list[int]) -> int:
    """
    Combine a list of power values into a single total using reduce.

    Returns 0 for an empty list.
    """
    if not powers:
        return 0
    return reduce(add, powers)


def spell_partial(
    spell_func: Callable[[int, int], int],
    fixed_value: int,
) -> Callable[[int], int]:
    """
    Freeze the first argument of spell_func using functools.partial.

    spell_func is expected to be a binary function: (a, b) -> int
    Returned function becomes unary: (b) -> int
    """
    return partial(spell_func, fixed_value)


@lru_cache(maxsize=None)
def mana_cache(spell_name: str, base_mana: int) -> int:
    """
    Cached mana cost computation.
    Demonstrates lru_cache behavior for repeated calls.
    """
    name_weight = len(spell_name)
    return base_mana + name_weight


@singledispatch
def artifact_analyzer(value: Any) -> str:
    """
    Analyze an artifact depending on its type.
    Default implementation for unsupported types.
    """
    return "Unknown artifact"


@artifact_analyzer.register
def _(value: int) -> str:
    return f"Power level: {value}"


@artifact_analyzer.register
def _(value: str) -> str:
    return f"Artifact name: {value}"


@artifact_analyzer.register
def _(value: dict) -> str:
    name = value.get("name", "Unnamed")
    power = value.get("power", "N/A")
    return f"Artifact: {name} (power={power})"


def main() -> None:
    print("=== Ancient Library ===")

    powers = [3, 5, 7]
    print("power_reduce:", power_reduce(powers))

    def add_spell(a: int, b: int) -> int:
        return a + b

    fixed_add = spell_partial(add_spell, 10)
    print("spell_partial:", fixed_add(5))

    print("mana_cache:", mana_cache("fireball", 10))
    print("mana_cache (cached):", mana_cache("fireball", 10))

    print("artifact_analyzer int:", artifact_analyzer(7))
    print("artifact_analyzer str:", artifact_analyzer("Orb of Insight"))
    print(
        "artifact_analyzer dict:",
        artifact_analyzer({"name": "Wand of Sparks", "power": 3}),
    )
    print("artifact_analyzer other:", artifact_analyzer([1, 2, 3]))


if __name__ == "__main__":
    main()
