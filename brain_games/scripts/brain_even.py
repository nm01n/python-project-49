#!/usr/bin/env python3
"""Script to run the Brain Even game."""

from brain_games.games.brain_even import get_game_data, instruction
from brain_games.games.engine import play_game


def main():
    """Run the Brain Even game."""
    play_game(get_game_data, instruction)


if __name__ == "__main__":
    main()
