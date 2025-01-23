# brain_games/games/brain_gcd.py
#!/usr/bin/env python3

import random
import math
from brain_games.games.engine import play_game

def get_game_data():
    """Generate question and correct answer for GCD game."""
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    
    question = f"{number1} {number2}"
    correct_answer = str(math.gcd(number1, number2))
    
    return question, correct_answer

def instruction():
    """Print game instructions."""
    print('Find the greatest common divisor of given numbers.')

def main():
    play_game(get_game_data, instruction)

if __name__ == '__main__':
    main()