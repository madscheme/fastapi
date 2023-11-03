HIT = "H"
MISS = "M"
CLOSE = "C"  # (letter is in the word, but at another position)

def get_score(word: str, guess: str) -> str:
    word = word.lower()
    guess = guess.lower()
    score: str = ""
    if len(word) == len(guess):
        for pos, letter in enumerate(guess):
            if letter in word:
                if letter == word[pos]:
                    score += HIT
                else:
                    score += CLOSE
            else:
                score += MISS
    return score
