"""Script to run the Brain GCD game."""

from brain_games.games.brain_gcd import get_game_data, instruction
from brain_games.games.engine import play_game


def main():
    """Run the Brain GCD game."""
    play_game(get_game_data, instruction)


if __name__ == "__main__":
    main()
