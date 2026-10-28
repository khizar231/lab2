# CAI601400 — Artificial Intelligence Lab 2

## Files
- `lab2_percepts.py`: memoryless reflex baseline.
- `lab2_model.py`: stateful controller that stores the previous target and suppresses duplicate commands.
- `lab2_check.py`: automated checks for repeat suppression, boundaries, transitions and occupancy priority.
- `Lab2_Report.docx`: PEAS specifications, environment classifications, trace, alternatives, limitations and reflection.
- `outputs.txt`: captured reproducible outputs.

## Requirements
Python 3.10+; no third-party Python packages are required to run the scripts.

## Run
```bash
python lab2_percepts.py
python lab2_model.py
python lab2_check.py
```

## Assumptions and safety
This is a synthetic classroom controller, not a real HVAC or safety system. Occupancy overrides temperature and selects `COMFORT`; if unoccupied, temperature below 18 C selects `HEAT`, above 26 C selects `COOL`, and the inclusive middle interval [18, 26] selects `IDLE`. The controller suppresses commands when the target equals the previous target. A real actuator may fail or drift, so real systems need feedback, safety limits and fault handling.

## GitHub submission checklist
Commit the scripts, report, README and trace. Do not commit credentials, private data, or virtual environments. Give the instructor access and submit the repository URL and final commit identifier through the course submission channel.
