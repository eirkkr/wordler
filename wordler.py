"""
Wordler.
"""

import pathlib
import re
from typing import List, Tuple


class Wordler:
    """
    Wordler.
    """

    def __init__(self) -> None:

        self._all_words = self._load_word_list()
        self._words = self._load_word_list()

        _display_instructions()

        self._guess_words()

    def _load_word_list(self) -> List[str]:
        path = pathlib.Path(__file__).parent / "word_list.txt"

        # Load wordlist.
        with open(file=path, mode="r", encoding="utf-8") as file:
            words = file.readlines()

        # Remove newline characters.
        words = [line.strip() for line in words]

        return words

    def _guess_words(self) -> None:

        guess = self._guess_a_word()

        guesses = {guess[0]: guess[1]}

    def _guess_a_word(self) -> Tuple[str, str]:

        guess_is_valid = False
        score_is_valid = False

        valid_score_regex = r"[012]{5}"

        while not guess_is_valid:

            guess = input("Guess a word: ")

            if guess not in self._all_words:
                print("Invalid word.")
            else:
                guess_is_valid = True

        while not score_is_valid:

            score = input("Word score: ")

            if not re.match(pattern=valid_score_regex, string=score):
                print("Invalid score.")
            else:
                score_is_valid = True

        return guess, score


def _display_instructions() -> None:
    instructions = """
    Wordle Solver.
    """

    print(instructions)


if __name__ == "__main__":
    Wordler()
