# Exercise 1
A `while` loop is OK:

```python
i = 9
while i > 1:
    print i
    i -= 1
```

But range is more pythonic.

The `break` statement is rarely needed. Try to modify the stop condition
instead:

```python
while True:
    if x < 1:
        break
    x -= 1
```
To:
```python
while x >= 1:
    x -= 1
```

The three statements concerning 2, 1, or 0 bottles of beer on the wall can be
printed inside the loop, but better to avoid extra computation.

Use string formatting instead of the `replace` function.

This is too much computation. You can start like this but refine it later.
```python
l=list(range(10))
l.reverse()
```

# Exercise 2
Nice one, but the string `s` is empty after this operation:
```python
while len(s) > 0:
    print s
    s = s[1:]
```

Alternative, leaving `s` untouched:
```python
for i in range(len(s)):
    print s[i:]
```

Manipulation of an iterator value does nothing in a for-loop:
```python
for i in range(10):
    print i
    i += 1 # This does nothing.
```

Doing something in more than one case can often be written simpler, e.g.:
```python
if x > 10:
    x += 1
    print x
else:
    x -= 1
    print x
```
To:
```python
if x > 10:
    x += 1
else:
    x -= 1
print x
```

Slicing up to the end of the list can be done by omitting the second position,
e.g., `s[4:]`.

# Exercise 3
Use the logical `or` and `and`, not the bitwise `|` and `&` in logical
expressions.

Use `elif` and `else`, and not this:
```python
for i in range(1, 100):
    if i%3 == 0:
        print("Fizz")
    if i%5 == 0:
        print("Buzz")
    if i%3 != 0 and i%5 != 0:
        print(i)
print()
```

# Exercise 4
Instead of copying values like:
```python
y = x
print (x, y)
```
Use:
```python
print (x, x)
```
# Exercise 5
Preferably do not reuse variables like this: `for x in x:`.

# Exercise 6
No need to use `update` when adding a new entry in a dictionary.
```python
unique.update({subseq : 1})
```
Just do:
```python
unique[subseq] = 1
```

Docstrings should be the first statement in a function definition. So not:
```python
def find_strings_dict(STR,k):
    d = {}
    newvalue = 0
"""A function that takes in a string and returns a dictionary k-mer counts for the strings."""
length = len(STR) + 1
```


# General

- There should be no space between the function name and the parenthesis: not
`func ()` but `func()`.
- No spaces when slicing: not `l[1: 3]` but `l[1:3]`.
- Stick to either single quotes or double quotes for strings (be consistent).
- Don't use keywords like `list` or `str` as variable names, this is a recipe
for disaster.
- Use spaces around operators for clarity: ` == `, ` = `, ` + `, etc. Notable
exceptions: named parameters in function calls and slicing.
- Avoid idempotent statements like `a = a`.
- Use an indentation of 4 spaces.
- Better to avoid the usage of a variable named l (lower case L).
- Avoid creating objects that are only used once, e.g., `lst = range(10) ... `
`for item in lst: ...`
- Just mentioning a variable is not really a good way for printing its contents
(use print).
- Avoid unused loop variables.
- Most people have the tendency to explicitly calculate everything, while often
a more pythonic way should be preferred.
- No need to add `0`, e.g., `string=input[0+i:k_mer+i]`.
