"""Lab 2: simple reflex controller for room climate.

Synthetic lab assumptions:
- Occupancy has priority: an occupied room targets COMFORT.
- Otherwise, temperature below 18 C targets HEAT; above 26 C targets COOL.
- At exactly 18 C or 26 C, target IDLE when unoccupied.
- This simple baseline has no memory and emits a command every time.
Run: python lab2_percepts.py
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Percept:
    temperature_c: float
    occupied: bool


def reflex_target(percept: Percept) -> str:
    if percept.occupied:
        return "COMFORT"
    if percept.temperature_c < 18:
        return "HEAT"
    if percept.temperature_c > 26:
        return "COOL"
    return "IDLE"


def reflex_step(percept: Percept) -> tuple[str, bool]:
    """Baseline reflex controller: always requests the current target."""
    return reflex_target(percept), True


if __name__ == "__main__":
    samples = [
        Percept(17.9, False),
        Percept(17.9, False),
        Percept(18.0, False),
        Percept(26.0, False),
        Percept(26.1, False),
        Percept(22.0, True),
        Percept(22.0, False),
    ]
    print("REFLEX BASELINE (always sends)")
    for i, percept in enumerate(samples, start=1):
        target, send = reflex_step(percept)
        print(f"{i}. percept={percept} -> target={target}, command={'SEND' if send else 'NO SEND'}")
