"""
Problem from TestGorilla interview.
"""


def rotate_word(word, num):
    """Rotates word or sentence. Only change lower or upper chars."""
    rotated = ""
    num = num % 26
    for c in word:
        ic = ord(c)
        if ic >= ord("a") and ic <= ord("z"):
            ic += num
            while ic > ord("z"):
                ic -= 26
        elif ic >= ord("A") and ic <= ord("Z"):
            ic += num
            while ic > ord("Z"):
                ic -= 26
        rotated += chr(ic)
    return rotated


def get_rotation_diff(word1, word2):
    """See difference in rotation of first char of words. Ret -1 if too far apart."""
    if len(word1) == 0 or len(word2) == 0:
        return -1
    c1, c2 = word1[0], word2[0]
    diff = ord(c2) - ord(c1)
    if abs(diff) >= 26:
        return -1
    return diff % 26  # handle negatives


def split_in_words(text):
    """Handle chars that are not spaces on split."""
    words = text.split(" ")
    split = []
    for word in words:
        if word.isalnum():
            split.append(word)
            continue
        t = ""
        for c in word:
            if c.isalnum():
                t += c
            else:
                if len(t) > 0:
                    split.append(t)
                t = ""
        if len(t) > 0:
            split.append(t)
    return split


def decipher(ciphertext, knownWord):
    words = split_in_words(ciphertext)
    for word in words:
        if len(word) != len(knownWord):
            continue
        diff = get_rotation_diff(word, knownWord)
        if diff == -1:
            continue
        rotated = rotate_word(word, diff)
        if rotated == knownWord:
            return rotate_word(ciphertext, diff)
    return "Invalid"


def decipher2(ciphertext, knownWord):
    # Another way of doing it
    for i in range(26):
        word = rotate_word(knownWord, i)
        start = 0
        while True:
            idx = ciphertext.find(word, start)
            if idx == -1:
                break
            before = (idx == 0 or not ciphertext[idx - 1].isalpha())
            after = (idx + len(word) == len(ciphertext) or not ciphertext[idx + len(word)].isalpha())
            if before and after:
                return rotate_word(ciphertext, -i)
            start = idx + 1
        return "Invalid"


if __name__ == "__main__":
    ciphertext = "Eqfkpi vguvu, qj agcj, ctg xgta hwp! Lwuv vta kv :)"
    for known_word in ["fun", "very", "try", "tryy", "ver", "potato", "it"]:
        r = decipher(ciphertext, known_word)
        print(known_word, "-->", r)
