# python-basics-practice
A beginner-friendly Python practice project covering basic programming concepts such as variables, data types, conditionals, loops, functions, and list comprehensions.

## 📂 Project Overview

This file demonstrates:
- Printing output with `print()`
- Working with **variables and data types**
- Using **input()** for user interaction
- Performing **type checking** with `type()`
- Writing **conditional statements (if-else)**
- Handling **loops (for and while)**
- Using **match-case** (Python 3.10+)
- Defining **functions**
- Working with **lists and comprehensions**

---

## 🧾 Code Sections

### 1. Printing and Variables
```python
print("Hello World")
a = 2
b = 3.2
c = a + b
print(type(c))
````

### 2. Conditional Statements

```python
bill_total = 95
discount = 10

if bill_total > 100:
    print("Bill is greater than 100")
    bill_total -= discount
else:
    print("Bill is less than 100")
    print("Total bill:", bill_total)
```

### 3. Loops and Iterations

```python
favourites = ['creme brulee', 'apple pie', 'churros', 'tiramisu', 'chocolate cake']
for dessert in favourites:
    print('Favourite dessert:', dessert)
```

### 4. Function Example

```python
def calculate_tax(bill, tax_rate):
    return (bill * tax_rate) / 100.0

print('Total Tax:', calculate_tax(175.00, 15))
```

### 5. List Comprehension & Reversing Lists

```python
numbers = [1, 2, 3, 4, 5]
odd_numbers = [x for x in numbers if x % 2 != 0][::-1]
even_numbers = [x for x in numbers if x % 2 == 0][::-1]
```

---

## ⚙️ How to Run

1. Make sure Python 3 is installed:

   ```bash
   python --version
   ```

2. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/python-basics-practice.git
   ```

3. Navigate into the folder:

   ```bash
   cd python-basics-practice
   ```

4. Run the script:

   ```bash
   python basics.py
   ```

---

## 📚 Learning Outcomes

By going through this code, you’ll learn:

* How to handle **input/output** in Python
* The difference between **data types** (`int`, `float`, `str`, `list`)
* Writing and calling **functions**
* Using **loops and conditions**
* Working with **lists and comprehensions**
* Using **match-case** in Python 3.10+

---

## 👩‍💻 Author

**Iqra **
Full Stack Developer | Python | Django | React.js | Flutter
📍 Lahore, Pakistan

---



