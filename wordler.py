"""
Wordler.
"""
import csv
import pathlib


class Wordler:
    """
    Wordler.
    """

    def __init__(self) -> None:

        path = pathlib.Path(__file__).parent / "five_letter_words.csv"

        with open(file=path, mode="r", encoding="utf-8") as file:
            possible_words = csv.reader(file, delimiter="")
