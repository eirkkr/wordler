"""
Gets list of all five letter words from 
"""

from typing import List


def main() -> None:

    words = _load_words()
    words = _get_five_letter_words(words)

    print(words)


def _load_words() -> List[str]:

    with open("words_alpha.txt") as file:
        words = file.readlines()

    return words


def _get_five_letter_words(words: List[str]) -> List[str]:

    five_letter_words: List[str] = []

    for word in words:
        if len(word) == 5:
            five_letter_words.append(word)

    words = [word.strip() for word in words]

    return five_letter_words


if __name__ == "__main__":
    main()
