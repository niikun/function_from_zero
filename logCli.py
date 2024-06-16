#!/usr/bin/env python
from mylib.logistics import distance, travel_time
import click
"""
This is a simple CLI tool to calculate the distance between two cities 
and the time it takes to travel between them at a given speed
"""

@click.group()
def cli():
    """A simple logistics calculator"""

@cli.command("distance")
@click.argument("city1", type=str)
@click.argument("city2", type=str)
def distance_command(city1, city2):
    """Calculate the distance between two cities
    Example:
    ./logCli.py distance Tokyo Nagoya
    """
    click.echo(click.style(f"{distance(city1, city2)} km", fg="green"))


@cli.command("travel_time")
@click.argument("city1", type=str)
@click.argument("city2", type=str)
@click.argument("speed", type=float)
def travel_time_command(city1, city2, speed):
    """Calculate the time it takes to travel between two cities at a given speed
    Example:
    ./logCli.py travel_time Tokyo Nagoya 100
    """
    click.echo(click.style(f"{travel_time(city1, city2, speed)} hours", fg="green"))    

if __name__ == "__main__":
    cli()
