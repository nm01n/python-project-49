#!/usr/bin/env python3
"""Module for the Brain Even game."""

import random
from brain_games.games.engine import play_game


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
    print('Answer "yes" if the number is even, otherwise answer "no".')


def main():
    """Run the Brain Even game."""
    play_game(get_game_data, instruction)


if __name__ == "__main__":
    main()