#!/usr/bin/env python3
"""Module for the Brain GCD game."""

import random
import math


def get_game_data():
    """
    Generate question and correct answer for GCD game.

    Returns:
        tuple: A tuple containing the question and correct GCD answer.
    """
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)

    question = f"{number1} {number2}"
    correct_answer = str(math.gcd(number1, number2))

    return question, correct_answer


def instruction():
    """Display game instructions."""
    print("Find the greatest common divisor of given numbers.")


def main():
    """Run the Brain GCD game."""
    from brain_games.games.engine import play_game

    play_game(get_game_data, instruction)


if __name__ == "__main__":
    main()
