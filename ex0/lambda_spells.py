#!/usr/bin/env python3
"""
ex0 - lambda_spells.py
Lambda practice: sorting, filtering, mapping and basic stats (Pydantic-free).
"""

from __future__ import annotations

from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Sort artifacts by power (descending).

    Each artifact:
    - "name": str
    - "power": int
    - "type": str
    """
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True,
    )


def power_filter(
    mages: list[dict[str, Any]],
    min_power: int,
) -> list[dict[str, Any]]:
    """
    Filter mages with power >= min_power.

    Each mage:
    - "name": str
    - "power": int
    - "element": str
    """
    return list(
        filter(
            lambda mage: mage["power"] >= min_power,
            mages,
        )
    )


def spell_transformer(spells: list[str]) -> list[str]:
    """
    Transform spell names by adding '* ' prefix and ' *' suffix.
    """
    return list(
        map(
            lambda spell: f"* {spell} *",
            spells,
        )
    )


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Compute power stats from a list of mages.

    Returns:
    - "max_power": int
    - "min_power": int
    - "avg_power": float (rounded to 2 decimals)
    """
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    min_power = min(mages, key=lambda mage: mage["power"])["power"]
    total_power = sum(map(lambda mage: mage["power"], mages))
    avg_power = round(total_power / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power,
    }


def main() -> None:
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Crystal Orb", "power": 85, "type": "relic"},
        {"name": "Shadow Cloak", "power": 40, "type": "armor"},
    ]

    mages = [
        {"name": "Astra", "power": 9, "element": "fire"},
        {"name": "Orion", "power": 5, "element": "air"},
        {"name": "Lyra", "power": 2, "element": "water"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    if len(sorted_artifacts) >= 2:
        first = sorted_artifacts[0]
        second = sorted_artifacts[1]
        print(
            f"{first['name']} ({first['power']} power) comes before "
            f"{second['name']} ({second['power']} power)"
        )

    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("Testing power filter...")
    filtered = power_filter(mages, 5)
    print([mage["name"] for mage in filtered])

    print("Testing mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
