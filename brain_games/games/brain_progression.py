#!/usr/bin/env python3
"""Module for the Brain Progression game."""

import random


MIN_START_NUMBER = 1
MAX_START_NUMBER = 100
MIN_STEP_NUMBER = 1
MAX_STEP_NUMBER = 10
PROGRESSION_LENGTH = 10


def generate_progression(start, step, length):
    """
    Generate an arithmetic progression.

    Args:
        start: First number in progression
        step: Difference between consecutive numbers
        length: Length of progression

    Returns:
        list: Generated arithmetic progression
    """
    return [start + i * step for i in range(length)]


def get_game_data():
    """
    Prepare game data for a single round.

    Returns:
        tuple: Game question and correct answer.
    """
    start = random.randint(MIN_START_NUMBER, MAX_START_NUMBER)
    step = random.randint(MIN_STEP_NUMBER, MAX_STEP_NUMBER)

    progression = generate_progression(start, step, PROGRESSION_LENGTH)
    hidden_index = random.randint(0, PROGRESSION_LENGTH - 1)
    correct_answer = str(progression[hidden_index])

    progression_display = progression.copy()
    progression_display[hidden_index] = ".."
    question = " ".join(map(str, progression_display))

    return question, correct_answer


def game_instruction():
    """Return game instructions."""
    return "What number is missing in the progression?"
