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

        self._regex = f"^{self._regex}$"

    def main(self) -> None:
        """
        Wordler.
        """

        while len(self._guesses) < 6:
            self._guess_a_word()
            self._update_letters()
            self._update_words()
            print(f"Valid letters: {self._letters}")
            print(f"{len(self._words)} valid words remain.")

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

    def _update_letters(self) -> None:

        for i in range(_LETTERS):
            print(i)

            for letter in self._guesses:
                if letter[i] == "2":
                    self._letters[i] = letter
                else:
                    self._letters[i].replace(letter, "")

    def _update_words(self) -> None:

        # new_word_list = self._words

        # for letter in self._letters:
        #     for word in self._words:
        #         if letter in word

        pass


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
