"""
Wordler.
"""

import pathlib
import re
from typing import List
from typing import Dict


class Wordler:
    """
    Wordler.
    """

    def __init__(self) -> None:

        self._all_words = _load_word_list()
        self._words = _load_word_list()
        self._guesses: Dict[str, str] = {}

        _display_instructions()

    def main(self) -> None:
        """
        Wordler.
        """

        while len(self._guesses) < 6:
            self._guess_a_word()

    def _guess_a_word(self):

        guess_is_valid = False
        score_is_valid = False

        valid_score_regex = r"[012]{5}"

        # Ask for a guess from user.
        while not guess_is_valid:

            guess = input("Guess a word: ")

            if guess not in self._all_words:
                print("Invalid word.")
            else:
                guess_is_valid = True

        # Ask for a score from user.
        while not score_is_valid:

            score = input("Word score: ")

            if not re.match(pattern=valid_score_regex, string=score):
                print("Invalid score.")
            else:
                score_is_valid = True

        self._guesses[guess] = score

        print(self._guesses)


def _load_word_list() -> List[str]:
    path = pathlib.Path(__file__).parent / "word_list.txt"

    # Load wordlist.
    with open(file=path, mode="r", encoding="utf-8") as file:
        words = file.readlines()

    # Remove newline characters.
    words = [line.strip() for line in words]

    return words


def _display_instructions() -> None:
    instructions = """
    Wordle solver.
    """

    print(instructions)


if __name__ == "__main__":
    Wordler().main()
