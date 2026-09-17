# ECU44291 project repository

**Student:** [your name], [student number]

This repository holds your term project for ECU44291 Quantitative Macroeconomics. Every graded piece is submitted by pushing here. Keep it private; only you and the lecturer can see it.

## Run it

```
uv sync                       # build the environment (once, and after any change to pyproject.toml)
uv run pytest                 # run every test in tests/
uv run python check_setup.py  # self-check: PASS on every line means you are set up
```

## Layout

```
src/         your code: solow.py (M0), household.py (M1), equilibrium.py (M3), ...
tests/       pytest tests; test_setup.py is the template's one green test, keep it
notebooks/   Jupyter notebooks: the Week 1 lecture notebook is here; 03_calibration.ipynb (M3) later
data/        the calibration data, provided with M3; plus anything your extension needs
report/      the final report and its figures
AI_LOG.md    your generative-AI disclosure, updated as you go
SPEC.md      your approved project proposal (from M2 onwards)
```

Tests import your code directly (`from solow import k_next`), because `pyproject.toml` puts `src/` on the path for pytest.

## Rules that live here

- Commit regularly with informative messages. A single-commit history forfeits process marks.
- `AI_LOG.md` is part of every submission. No entry for a piece means no AI was used on it.
- During M1 Part A (from the release of M0 marks to your `m1-solo` tag) no generative AI touches `src/household.py` or `tests/`, and Copilot is off.
- Do not put this repository inside OneDrive, iCloud Drive or Dropbox.

The definitive rules are the Blackboard module description.
