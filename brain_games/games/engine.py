# brain_games/games/engine.py
#!/usr/bin/env python3

import prompt

def play_game(get_game_data, instruction):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    instruction()
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
