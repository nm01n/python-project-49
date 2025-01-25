#!/usr/bin/env python3
"""Module for running brain games."""

import prompt


def play_game(get_game_data, instruction):
    """
    Run the game logic for brain games.

    Args:
        get_game_data (callable): Function to generate game question and answer.
        instruction (callable): Function to display game instructions.
    """
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    instruction()
    rounds_count = 3

    for _ in range(rounds_count):
        question, correct_answer = get_game_data()
        print(f"Question: {question}")

        user_answer = prompt.string("Your answer: ")

        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
