# 🧙‍♀️ FuncMage — Functional Programming in Python

A small project to practice **functional programming patterns** in modern Python:
lambdas, higher-order functions, closures, `functools`, and decorators.

The focus is not “clever code”, but **clear, testable, explainable design**
using function composition and controlled side effects.

---

## 🎯 Goals

- Use functions as first-class objects (pass/return functions)
- Build closures that preserve state safely
- Apply `functools` utilities to simplify patterns
- Write decorators that keep metadata with `functools.wraps`
- Keep code clean, typed, and lint-friendly (`flake8`)

---

## 📂 Structure

- **ex0 — `lambda_spells.py`**  
  Lambdas + `sorted`, `filter`, basic transformations and stats.

- **ex1 — `higher_magic.py`**  
  Higher-order functions: combine, amplify, conditionally apply and sequence spells.

- **ex2 — `scope_mysteries.py`**  
  Closures, lexical scope, and `nonlocal` state.

- **ex3 — `functools_artifacts.py`**  
  `reduce`, `partial`, `lru_cache`, and `singledispatch`.

- **ex4 — `decorator_mastery.py`**  
  Decorators with `wraps`, parametrized decorators, retry logic, and static methods.

---

## 🚀 Run

From the repository root:

```bash
python3 ex0/lambda_spells.py
python3 ex1/higher_magic.py
python3 ex2/scope_mysteries.py
python3 ex3/functools_artifacts.py
python3 ex4/decorator_mastery.py