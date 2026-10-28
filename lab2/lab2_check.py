"""Automated checks for the Lab 2 stateful controller."""
from lab2_model import Percept, StatefulController, target_for


def run_checks():
    checks = []
    c = StatefulController()
    target, send, previous = c.step(Percept(17.0, False))
    checks.append(("first cold target sends", target == "HEAT" and send and previous == "UNKNOWN"))
    target, send, previous = c.step(Percept(17.0, False))
    checks.append(("repeated target suppressed", target == "HEAT" and not send and previous == "HEAT"))
    target, send, previous = c.step(Percept(18.0, False))
    checks.append(("18 C exact lower boundary is IDLE", target == "IDLE" and send))
    target, send, previous = c.step(Percept(26.0, False))
    checks.append(("26 C exact upper boundary is IDLE", target == "IDLE" and not send))
    target, send, previous = c.step(Percept(27.0, False))
    checks.append(("transition to COOL sends", target == "COOL" and send))
    target, send, previous = c.step(Percept(27.0, True))
    checks.append(("occupancy overrides hot temperature", target == "COMFORT" and send))
    target, send, previous = c.step(Percept(22.0, False))
    checks.append(("empty room returns to IDLE", target == "IDLE" and send))
    for label, passed in checks:
        print(f"{label}: {'PASS' if passed else 'FAIL'}")
    print(f"Summary: {sum(p for _, p in checks)}/{len(checks)} checks passed")
    if not all(p for _, p in checks):
        raise SystemExit(1)


if __name__ == "__main__":
    run_checks()
