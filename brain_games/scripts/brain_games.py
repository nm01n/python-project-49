#!/usr/bin/env python3
"""Script that runs Brain Games."""

from brain_games.cli import welcome_user


def main():
    """Run the Brain Games."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
