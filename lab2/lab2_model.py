"""Lab 2: stateful controller suppressing duplicate target commands.

All thresholds and modes are synthetic teaching assumptions, not a real HVAC
control specification. Run: python lab2_model.py
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Percept:
    temperature_c: float
    occupied: bool


def target_for(percept: Percept) -> str:
    # Occupancy priority is intentionally retained.
    if percept.occupied:
        return "COMFORT"
    if percept.temperature_c < 18:
        return "HEAT"
    if percept.temperature_c > 26:
        return "COOL"
    return "IDLE"


class StatefulController:
    def __init__(self, initial_mode: str = "UNKNOWN"):
        self.previous_target_mode = initial_mode

    def step(self, percept: Percept) -> tuple[str, bool, str]:
        previous = self.previous_target_mode
        target = target_for(percept)
        send_command = target != previous
        # Store the desired target even when no command is sent.
        self.previous_target_mode = target
        return target, send_command, previous


if __name__ == "__main__":
    samples = [
        ("Repeated cold percept 1", Percept(17.0, False)),
        ("Repeated cold percept 2", Percept(17.0, False)),
        ("Lower exact boundary", Percept(18.0, False)),
        ("Upper exact boundary", Percept(26.0, False)),
        ("Mode transition", Percept(27.0, False)),
        ("Occupied priority", Percept(27.0, True)),
        ("Empty room", Percept(22.0, False)),
    ]
    controller = StatefulController()
    print("STATEFUL CONTROLLER TRACE")
    print("Case | Previous mode | Percept | Target | Command outcome")
    for name, percept in samples:
        target, send, previous = controller.step(percept)
        print(f"{name} | {previous} | {percept} | {target} | {'SEND' if send else 'NO COMMAND'}")
