# Day 2 Worksheet: Lists, Functions, Derivatives

**Date:** Mon 26 Oct 2026 · **Topic:** Python revision + derivatives (slope at a point)
**23 questions** · Target time: 60–75 min

## Rules
1. **Predict first, on paper.** Every predict-the-output answer needs a **reason** (one line is enough).
2. **Then run it.** Paste the real output under your prediction. "I believe…" doesn't count.
3. **Mark yourself honestly** ✅ / ❌, and for every ❌ write *what exactly went wrong*.
4. Code goes in `Day-2/worksheet_code.py`. Answers go in this file.

Several questions are today's checks with a twist, especially the ones you missed. Don't answer from memory; the numbers changed.

---

## Section A: Python, predict the output (10)

**A1.** (today's Check 1, new numbers)
```python
nums = [4, 1, 3]
r = sorted(nums, reverse=True)
nums.append(2)
print(nums)
print(r)
```
Prediction + reason:
Actual output:

**A2.** (continues from A1)
```python
x = nums.sort()
print(x)
print(nums)
```
Prediction + reason:
Actual output:

**A3.** Slicing
```python
a = [1, 2, 3, 4, 5]
print(a[-3:])
print(a[5:])
print(a[:-1])
```
Prediction + reason:
Actual output:

**A4.** Aliasing vs copying
```python
a = [1, 2, 3]
b = a
c = a.copy()
b.append(4)
print(a, c)
```
Prediction + reason:
Actual output:

**A5.** Shallow copy, with a twist
```python
grid = [[0, 0], [0, 0]]
s = grid[:]
s[0][0] = 9
s.append([1, 1])
print(grid)
print(s)
```
Prediction + reason (careful: two different kinds of change happen here):
Actual output:

**A6.** append vs extend
```python
xs = [1, 2]
xs.append([3])
xs.extend("ab")
print(xs, len(xs))
```
Prediction + reason:
Actual output:

**A7.** remove vs pop
```python
nums = [3, 7, 3, 9]
nums.remove(3)
y = nums.pop()
print(y, nums)
```
Prediction + reason:
Actual output:

**A8.** Functions as arguments
```python
def twice(f, x):
    return f(f(x))

def inc(n):
    return n + 1

print(twice(inc, 5))
print(twice(lambda s: s + "!", "go"))
```
Prediction + reason:
Actual output:

**A9.** Functions in a list
```python
funcs = [abs, round, len]
print(funcs[0](-3), funcs[2]("chai"))
```
Prediction + reason:
Actual output:

**A10.** Mutable default trap
```python
def log(msg, history=[]):
    history.append(msg)
    return len(history)

print(log("a"))
print(log("b"))
print(log("c", []))
print(log("d"))
```
Prediction + reason (the last line is the real test):
Actual output:

---

## Section B: Python, write from a blank file (3)

No looking at old code. Write it, run it, paste code + output.

**B1.** `count_words(text)` returns a dict of how many times each word appears.
`count_words("the cat the hat")` → `{'the': 2, 'cat': 1, 'hat': 1}`
*(You skipped this one in the diagnostic.)*

**B2.** `evens_squared(nums)` returns the squares of only the even numbers, using **one list comprehension**.
`evens_squared([1, 2, 3, 4])` → `[4, 16]`
*(In the diagnostic you used `:` and forgot the filter. Get both right.)*

**B3.** Fix `dict_operation(a, b={})` in your **Functions/DAY-3** using the `b=None` pattern. Call it twice without passing `b` and show the second call no longer sees data from the first.

---

## Section C: Derivatives by hand (6)

Calculator allowed. Show every step.

**C1.** Slope of the straight line through (1, 3) and (4, 12).

**C2.** For y = x², give the **sign** of the slope (positive / negative / zero) at x = −3, x = 0 and x = 2. One-line reason each, using the word "negative", "zero" or "positive".

**C3.** For y = x² at **x = 5** with **h = 0.1**, write the four lines: start y, new x and new y, rise, rise ÷ run.
Then, **without calculating**, use the 2x + h result from today's proof to predict the guess for h = 0.01.

**C4.** Proof. Show with algebra that the secant slope of x² at **x = 1** is exactly **2 + h**. (Same steps as today's 6 + h proof: expand, subtract, divide.) What's the true slope at x = 1?

**C5.** New loss curve. One data point: **x = 3, true y = 12**. Model: prediction = w × x.
(a) Write loss(w).
(b) Fill in the table:

| w | Prediction | Error (pred − actual) | Loss |
|---|---|---|---|
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |

(c) Which w is best, and why?

**C6.** For the C5 loss:
(a) At w = 2, is the slope of the loss positive or negative? Turn w up or down? Prove it with two rows of your table, not a guess.
(b) Find two values of w that have the **same loss** but **opposite slopes**.

---

## Section D: Code (4)

All in `Day-2/worksheet_code.py`, reusing your `derivative()`. Label every print with the right variable name (x or w).

**D1.** Write `cube(x)` returning x³. Print the slope at x = 2 for h = 0.1, 0.01, 0.001. What number is it heading towards?

**D2.** Code the C5 loss as `loss2(w)`. Print the slope at **w = 2, 4 and 6**, formatted with `:.5f`. Do the signs match your answers to C6? At w = 4, why isn't it exactly 0? (Hint: think about what today's "+ h" did.)

**D3.** The error column, now that you know what it means. For h in `[1e-1, 1e-3, 1e-5, 1e-8, 1e-12, 1e-15]`, print the slope of `square` at x = 3 **and** `abs(d - 6)`. Which h has the smallest error? Which row would you have picked wrongly without `abs`?

**D4.** Depth question. Write `central_derivative(f, x, h=0.01)` that returns:
```
(f(x + h) - f(x - h)) / (2 * h)
```
It uses one point on **each side** instead of only ahead. Compare it with `derivative()` for `square` at x = 3, h = 0.01, using the error `abs(d - 6)`. Which one is more accurate? Bonus: use algebra like C4 to explain why.

---

## Section E: Ship it

- [ ] All 23 answered, predictions + real outputs, self-marked
- [ ] `Functions/DAY-3` fixed (B3)
- [ ] Committed and pushed (see the push list in chat)

## Score
Section A: __ / 10 · B: __ / 3 · C: __ / 6 · D: __ / 4 · **Total: __ / 23**
