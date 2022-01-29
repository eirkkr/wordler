"""
Gets list of 5 letter words and saves as .csv.
"""
import csv
import pathlib


from typing import List


def _main() -> None:

    words = _load_words()
    words = _filter_to_five_letter_words(words)
    _export_to_csv(words)


def _load_words() -> List[str]:

    path = pathlib.Path(__file__).parent / "words_alpha.txt"

    with open(file=path, mode="r", encoding="utf-8") as file:
        words = file.readlines()

    return words


def _filter_to_five_letter_words(words: List[str]) -> List[str]:

    five_letter_words: List[str] = []

    for word in words:
        if len(word) == 6:
            five_letter_words.append(word)

    words = [word.strip() for word in five_letter_words]

    return words


def _export_to_csv(words: List[str]) -> None:

    path = pathlib.Path(__file__).parent / "five_letter_words.csv"

    with open(file=path, mode="w+", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows([words])


if __name__ == "__main__":
    _main()
