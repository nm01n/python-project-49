# brain_games/games/brain_prime.py
#!/usr/bin/env python3

import random
import math

def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def generate_prime_challenge():
    """Generate a number and determine whether it's prime."""
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    
    return str(number), correct_answer

def get_game_data():
    """Prepare game data for a single round."""
    return generate_prime_challenge()

def game_instruction():
    """Display game instructions."""
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

def main():
    from brain_games.games.engine import play_game
    play_game(get_game_data, game_instruction)

if __name__ == '__main__':
    main()