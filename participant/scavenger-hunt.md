# Commit Message Clinic — Scavenger Hunt

This repo belongs to a small analytics team. The work in it is real
enough — but the commit messages are deliberately terrible (`bug fix`,
`stuff`, `misc changes`). Six months later, nobody can tell from the log
which changes were safe and which moved published numbers.

Below are 10 descriptions. Each one matches exactly one commit. For each,
find the commit and write the message it should have had, using the
prefix taxonomy in [`CONTRIBUTING.md`](../CONTRIBUTING.md).

You don't have to do them in order, and you don't have to do all 10. Pick
the ones that look findable and go.

## Who's on the team

People touch the files they own, so **who made the change is a clue**.
Every description below names the person who made the commit — that alone
narrows 100+ commits to a handful.

| Person | Role | Usually touches |
|---|---|---|
| Raphael Mensah | senior analyst, poverty & inequality | `currency.py` |
| Priya Raghunathan | data engineer, pipelines & storage | `survey.py`, `fraud_risk.py`, `jobs/`, `config/` |
| Tomás Ferreira | analyst, methodology | `poverty_calc.py`, `tests/` |
| Wei Chen | analyst, regional aggregates | `aggregation.py`, `indicators/`, `country_codes.py` |
| Amara Okonkwo | visualization & reporting | `api.py`, `charts.py`, `export.py` |
| Sofia Marchetti | documentation & translation | `docs/` |
| Dmitri Volkov | CI, tooling & release | `.github/`, `Makefile`, `pyproject.toml` |

There is also a `dependabot[bot]`, which commits a lot and is never the
answer to anything here.

## You don't need a terminal

Everything happens in your browser, on GitHub:

- **See every commit:** open the repo and click **Commits** (the
  clock-and-arrow icon above the file list).
- **See what a commit changed:** click the commit. Green is added, red is
  removed. That's the diff.
- **See one file's history:** open the file, then click **History** (top
  right). This is the fastest move when a description names a file.
- **Filter by author:** on the Commits page, use the author dropdown.
  This is the fastest move when a description names a person.
- **Search commits:** the search box on the Commits page filters by
  message text — useful once you know roughly what you're hunting.

Nothing here can break anything. You're reading, not writing.

## How to record an answer

For each clue you solve, fill in all three lines. The middle one — the
message that's actually in the repo — is how the facilitator checks you
found the right commit, and it's half the point of the exercise: you have
to see the bad message next to what it should have said.

```
Commit hash:      ________
As committed:     ________________________________________
Should have been: ________________________________________
```

---

### 1. The poverty line moved

**Tomás Ferreira** changed a single constant in the poverty calculation
— one line, one number — and every downstream poverty estimate shifted.
No logic changed. Just the value, and a comment saying why.

*How to find it:* open `src/wb_analytics/poverty_calc.py` → **History**
and scroll to the bottom. It is the very first change made to that file
after it was created.

```
Commit hash:      ________
As committed:     ________________________________________
Should have been: ________________________________________
```

### 2. Two countries, one code

**Wei Chen** fixed a country code that was colliding with a completely
different country's code. Curaçao had been sitting on Cuba's code.

*How to find it:* `src/wb_analytics/country_codes.py` → **History**. The
diff is a single line of the country lookup table. This is the fastest
clue on the sheet — start here if you want a win.

```
Commit hash:      ________
As committed:     ________________________________________
Should have been: ________________________________________
```

### 3. The commit that changes nothing

**Priya Raghunathan** committed a change to `config/indicator_config.yaml`
that alters nothing but invisible characters — trailing whitespace.

Careful: there are two other whitespace-only commits in this repo, both in
`poverty_calc.py` — one by **Tomás Ferreira**, one by **Dmitri Volkov**.
Neither is the one you want. You want the config file.

*How to find it:* `config/indicator_config.yaml` → **History**. If the
diff doesn't change a single value, you've got it.

```
Commit hash:      ________
As committed:     ________________________________________
Should have been: ________________________________________
```

### 4. A new file appears

**Wei Chen** added a reference file to the repo for the first time — a
country classification CSV. No code was written for it; the data was
simply tracked into version control.

Careful: **Priya** adds a different CSV to the same folder later. You want
the country classification one.

*How to find it:* browse to `data/raw/` and open the file's **History**,
or look for the commit whose diff is one new file and nothing else.

```
Commit hash:      ________
As committed:     ________________________________________
Should have been: ________________________________________
```

### 5. A new indicator from an outside survey

**Amara Okonkwo** added a brand-new indicator sourced from an external
survey — Global Findex — as a new function in the API layer. Purely
additive: nothing that already existed changed shape.

*How to find it:* filter the Commits page by Amara, then look for the
diff that is all green and no red.

```
Commit hash:      ________
As committed:     ________________________________________
Should have been: ________________________________________
```

### 6. Fresher data, same code

**Priya Raghunathan** refreshed a chunk of household survey microdata
covering more than a dozen countries. No calculation logic was touched —
only which data feeds into it.

*How to find it:* `src/wb_analytics/survey.py` → **History**. Like clue 1,
it comes down to one constant.

```
Commit hash:      ________
As committed:     ________________________________________
Should have been: ________________________________________
```

### 7. Stop recomputing the same number

**Raphael Mensah** added caching to the PPP conversion factor lookup,
which had been recomputed on every single request.

Careful: `currency.py` is busy. It carries a long argument about exchange
rates, with several commits reverting each other. Ignore those — you want
the one that makes the code *faster*, not the ones that change a rate.

*How to find it:* `src/wb_analytics/currency.py` → **History**, and look
for the diff that adds a decorator rather than changing a value.

```
Commit hash:      ________
As committed:     ________________________________________
Should have been: ________________________________________
```

### 8. The shape of the repo changes

**Wei Chen** split a single monolithic aggregation file into a whole
`indicators/` package. This is the one commit where the file tree visibly
changes shape — you can spot it without reading the diff at all.

*How to find it:* open `src/wb_analytics/indicators/` and check the
**History** of anything inside it. The oldest commit there is the split.

```
Commit hash:      ________
As committed:     ________________________________________
Should have been: ________________________________________
```

### 9. Shipped under pressure

**Priya Raghunathan** shipped an urgent fix for a crash in the fraud-risk
pipeline — a null country code was blowing up a scoring function.

Careful: Priya also fixed a bug in the nightly batch job around the same
time, and the two are easy to confuse. Only one of them is a crash in
fraud-risk scoring.

*How to find it:* `src/wb_analytics/fraud_risk.py` → **History**. Read the
diff and check it's really about a missing country code.

```
Commit hash:      ________
As committed:     ________________________________________
Should have been: ________________________________________
```

### 10. A field becomes required

**Amara Okonkwo** made a field in an API response required where it had
previously been optional-by-omission — genuinely breaking for anyone
still calling the old way — and wrote a short migration doc alongside it.
Two files change in this commit, not one.

*How to find it:* open `docs/migration_guide.md` and click **History**.
The commit that created that file is your answer.

```
Commit hash:      ________
As committed:     ________________________________________
Should have been: ________________________________________
```

---

## If you finish early

Don't just write the subject line. Write the **body** too — the two or
three sentences under it explaining *why* the change was made and what a
reader needs to watch out for. The subject says what happened; the body
is what saves someone six months from now. That skill has no ceiling.
