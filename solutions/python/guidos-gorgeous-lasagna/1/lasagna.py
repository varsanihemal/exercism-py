"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

EXPECTED_BAKE_TIME = 40;

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.
    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    bake_time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time;
    return bake_time_remaining;

#TODO (student): Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time (in minutes).
    """

    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total time spent so far.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed (in minutes).
    :return: int - preparation time plus baking time so far (in minutes).
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
