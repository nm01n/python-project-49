#!/usr/bin/env python3
"""Module for running brain games."""

import prompt


ROUNDS_COUNT = 3


def play_game(get_game_data, instruction):
    """
    Run the game logic for brain games.

    Args:
        get_game_data (func): Generates game question and answer.
        instruction (func): Displays game instructions.
    """
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print(instruction())

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = get_game_data()
        print(f"Question: {question}")

        user_answer = prompt.string("Your answer: ")

        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
