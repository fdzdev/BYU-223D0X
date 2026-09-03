# BYU CS 223 — Data Structures (Section D0X)

Coursework repository for CS 223, Winter 2026. Implementations and unit tests for
the assigned abstract data types.

## Layout

```
src/     ADT implementations
tests/   pytest suites, one module per ADT
```

## Implemented

| ADT | Module | Status |
|-----|--------|--------|
| Dynamic array | `src/dynarray.py` | complete |
| Singly linked list | `src/linkedlist.py` | complete |
| Binary search tree | `src/bst.py` | complete |
| Hash map (chaining) | `src/hashmap.py` | in progress |

## Running the tests

```
python -m pip install -r requirements.txt
python -m pytest tests/ -v
```

## Notes

Amortized analysis writeups for each ADT are in the course LMS, not here.
Growth factor for the dynamic array is 2x; the hash map resizes at load factor 0.75.
