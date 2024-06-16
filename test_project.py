from mylib.calc import add, sub, mul, div
from calCli import cli
from click.testing import CliRunner

import pytest


# write test for each function in calc.py


def test_add():
    assert add(2, 3) == 5
    assert add(2, -3) == -1
    assert add(2, 0) == 2
    assert add(0, 0) == 0


def test_sub():
    assert sub(2, 3) == -1
    assert sub(2, -3) == 5
    assert sub(2, 0) == 2
    assert sub(0, 0) == 0


def test_mul():
    assert mul(2, 3) == 6
    assert mul(2, -3) == -6
    assert mul(2, 0) == 0
    assert mul(0, 0) == 0


def test_div():
    assert div(2, 3) == 2 / 3
    assert div(2, -3) == 2 / -3
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        div(2, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        div(0, 0)


# test the cli function


def test_cli_add():
    runner = CliRunner()
    result = runner.invoke(cli, ["add", "2", "3"])
    assert result.exit_code == 0
    assert result.output == "5.0\n"


def test_cli_sub():

    runner = CliRunner()
    result = runner.invoke(cli, ["sub", "2", "3"])
    assert result.exit_code == 0
    assert result.output == "-1.0\n"


def test_cli_mul():

    runner = CliRunner()
    result = runner.invoke(cli, ["mul", "2", "3"])
    assert result.exit_code == 0
    assert result.output == "6.0\n"


def test_cli_div():

    runner = CliRunner()
    result = runner.invoke(cli, ["div", "2", "3"])
    assert result.exit_code == 0
    assert result.output == "0.6666666666666666\n"

    result = runner.invoke(cli, ["div", "2", "0"])
    assert result.exit_code == 1
    assert isinstance(result.exception, ValueError)
    assert str(result.exception) == "Cannot divide by zero!"

    result = runner.invoke(cli, ["div", "0", "0"])
    assert result.exit_code == 1
    assert isinstance(result.exception, ValueError)
    assert str(result.exception) == "Cannot divide by zero!"
