#!/usr/bin/env python3
"""Script to run the Brain Progression game."""

from brain_games.games.brain_progression import get_game_data, game_instruction
from brain_games.games.engine import play_game


def main():
    """Run the Brain Progression game."""
    play_game(get_game_data, game_instruction)


if __name__ == "__main__":
    main()
