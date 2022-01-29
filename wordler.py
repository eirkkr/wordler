def main() -> None:

    # Read in words.
    with open("words_alpha.txt") as file:
        words = file.readlines()

    # Strip newline characters.
    words = [word.strip() for word in words]

    five_letter_words = []

    for word in words:
        if len(word) == 5:
            five_letter_words.append(word)


if __name__ == "__main__":
    main()
