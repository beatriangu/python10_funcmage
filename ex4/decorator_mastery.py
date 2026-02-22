#!/usr/bin/env python3
"""
ex4 - decorator_mastery.py
Decorators with wraps, parametrized decorators,
retries, and static methods.
"""

from __future__ import annotations

import time
from functools import wraps
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def spell_timer(func: F) -> F:
    """
    Decorator that measures execution time of a spell function.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"{func.__name__} took {elapsed:.6f}s")
        return result

    return wrapper  # type: ignore[return-value]


def power_validator(min_power: int) -> Callable[[F], F]:
    """
    Decorator factory enforcing a minimum power value.
    Assumes the wrapped function receives 'power'
    as an int argument.
    """

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power")

            if power is None and len(args) >= 1:
                power = args[-1]

            if not isinstance(power, int):
                raise ValueError("power must be an int")

            if power < min_power:
                raise ValueError(
                    f"power must be >= {min_power}"
                )

            return func(*args, **kwargs)

        return wrapper  # type: ignore[return-value]

    return decorator


def retry_spell(retries: int) -> Callable[[F], F]:
    """
    Decorator factory that retries a spell function
    if it raises an exception.
    """

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exc: Exception | None = None

            for _ in range(retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_exc = exc

            if last_exc is not None:
                raise last_exc

            raise RuntimeError("Retry failed unexpectedly")

        return wrapper  # type: ignore[return-value]

    return decorator


class MageGuild:
    """Guild utilities for validating mages and casting spells."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        Validate mage name:
        must be non-empty and alphabetical (spaces allowed).
        """
        if not isinstance(name, str):
            return False

        stripped = name.strip()

        if not stripped:
            return False

        return all(
            part.isalpha() for part in stripped.split()
        )

    @staticmethod
    @power_validator(5)
    def cast_spell(
        mage_name: str,
        spell_func: Callable[[int], str],
        power: int,
    ) -> str:
        """
        Cast a spell if mage name is valid
        and power meets minimum threshold.
        """
        if not MageGuild.validate_mage_name(mage_name):
            raise ValueError("Invalid mage name")

        return spell_func(power)


def main() -> None:
    print("=== Master's Tower ===")

    @spell_timer
    def fireball(power: int) -> str:
        return f"Fireball cast with power {power}"

    @retry_spell(2)
    def unstable_spell(power: int) -> str:
        if power < 3:
            raise RuntimeError("Spell fizzled!")
        return (
            f"Unstable spell succeeded with power {power}"
        )

    print(
        MageGuild.cast_spell(
            "Astra Nova",
            fireball,
            7,
        )
    )

    try:
        print(
            MageGuild.cast_spell(
                "Astra Nova",
                fireball,
                2,
            )
        )
    except ValueError as exc:
        print("Validation error:", exc)

    try:
        print(unstable_spell(1))
    except RuntimeError as exc:
        print("Retry error:", exc)

    print(unstable_spell(3))


if __name__ == "__main__":
    main()
