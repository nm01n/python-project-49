# brain_games/scripts/brain_even.py
#!/usr/bin/env python3

import random

def generate_progression():
    """Generate an arithmetic progression."""
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    
    progression = [start + i * step for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    
    progression_display = progression.copy()
    progression_display[hidden_index] = '..'
    
    question = ' '.join(map(str, progression_display))
    
    return question, correct_answer

def get_game_data():
    """Prepare game data for a single round."""
    return generate_progression()

def game_instruction():
    """Display game instructions."""
    print('What number is missing in the progression?')

def main():
    from brain_games.games.engine import play_game
    play_game(get_game_data, game_instruction)

if __name__ == '__main__':
    main(