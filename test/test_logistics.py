from mylib.logistics import distance, travel_time, cities, total_distance, find_best_route
from logCli import cli
from click.testing import CliRunner
import pytest

"""
This module tests the logistics.py and logCli.py modules
"""

# test the logistics.py module

def test_distance():
    assert distance("Tokyo", "Yokohama") == 27.702837848148494
    assert distance("Tokyo", "Osaka") == 397.1830862160771

def test_travel_time():
    assert travel_time("Tokyo", "Yokohama", 100) == 0.2770283784814849
    assert travel_time("Tokyo", "Osaka", 100) == 3.9718308621607705
    

# test the logCli.py module

def test_distance_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["distance", "Tokyo", "Yokohama"])
    assert result.exit_code == 0
    assert result.output == "27.702837848148494 km\n"

def test_travel_time_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["travel_time", "Tokyo", "Yokohama", "100"])
    assert result.exit_code == 0
    assert result.output == "0.2770283784814849 hours\n"