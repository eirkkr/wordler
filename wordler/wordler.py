#!/usr/bin/env python
"""
Wordler.
"""

import pathlib
import re
import string
from typing import List
from typing import Dict

# Letters per word.
_LETTERS: int = 5

# Number of guesses allowed.
_GUESSES: int = 6


class Wordler:
    """
    Wordler.
    """

    def __init__(self) -> None:

        _display_instructions()

        self._all_words = _load_word_list()
        self._words = _load_word_list()
        self._guesses: Dict[str, str] = {}

        # Create list of possible letters for each position.
        alphabet = string.ascii_lowercase
        self._letters = []
        for i in range(_LETTERS):
            self._letters.append(alphabet)

        # Construct regular expression to test words.
        self._regex = ""

        for i in range(_LETTERS):
            self._regex = rf"{self._regex}[{self._letters[i]}]"

    def main(self) -> None:
        """
        Wordler.
        """

        while len(self._guesses) < _GUESSES:
            self._guess_a_word()
            self._update_regex()
            self._update_words()

            print(f"Valid letters: {self._letters}")
            print(f"{len(self._words)} valid word(s) remain: {self._words}")

            # Exit i
            if self._guesses[list(self._guesses.keys())[-1]] == "22222":
                print(
                    f"Congratulations, you solved the puzzle in {len(self._guesses)} "
                    "guess(es)!"
                )
                break

    def _guess_a_word(self):

        guess_is_valid = False
        score_is_valid = False
        valid_score_regex = r"[012]{5}"

        # Ask for a guess from user.
        while not guess_is_valid:

            guess = input("Guess a word: ")

            if guess not in self._all_words:
                print("Word not in word list, try again.")
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

        self._update_letters(guess, score)

    # TODO: Validate score, e.g. can't say 2 of the same letter is correct.

    def _update_letters(self, guess, score) -> None:
        # TODO: This is incomplete, it currently only checks if a letter is
        # correct. It needs to also check for things such as letters which can
        # be removed from all spots (score of zero).
        #
        # In addition, it might need a separate regex to check for matches on
        # letters which are correct but in the wrong spot.

        for i in range(_LETTERS):
            if score[i] == "2":
                self._letters[i] = guess[i]
            else:
                self._letters[i] = self._letters[i].replace(guess[i], "")

    def _update_regex(self) -> None:

        self._regex = ""

        for i in range(_LETTERS):
            self._regex = rf"{self._regex}[{self._letters[i]}]"

    def _update_words(self) -> None:

        new_words = []
        pattern = re.compile(self._regex)

        for word in self._words:
            if pattern.match(word):
                new_words.append(word)

        self._words = new_words


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
