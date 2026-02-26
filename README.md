# 🧙‍♀️ FuncMage — Functional Programming in Python

A structured exploration of **functional programming patterns** in modern Python.

This module focuses on clarity, composability, and architectural thinking —  
not clever tricks or condensed syntax.

The goal is to design behavior that is:

- Predictable  
- Reusable  
- Composable  
- Cleanly separated  

---

## 🎯 What This Module Demonstrates

- Functions as first-class objects  
- Higher-order functions (functions receiving and returning functions)  
- Closures and lexical scope  
- Controlled state using `nonlocal`  
- Functional utilities from `functools`  
- Clean decorator design with `functools.wraps`  

The emphasis is not syntax —  
it is **behavioral architecture through composition**.

---

## 🗺 Conceptual Progression

Data Transformation → Higher-Order Functions → Closures → `functools` → Decorators

Each exercise builds incrementally on the previous one.

---

## 📂 Structure

### 🔹 ex0 — `lambda_spells.py`
Lambda expressions and transformation pipelines using:

- `sorted(..., key=lambda ...)`
- `filter(lambda ...)`
- `map(lambda ...)`
- Aggregation with `max`, `min`, `sum`

**Focus:** Expressing intent over manual iteration.

---

### 🔹 ex1 — `higher_magic.py`
Higher-order functions and composition:

- Function chaining  
- Conditional execution  
- Behavior amplification  

**Focus:** Building logic through composition instead of branching.

---

### 🔹 ex2 — `scope_mysteries.py`
Closures and encapsulated state:

- Lexical scope  
- `nonlocal`  
- Controlled mutable state  

**Focus:** Maintaining state without globals.

---

### 🔹 ex3 — `functools_artifacts.py`
Functional tools from the standard library:

- `reduce`
- `partial`
- `lru_cache`
- `singledispatch`

**Focus:** Leveraging built-in abstractions instead of reinventing patterns.

---

### 🔹 ex4 — `decorator_mastery.py`
Decorator design and behavior wrapping:

- Parametrized decorators  
- Retry and timing patterns  
- Metadata preservation with `functools.wraps`  

**Focus:** Separating cross-cutting concerns from core logic.

---

## 🧠 Design Principles

- Explicit behavior  
- Minimal side effects  
- Separation of concerns  
- Composability over conditionals  
- Readability over cleverness  

All exercises follow Python 3.10+ standards and are linted with `flake8`.

---

## 🚀 Run

From the repository root:

```bash
python3 ex0/lambda_spells.py
python3 ex1/higher_magic.py
python3 ex2/scope_mysteries.py
python3 ex3/functools_artifacts.py
python3 ex4/decorator_mastery.py