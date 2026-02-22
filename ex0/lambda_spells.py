#!/usr/bin/env python3
"""
ex0 - lambda_spells.py
Lambda practice: sorting, filtering, mapping and basic stats.
"""

from __future__ import annotations

from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Return artifacts sorted by (power ASC, name ASC).

    Each artifact is expected to have:
    - "name": str
    - "power": int
    """
    return sorted(
        artifacts,
        key=lambda artifact: (artifact["power"], artifact["name"]),
    )


def power_filter(
    artifacts: list[dict[str, Any]],
    threshold: int,
) -> list[dict[str, Any]]:
    """
    Return artifacts with power strictly greater than threshold.
    """
    return list(
        filter(
            lambda artifact: artifact["power"] > threshold,
            artifacts,
        )
    )


def spell_transformer(spell: str) -> str:
    """
    Transform spell into a shouted incantation.

    Rule:
    - strip spaces
    - uppercase
    - replace spaces by underscores
    - append "!"
    """
    cleaned = spell.strip().upper()
    return cleaned.replace(" ", "_") + "!"


def mage_stats(powers: list[int]) -> dict[str, float]:
    """
    Return basic stats from a list of powers.

    Keys:
    - "min"
    - "max"
    - "avg"
    """
    if not powers:
        return {"min": 0.0, "max": 0.0, "avg": 0.0}

    total = sum(powers)
    return {
        "min": float(min(powers)),
        "max": float(max(powers)),
        "avg": float(total / len(powers)),
    }


def main() -> None:
    artifacts = [
        {"name": "Orb of Insight", "power": 7},
        {"name": "Wand of Sparks", "power": 3},
        {"name": "Cloak of Shadows", "power": 5},
        {"name": "Amulet of Dawn", "power": 5},
    ]

    print("=== Lambda Sanctum ===")

    print("\nSorted artifacts:")
    for artifact in artifact_sorter(artifacts):
        print(artifact)

    print("\nFiltered artifacts (power > 4):")
    for artifact in power_filter(artifacts, 4):
        print(artifact)

    print("\nTransformed spell:")
    print(spell_transformer("fire ball"))

    print("\nMage stats:")
    powers = [artifact["power"] for artifact in artifacts]
    print(mage_stats(powers))


if __name__ == "__main__":
    main()
