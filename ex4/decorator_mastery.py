#!/usr/bin/env python3
"""
decorator_mastery.py
Exercise 4 - Decorator mastery and class methods.
"""

import time
from functools import wraps


def spell_timer(func: callable) -> callable:
    """
    Decorator that measures execution time.
    Prints before and after execution.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> callable:
    """
    Decorator factory that validates minimum power.
    """

    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(self, spell_name: str, power: int):
            if power < min_power:
                return "Insufficient power for this spell"
            return func(self, spell_name, power)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> callable:
    """
    Retry decorator.
    """

    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
                    attempt += 1
            return (
                "Spell casting failed after "
                f"{max_attempts} attempts"
            )

        return wrapper

    return decorator


class MageGuild:
    """Guild class demonstrating staticmethod and decorators."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        stripped = name.strip()
        if len(stripped) < 3:
            return False
        for char in stripped:
            if not (char.isalpha() or char == " "):
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print("Result:", result)

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Astra"))
    print(MageGuild.validate_mage_name("X!"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
