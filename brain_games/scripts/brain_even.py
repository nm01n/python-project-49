# brain_games/scripts/brain_even.py
#!/usr/bin/env python3

import prompt
import random

def is_even(number):
    return number % 2 == 0

def get_game_data():
    question = random.randint(1, 100)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer

def play_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Answer "yes" if the number is even, otherwise answer "no".')

    rounds_count = 3
    
    for _ in range(rounds_count):
        question, correct_answer = get_game_data()
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return 
        
        print('Correct!')

    print(f'Congratulations, {name}!')

def main():
    """Script entry point."""
    play_game()


if __name__ == '__main__':
    main()