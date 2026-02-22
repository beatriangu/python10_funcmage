# 🧙‍♀️ FuncMage — MAP
## Programación funcional en Python

---

## 1. Objetivo del módulo

Este módulo profundiza en los fundamentos de la programación funcional
en Python.

El objetivo no es escribir código “ingenioso”, sino comprender cómo:

- Las funciones pueden componerse.
- El comportamiento puede construirse dinámicamente.
- El estado puede mantenerse de forma controlada.
- Las responsabilidades pueden separarse mediante decoradores.

Se trabaja una transición clara desde un enfoque imperativo
hacia un diseño más declarativo y composable.

---

## 2. Conceptos clave trabajados

- Funciones como objetos de primera clase.
- Expresiones lambda y operaciones funcionales básicas.
- Funciones de orden superior (reciben y devuelven funciones).
- Closures y alcance léxico.
- Uso de `nonlocal` para modificar variables del cierre.
- Herramientas de `functools`:
  - `reduce`
  - `partial`
  - `lru_cache`
  - `singledispatch`
- Decoradores simples y parametrizados.
- Preservación de metadatos con `functools.wraps`.
- Separación de responsabilidades mediante decoradores.

---

## 3. Desglose por ejercicios

### ex0 — Lambda Sanctum

**Enfoque:** Transformaciones funcionales simples.

Se aplican:
- Ordenación con clave compuesta.
- Filtrado por condición.
- Transformación de cadenas.
- Cálculo de estadísticas básicas.

**Aprendizaje clave:**
Expresar transformaciones de datos sin lógica condicional dispersa.

---

### ex1 — Higher Realm

**Enfoque:** Funciones de orden superior.

Se implementa:
- Composición de funciones.
- Amplificación de resultados.
- Aplicación condicional de comportamiento.
- Encadenamiento secuencial de funciones.

**Aprendizaje clave:**
Construir comportamiento por composición, no por ramificación.

---

### ex2 — Memory Depths

**Enfoque:** Closures y estado controlado.

Se desarrollan:
- Contadores que recuerdan estado.
- Acumuladores con `nonlocal`.
- Estructuras mutables capturadas en el cierre.

**Aprendizaje clave:**
El estado puede existir dentro del cierre sin convertirse en estado global.

---

### ex3 — Ancient Library

**Enfoque:** Herramientas funcionales estándar.

Se aplican:
- Reducción con `reduce`.
- Fijación parcial de argumentos con `partial`.
- Cacheo transparente con `lru_cache`.
- Despacho por tipo con `singledispatch`.

**Aprendizaje clave:**
Reutilizar herramientas del lenguaje para resolver patrones recurrentes.

---

### ex4 — Master’s Tower

**Enfoque:** Decoradores completos y reutilizables.

Se implementan:
- Decorador de medición de tiempo.
- Decorador parametrizado para validación.
- Decorador con reintento ante excepciones.
- Uso de `@staticmethod` en contexto funcional.

**Aprendizaje clave:**
Separar comportamientos transversales sin contaminar
la lógica principal de la función.

---

## 4. Evolución conceptual

Este módulo consolida un cambio de mentalidad:

Antes:
- Funciones aisladas.
- Lógica directa.
- Estado explícito.

Ahora:
- Composición funcional.
- Estado encapsulado en closures.
- Comportamientos añadidos mediante decoradores.
- Reutilización estructurada con `functools`.

---

## 5. Conclusión

La programación funcional en Python no es un estilo alternativo,
sino una herramienta para:

- Reducir complejidad.
- Aumentar claridad.
- Separar responsabilidades.
- Construir comportamiento escalable.

El resultado es un código más modular,
más expresivo y más defendible.