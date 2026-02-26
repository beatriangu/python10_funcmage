# 🧙‍♀️ FuncMage — MAP  
## Functional Programming in Python

---

## 🎯 Module Objective

This module explores how **functions become architectural tools**, not just executable blocks.

The goal is not clever syntax.

It is to understand that:

- Functions are first-class objects.
- Behavior can be composed dynamically.
- State can live inside closures.
- Cross-cutting concerns can be abstracted with decorators.

This marks a transition from:

> Imperative execution  
to  
> Declarative composition

---

## 🗺 Conceptual Progression

---

## 📂 Exercise Breakdown

### 🔹 ex0 — Lambda Sanctum  
**Focus:** Data transformation pipelines

- Ordering with `sorted(..., key=lambda ...)`
- Filtering with `filter(lambda ...)`
- Mapping with `map(lambda ...)`
- Aggregation with `max`, `min`, `sum`

**Key idea:**  
Express *what* happens to data, not *how* to iterate.

---

### 🔹 ex1 — Higher Realm  
**Focus:** Higher-order functions

- Functions as arguments
- Sequential function composition
- Behavior amplification

**Key idea:**  
Build logic through composition instead of branching.

---

### 🔹 ex2 — Memory Depths  
**Focus:** Closures and controlled state

- Captured variables
- `nonlocal` modification
- Encapsulated state without globals

**Key idea:**  
State can exist safely inside a function scope.

---

### 🔹 ex3 — Ancient Library  
**Focus:** Standard functional tools

- `reduce` for cumulative operations
- `partial` for argument specialization
- `lru_cache` for memoization
- `singledispatch` for type-based dispatch

**Key idea:**  
Leverage language primitives instead of reinventing patterns.

---

### 🔹 ex4 — Master’s Tower  
**Focus:** Decorators

- Behavior wrapping
- Parameterized decorators
- Retry, timing, validation patterns
- Metadata preservation with `functools.wraps`

**Key idea:**  
Separate cross-cuting concerns from core logic.

---

## 🧠 Evolution of Thinking

Before this module:

- Functions were isolated.
- Logic was linear.
- State was explicit.

After this module:

- Behavior is composable.
- State can be encapsulated.
- Functions can modify other functions.
- Control flow becomes declarative.

---

## 📌 Core Takeaway

Functional programming in Python is not about purity.

It is about:

- Composability  
- Predictability  
- Encapsulation  
- Separation of concerns  

It reduces control-flow noise  
and increases architectural clarity.