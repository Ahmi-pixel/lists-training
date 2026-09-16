# lists-training

[![CI](https://github.com/Ahmi-pixel/lists-training/actions/workflows/ci.yml/badge.svg)](https://github.com/Ahmi-pixel/lists-training/actions/workflows/ci.yml)

A small collection of Python list-manipulation exercises, each with its own pytest suite. Every problem lives in a single module at the repo root and has a matching test file under `tests/`.

## Problems

| Module | Function | What it does |
| --- | --- | --- |
| `appending_zeros.py` | `move_zeros_front(nums)` | Moves every `0` to the front of the list, keeping the order of the other elements. |
| `find_target.py` | `find_target_brute(nums, target)` / `find_target(nums, target)` | Finds all index pairs `(i, j)` with `i < j` whose values sum to `target`. Two implementations: an O(n²) pairwise check and an O(n) single pass using a value → index map. |
| `finding_duplicates.py` | `separate_duplicates(nums)` | Returns `(unique values in first-seen order, values that appeared more than once)`. |
| `second_highest.py` | `second_highest(nums)` | Returns the second-largest *distinct* value in one pass, or `None` if there isn't one. |
| `threesum.py` | `three_sum(nums)` | Returns all unique triplets that sum to zero (sort + two-pointer approach). |

Each module can also be run directly to see a sample result:

```bash
python threesum.py
# [[-1, -1, 2], [-1, 0, 1]]
```

## Running the tests

Requires Python 3.12+ and `pytest`.

```bash
pip install pytest
pytest
```

`pyproject.toml` points pytest at the `tests/` directory and adds the repo root to `sys.path`, so tests import the modules directly (e.g. `from threesum import three_sum`).

## CI

GitHub Actions runs the test suite on every push and pull request (see `.github/workflows/ci.yml`).

## Layout

```
.
├── appending_zeros.py
├── find_target.py
├── finding_duplicates.py
├── second_highest.py
├── threesum.py
├── tests/
│   ├── test_appending_zeros.py
│   ├── test_find_target.py
│   ├── test_finding_duplicates.py
│   ├── test_second_highest.py
│   └── test_threesum.py
├── pyproject.toml
└── .github/workflows/ci.yml
```
