# brain_games/scripts/brain_calc.py
#!/usr/bin/env python3

import prompt
import random
from brain_games.games.engine import play_game 

def get_game_data():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    operators = ['+', '-', '*']
    current_operator = random.choice(operators)
    
    expression = f'{number_1} {current_operator} {number_2}'
    
    if current_operator == '+':
        correct_answer = number_1 + number_2
    elif current_operator == '-':
        correct_answer = number_1 - number_2
    else:
        correct_answer = number_1 * number_2
    
    return expression, str(correct_answer)

def instruction():
    print('What is the result of the expression?')

def main():
    """Script entry point."""
    play_game(get_game_data, instruction)

if __name__ == '__main__':
    main()