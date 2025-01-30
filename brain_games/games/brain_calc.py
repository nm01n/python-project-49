#!/usr/bin/env python3
"""Module for the Brain Calc game."""

import random


MIN_GEN_NUMBER = 1
MAX_GEN_NUMBER = 100
OPERATORS = ("+", "-", "*")


def calculate(number1, number2, operator):
    """
    Calculate the result of arithmetic operation.

    Args:
        number1: First number
        number2: Second number
        operator: String with arithmetic operator ('+', '-', '*')

    Returns:
        int: Result of the operation
    """
    if operator == "+":
        return number1 + number2
    if operator == "-":
        return number1 - number2
    if operator == "*":
        return number1 * number2
    raise ValueError(f"Unknown operator: {operator}")


def get_game_data():
    """
    Generate a math expression and its solution.

    Returns:
        tuple: Expression and correct answer as a string.
    """
    number_1 = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    number_2 = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    current_operator = random.choice(OPERATORS)

    expression = f"{number_1} {current_operator} {number_2}"
    correct_answer = calculate(number_1, number_2, current_operator)

    return expression, str(correct_answer)


def instruction():
    """Return game instructions."""
    return "What is the result of the expression?"
