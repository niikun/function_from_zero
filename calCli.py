#!/usr/bin/env python3

from mylib.calc import add, sub, mul, div
import click

@click.group()
def cli():
    """A simple calculator"""

@cli.command("add")
@click.argument("x", type=float)
@click.argument("y", type=float)
def add_command(x, y):
    """Add two numbers
    Example:
    ./calCli.py add 2 3
    """
    #use colored output to print the result
    click.echo(click.style(f"{add(x, y)}", fg='green'))

@cli.command("sub")
@click.argument("x", type=float)
@click.argument("y", type=float)
def sub_command(x, y):
    """Subtract two numbers
    Example:
    ./calCli.py sub 2 3
    """
    click.echo(click.style(f"{sub(x, y)}", fg='green'))

@cli.command("mul")
@click.argument("x", type=float)
@click.argument("y", type=float)
def mul_command(x, y):
    """Multiply two numbers
    Example:
    ./calCli.py mul 2 3
    """
    click.echo(click.style(f"{mul(x, y)}", fg='green'))

@cli.command("div")
@click.argument("x", type=float)
@click.argument("y", type=float)
def div_command(x, y):
    """Divide two numbers
    Example:
    ./calCli.py div 2 3
    """
    click.echo(click.style(f"{div(x, y)}", fg='green'))


if __name__ == "__main__":
    cli()