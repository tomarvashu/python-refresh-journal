# Functions Notes

## What is a function?
A function is a reusable block of code that performs a specific task.

Functions help in:
- avoiding repeated code
- improving readability
- breaking a problem into smaller parts
- making code easier to test and maintain

## Basic Syntax

```python
def function_name():
    print("Hello")

function_name()
```

## Parameters
Parameters allow us to pass values into a function.

```python
def greet(name):
    print("Hello", name)

greet("Vashu")
```

## Return Values
A function can return a value using the `return` keyword.

```python
def add(a, b):
    return a + b

result = add(10, 20)
```

## Key Understanding
- `print()` displays output
- `return` sends value back to the caller
- functions should ideally do one clear task
- meaningful function names improve readability
