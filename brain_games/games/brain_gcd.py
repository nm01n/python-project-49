"""Module for the Brain GCD game."""

import random
import math


def get_game_data():
    """
    Generate question and correct answer for GCD game.

    Returns:
        tuple: Question and correct GCD answer.
    """
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)

    question = f"{number1} {number2}"
    correct_answer = str(math.gcd(number1, number2))

    return question, correct_answer


def instruction():
    """Display game instructions."""
    return "Find the greatest common divisor of given numbers."
