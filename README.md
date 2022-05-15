# Wordler

## Algorithm

### Step 1: Match word that have each letter in each position.

```python
pattern_a = r"[a..z][a..z][a..z][a..z][a..z]"
```

### Step 2: From the remaining words, match words that that have at least x number of each letter.

```python
# Unsure if this is correct.
pattern_b = r"(?=a{0,5}(?=b{0,5}(?=c{0,5}...(?=y{0,5}(?=z{0,5}"
```

### Step 3: User makes a guess and enters a score.

e.g:

guess = "pants" (entered by user)

score = "00012" (entered by user)

* 0 = incorrect letter
* 1 = correct letter, wrong position
* 2 = correct letter, correct position

### Step 4: Update patterns.

This won't work, need more thought...

For each position:
* If `letter_score = "2"`:
    * Update `pattern_a` to match exactly this letter for the position.

Then...

For each unique letter than appeared in the guess, count the number of nonzero guesses.
* If `count_of_nonzero_letter_scores = "0"`:
    * Update `pattern_b` to drop the maximum score for that letter to `"0"`.
* If `letter_score = "1"`:

## Notes

Rather than modifying the regex each guess, an object could be modified, then a new regex generated from this object each iteration.
