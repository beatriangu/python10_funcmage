#!/usr/bin/env python3
"""
higher_magic.py
Exercise 1 - Higher-order functions and function composition
(FuncMage).

This module demonstrates that functions are first-class citizens:
they can be passed as arguments, returned from other functions,
and combined to build reusable behavior.
"""


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """
    Combine two spells into a single spell.

    The returned function calls both spells using the same arguments
    and returns a tuple containing both results.
    """
    if not callable(spell1) or not callable(spell2):
        print("Error: spell_combiner expects two callable spells.")
        return None

    def combined(*args, **kwargs) -> tuple:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))

    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """
    Amplify a spell by multiplying its numeric result.

    Assumes base_spell returns a number.
    """
    if not callable(base_spell):
        print("Error: power_amplifier expects a callable base_spell.")
        return None

    if not isinstance(multiplier, int):
        print("Error: multiplier must be an int.")
        return None

    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier

    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    """
    Cast a spell only if condition returns True.

    If the condition fails, return the string: "Spell fizzled".
    """
    if not callable(condition) or not callable(spell):
        print(
            "Error: conditional_caster expects callable "
            "condition and spell."
        )
        return None

    def conditional(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"

    return conditional


def spell_sequence(spells: list[callable]) -> callable:
    """
    Create a spell sequence.

    Each spell receives the same arguments.
    Returns a list of all spell results.
    """
    if not isinstance(spells, list) or not spells:
        print("Error: spell_sequence expects a non-empty list.")
        return None

    for spell in spells:
        if not callable(spell):
            print("Error: all elements in spells must be callable.")
            return None

    def sequence(*args, **kwargs) -> list:
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results

    return sequence


# -------------------------------------------------------------------
# Demo spells
# -------------------------------------------------------------------


def fireball(target: str) -> str:
    """Return a descriptive fireball action."""
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    """Return a descriptive heal action."""
    return f"Heals {target}"


def base_damage(amount: int) -> int:
    """Return the base damage amount."""
    return amount


def always_true(*args, **kwargs) -> bool:
    """Condition that always returns True."""
    return True


def always_false(*args, **kwargs) -> bool:
    """Condition that always returns False."""
    return False


def cast_spell1(target: str) -> str:
    """First spell in sequence."""
    return f"Spell1 casts on {target}"


def cast_spell2(target: str) -> str:
    """Second spell in sequence."""
    return f"Spell2 casts on {target}"


def cast_spell3(target: str) -> str:
    """Third spell in sequence."""
    return f"Spell3 casts on {target}"


def ft_main() -> None:
    """Test higher-order magic functions."""

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    if combined is not None:
        result = combined("Dragon")
        print(
            "Combined spell result:",
            f"{result[0]}, {result[1]}",
        )

    print("\nTesting power amplifier...")
    amplified = power_amplifier(base_damage, 3)
    if amplified is not None:
        print(
            f"Original: {base_damage(10)}, "
            f"Amplified: {amplified(10)}",
        )

    print("\nTesting conditional casting...")
    conditional_ok = conditional_caster(always_true, fireball)
    if conditional_ok is not None:
        print("Condition True:", conditional_ok("Dragon"))

    conditional_fail = conditional_caster(always_false, fireball)
    if conditional_fail is not None:
        print("Condition False:", conditional_fail("Dragon"))

    print("\nTesting spell sequence...")
    spells = [cast_spell1, cast_spell2, cast_spell3]
    sequence = spell_sequence(spells)
    if sequence is not None:
        result = sequence("Dragon")
        print("Spell sequence results:", result)


if __name__ == "__main__":
    ft_main()
