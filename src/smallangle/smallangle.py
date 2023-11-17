"""
Small angle approximation

Ruben Gersons
"""

import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of times",
    show_default=True
)
def sin(number):
    """Gets the sin values from 0 to 2 pi over a [number] of steps

    Args:
        number (int): the number of equally spaced steps between 0 and 2 pi
    """
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of times",
    show_default=True
)
def tan(number):
    """Gets the cos values from 0 to 2 pi over a [number] of steps

    Args:
        number (int): the number of equally spaced steps between 0 and 2 pi
    """
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return

@cmd_group.command()
@click.argument("error")
def approx(error):
    """Find the maximum angle for which the sin approximation holds at a given accuracy

    Args:
        error (float): the accuracy for which to find the maximum angle
    Returns:
        float: the maximum angle for which the approximation holds given the accuracy
    """
    x = 0

    while abs(x - np.sin(x)) < float(error):
        x += 0.001

    print(f"For an accuracy of {error}, the small-angle approximation holds up to x = {np.round(x, 3)}.")
    return x

if __name__ == "__main__":
    cmd_group()