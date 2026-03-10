"""Command-line entry points for common WB Analytics workflows."""
import click

from wb_analytics.poverty_calc import poverty_rate


@click.group()
def main():
    """WB Analytics command-line interface."""


@main.command("poverty-rate")
@click.argument("incomes", nargs=-1, type=float)
def poverty_rate_cmd(incomes):
    """Compute the poverty rate for a list of INCOMES."""
    click.echo(poverty_rate(list(incomes)))


if __name__ == "__main__":
    main()
