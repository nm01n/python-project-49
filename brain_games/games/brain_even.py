#!/usr/bin/env python3
"""Module for the Brain Even game."""

import random


def get_game_data():
    """
    Generate a random number and determine if it's even.

    Returns:
        tuple: A tuple containing the number and its evenness.
    """
    number = random.randint(1, 100)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return str(number), correct_answer


def instruction():
    """Display game instructions."""
    return 'Answer "yes" if the number is even, otherwise answer "no".'
