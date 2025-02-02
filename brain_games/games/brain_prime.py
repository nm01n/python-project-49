"""Module for the Brain Prime game."""

import random
import math


MIN_GEN_NUMBER = 1
MAX_GEN_NUMBER = 100


def is_prime(number):
    """
    Check if a number is prime.

    Args:
        number (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def generate_prime_challenge():
    """
    Generate a number and its primality status.

    Returns:
        tuple: Number and primality answer.
    """
    number = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    correct_answer = "yes" if is_prime(number) else "no"

    return str(number), correct_answer


def get_game_data():
    """
    Prepare game data for a single round.

    Returns:
        tuple: Game question and correct answer.
    """
    return generate_prime_challenge()


def game_instruction():
    """Display game instructions."""
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'
