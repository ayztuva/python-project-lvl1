#!/usr/bin/env python
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print(f'Hello, {name}!')


if __name__ == '__main__':
    main()
