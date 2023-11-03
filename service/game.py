import data.game as data

HIT = "H "  # right letter and position
MISS = "M"  # letter not in word
CLOSE = "C" # letter in word but wrong position

def get_word() -> str:
    return data.get_word()

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
