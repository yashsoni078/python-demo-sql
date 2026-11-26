# Day 2: Take Input and Calculate Prices

## Today's Topics

1. What are we building today?
2. Data types: text, whole numbers, decimal numbers, `True`, `False`, and `None`
3. Read user input with `input()`
4. Convert input into the correct data type
5. Arithmetic operators: calculate a product total
6. Important terms

---

## 1. What Are We Building Today?

**Project:** Inventory and Order Management System for a small store.

Yesterday, our program showed **one product and its stock**.

Today, our program will:
1. **Ask** the user for a **quantity** and a **price** (in Rs).
2. **Calculate** the total price.
3. **Display** the total.

> This is the first step towards **customer orders**: when a customer buys 3 notebooks, the store needs to know the total price.

---

## 2. Data Types

Every value in Python has a **type**. The type tells Python **what kind of value** it is.

| Type | Python name | Meaning | Example |
|---|---|---|---|
| **Text** | `str` (string) | Letters, words, sentences | `"Notebook"`, `"NB-001"` |
| **Whole number** | `int` (integer) | Numbers without a decimal point | `25`, `0`, `-3` |
| **Decimal number** | `float` | Numbers with a decimal point | `12.50`, `0.5` |
| **True / False** | `bool` (boolean) | Only two values: yes or no | `True`, `False` |
| **Nothing** | `None` | "No value yet" | `None` |

### Examples in Our Store

```python
product_name = "Notebook"   # str   (text)
stock_quantity = 25         # int   (whole number)
weight_kg = 0.25            # float (decimal number)
is_available = True         # bool  (True or False)
supplier = None             # None  (no supplier yet)
```

### Important Points

- `"25"` (with quotes) is **text**. `25` (without quotes) is a **number**.
- `True` and `False` start with a **capital letter**.
- `None` means **"nothing here yet"**. It is **not** the same as `0` or `""`.

### Check the Type with `type()`

```python
print(type("Notebook"))   # <class 'str'>
print(type(25))           # <class 'int'>
print(type(12.50))        # <class 'float'>
print(type(True))         # <class 'bool'>
print(type(None))         # <class 'NoneType'>
```

---

## 3. Read User Input with `input()`

`input()` **asks the user to type something** and gives back what they typed.

```python
name = input("Enter product name: ")
print("You entered:", name)
```

**Output:**
```
Enter product name: Notebook
You entered: Notebook
```

- The text inside `input("...")` is the **message** shown to the user.
- The program **waits** until the user types and presses **Enter**.

---

## 4. Convert Input into the Correct Data Type

> ⚠️ **`input()` always gives back text (`str`)**, even if the user types a number.

```python
quantity = input("Enter quantity: ")   # user types 3
print(type(quantity))                  # <class 'str'>  → it is text, not a number!
```

**Problem:** we cannot do maths with text.

```python
quantity = input("Enter quantity: ")   # user types 3
print(quantity * 2)                    # prints 33, not 6!
```

### Solution: Convert the Value

| Function | Converts to | Example |
|---|---|---|
| `int()` | Whole number | `int("3")` → `3` |
| `float()` | Decimal number | `float("12.5")` → `12.5` |
| `str()` | Text | `str(3)` → `"3"` |

```python
quantity = int(input("Enter quantity: "))   # user types 3
print(quantity * 2)                         # 6 ✅
```

> If the user types something that is not a number (like `abc`), `int()` gives an **error**.
> We will learn how to handle these errors on **Day 8**.

---

## 5. Arithmetic Operators

**Arithmetic operators** are symbols used to do maths.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Add | `10 + 3` | `13` |
| `-` | Subtract | `10 - 3` | `7` |
| `*` | Multiply | `10 * 3` | `30` |
| `/` | Divide (gives a decimal) | `10 / 3` | `3.333...` |
| `//` | Divide (whole number only) | `10 // 3` | `3` |
| `%` | Remainder | `10 % 3` | `1` |

### Calculate a Product Total

```python
quantity = 3
price = 12.50               # price of one item in Rs

total = quantity * price
print("Total: Rs", total)   # Total: Rs 37.5
```

### Examples in Our Store

```python
stock = 25
stock = stock + 10      # new stock arrived → 35
stock = stock - 3       # customer bought 3 → 32
print(stock)            # 32
```

---

## 6. Important Terms

| Term | Simple Meaning |
|---|---|
| **Data type** | The kind of value (text, number, True/False, etc.) |
| **String (`str`)** | Text inside quotes, like `"Notebook"` |
| **Integer (`int`)** | A whole number, like `25` |
| **Float (`float`)** | A decimal number, like `12.50` |
| **Boolean (`bool`)** | `True` or `False` |
| **`None`** | Means "no value yet" |
| **`type()`** | Shows the data type of a value |
| **`input()`** | Asks the user to type something; always gives back text |
| **Convert** | Change a value from one type to another, like `int("3")` → `3` |
| **Arithmetic operator** | A symbol for maths, like `+`, `-`, `*`, `/` |

---

## Today's Hands-On

Create a program that:
1. **Asks** for a **quantity**.
2. **Asks** for a **price in Rs**.
3. **Calculates** the total.
4. **Displays** the total.

Example output:
```
Enter quantity: 3
Enter price in Rs: 12.50
Total: Rs 37.5
```

> Use `int()` for the quantity (whole number) and `float()` for the price (it can have a decimal, like `12.50`).

## Today's Git Task

Commit and push:
- ✅ The input program
- ✅ The calculation examples

```bash
git add .
git commit -m "Add input and price calculation"
git push
```

---

## Day 2 Summary

- Python has **data types**: `str` (text), `int` (whole number), `float` (decimal), `bool` (`True`/`False`), and `None`.
- `input()` asks the user for a value, and it **always gives back text**.
- Use `int()` or `float()` to **convert** text into a number.
- **Arithmetic operators** (`+`, `-`, `*`, `/`, `//`, `%`) do maths.
- **Total price** = quantity × price.
