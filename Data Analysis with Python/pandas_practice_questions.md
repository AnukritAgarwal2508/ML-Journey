# Pandas practice — `messy_employees.csv`

218 rows × 15 columns. Every problem below is deliberately planted. Do not peek at
"What's planted" until you've finished Level 2.

```python
import pandas as pd
df = pd.read_csv("messy_employees.csv")   # start here, then fix the read itself
```

---

## Level 1 — inspection

1. Shape, `dtypes`, `info()`, `describe()`. Which columns came in as `object` that
   should obviously be numeric? Why did that happen?
2. `df.columns` — two headers are wrong. Fix all headers to `snake_case` with no
   trailing spaces, in one line (no manual dict of 15 entries).
3. For every column, print the number of unique values. Which column is useless?
4. `df.head(20)` — spot three different formats used in `date_of_joining`.

## Level 2 — missing values

5. `df.isna().sum()` undercounts. Why? Find every sentinel used for "missing" in
   this file (there are six distinct ones plus whitespace-only cells).
6. Re-read the file so that all of them become real `NaN`, using `na_values=` in
   `read_csv`. Now recount.
7. Percentage of missing per column, sorted descending. Drop any column that is
   more than 90% missing.
8. Rows with 2+ missing values — how many? Show them.
9. Impute:
   - `salary` → median **of its own department** (not global median)
   - `performance_score` → global mean, rounded to 1dp
   - `department` → the string `"Unknown"`
   - `work_hours_per_week` → forward fill, then backfill anything still empty
   Do the salary one with `groupby().transform()`, not a loop.
10. `bonus` is missing for some rows but `salary` and `performance_score` exist.
    Reconstruct it as `salary * performance_score / 100` only where `bonus` is null.

## Level 3 — dirty types and categories

11. `salary` contains `$`, commas, and a `" AUD"` suffix. Convert the whole column
    to float without dropping rows. `str.replace` + `regex=True` + `astype`.
12. `age` has impossible values (a 5-year-old, a 999, a negative). Define a sane
    range, count violations, then set them to `NaN` and impute.
13. `department` has casing, whitespace, and abbreviation variants (`Engg`, `Mktg`,
    `H.R.`, `Customer Support`...). Collapse to exactly 6 clean categories + Unknown.
    Verify with `value_counts()`.
14. Same treatment for `city` (casing + whitespace only).
15. `remote` is stored as `Yes/yes/Y/TRUE/1/No/no/N/FALSE/0`. Map to a real boolean
    dtype. Any value you didn't anticipate should raise, not silently become `False`.
16. Parse `date_of_joining` into datetime despite four mixed formats. `format="mixed"`
    and `dayfirst=` are your friends — then sanity-check that no date landed in the
    future, which is how you catch `05/06/2021` parsed the wrong way round.
17. Strip whitespace and title-case `name`. Flag rows where `email` is blank and
    regenerate it as `first.last@corp.com`.

## Level 4 — duplicates

18. How many *exact* duplicate rows? Drop them, keeping the first.
19. After that, `emp_id` still repeats. These are near-duplicates: same employee,
    one copy with fields blanked out. For each duplicated `emp_id`, keep the row
    with the **fewest** nulls. (Hint: `df.isna().sum(axis=1)` as a sort key, then
    `drop_duplicates(subset="emp_id")`.)
20. Confirm `emp_id` is now unique and set it as the index.

## Level 5 — aggregation and derived columns

21. Mean, median and count of `salary` per `department`, sorted by median.
22. Add `tenure_years` = years between `date_of_joining` and today, rounded to 1dp.
23. Add `salary_band` using `pd.cut`: Low / Mid / High / Very High on quartiles.
    Then `pd.crosstab` band against department.
24. Per department, the single highest-paid employee (`idxmax`, or `sort_values`
    + `groupby().head(1)` — do it both ways and compare).
25. `pivot_table`: mean salary, rows = department, cols = remote, `margins=True`.
26. Rank employees within their department by `performance_score`
    (`groupby().rank(method="dense", ascending=False)`).
27. Correlation matrix of the numeric columns. Does `experience_years` predict
    `salary` more than `performance_score` does?
28. Departments where mean `performance_score` > 3.4 — filter with
    `groupby().filter()`, returning the original rows, not the aggregate.

## Level 6 — the stuff interviewers actually ask

29. Outliers in `salary` by IQR rule. Count them, then cap them (winsorize) instead
    of dropping.
30. `work_hours_per_week` has 0, 168 and -12. Handle these differently from the
    salary outliers and justify the difference in a comment.
31. Write one function `clean(path) -> pd.DataFrame` that does Levels 2–4 end to
    end and returns a tidy frame. Run it on the raw file. This is the actual
    deliverable — the previous 30 questions were the notes.
32. Prove your cleaning is idempotent: `clean_df(clean_df(df))` equals `clean_df(df)`.

---

## Sanity checks (peek only after Level 4)

<details>
<summary>What's planted</summary>

- Missing-value sentinels: `""`, `"NA"`, `"n/a"`, `"?"`, `"null"`, `"-"`, whitespace-only
- Missing counts (after treating all sentinels as NaN): salary 28, performance_score 21,
  bonus 19, age 16, department 16, work_hours_per_week 13, city 11,
  date_of_joining 10, email 6, exit_date 211
- `exit_date` is 96.8% empty → drop it
- Exact duplicate rows: 12
- Duplicate `emp_id` after dropping exact dupes: 6 (the near-duplicates)
- Clean department counts once collapsed: hr 41, sales 35, marketing 34,
  finance 33, engineering 31, support 28, unknown 16 (before dedup)
- 4 impossible ages, 3 impossible salaries, 3 impossible work-hour values,
  3 rows with `experience_years = 99`
</details>
