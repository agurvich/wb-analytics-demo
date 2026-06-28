# Contributing

1. Create a branch off `main`.
2. Run `make setup` to install dependencies and pre-commit hooks.
3. Run `make test` and `make lint` before opening a PR.
4. Follow the commit message conventions below.

## Commit message conventions

| Prefix | Meaning |
|---|---|
| `fix:` | Corrects incorrect behavior or a calculation that was wrong |
| `hotfix:` | Urgent, production-impacting correction, usually forked from main |
| `new:` | New capability, indicator, or feature; additive, non-breaking |
| `git:` | Tracking a newly added file into version control (not a code change) |
| `docs:` | Documentation-only changes |
| `style:` | Cosmetic/visual changes (charts, colors, formatting), no data/logic change |
| `whitespace:` | Pure formatting/indentation changes, zero semantic change |
| `refactor:` | Internal restructuring, no change to output values or public behavior |
| `data:` | Data refresh/update (new vintage, new source), not a code change |
| `breaking:` | Methodology or schema change that breaks comparability or downstream consumers |
| `perf:` | Performance improvement, no change to output values |
| `ci:` | Changes to CI/workflow configuration only |
| `chore:` | Maintenance with no behavior change, e.g. dependency bumps and tooling |

A commit history built on these prefixes doubles as an analytical audit
trail: a reviewer (or a future you) can tell from `git log --oneline`
alone which changes are safe to pull in blindly and which ones require
re-checking downstream numbers.

## Docstrings

Public functions use [NumPy-style
docstrings](https://numpydoc.readthedocs.io/en/latest/format.html): a
one-line summary, then `Parameters` and `Returns`, and a `Notes` section
wherever a methodology choice changes the number. One style across the
repo matters more than which style it is.

```python
def poverty_rate(incomes, line=POVERTY_LINE_USD_PPP):
    """Share of the population living below the poverty line.

    Parameters
    ----------
    incomes : list of float
        One daily income per person, in 2017 PPP dollars.
    line : float, optional
        The poverty line, in 2017 PPP dollars a day.

    Returns
    -------
    float
        The headcount ratio, between 0 and 1.
    """
```

Older modules predate this. Convert a function's docstring when you next
change that function, not in a separate sweep.
