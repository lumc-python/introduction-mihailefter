# Exercise 1
Instead of a `while` loop:

```python
i = 9
while i > 1:
    print i
    i -= 1
```

Use `range`:

```python
for i in range(9, 1, -1):
    print i
```

The three statements concerning 2, 1, or 0 bottles of beer on the wall can be
printed outside of the loop.

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

Use string formatting instead of the `replace` function.

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

# General

- There should be no space between the function name and the parenthesis: not
`func ()` but `func()`.
- No spaces when slicing: not `l[1: 3]` but `l[1:3]`.
- Use single quotes instead of double quotes for strings.
- Don't use keywords like `list` or `str` as variable names, this is a recipe
for disaster.
- Use spaces around operators for clarity: ` == `, ` = `, ` + `, etc. Notable
exceptions: named parameters in function calls and slicing.
- Avoid idempotent statements like `a = a`.
- Use an indentation of 4 spaces.
- Avoid the usage of a variable named l (lower case L).
- Avoid creating objects that are only used once, e.g., `lst = range(10) ... `
`for item in lst: ...`
- Just mentioning a variable is not really a good way for printing its contents (use print).
- Avoid unused loop variables.
- Most people have the tendency to explicitly calculate everything, while often a more pythonic way should be preferred.