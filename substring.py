def generateAllSubstrings(word):
    length = len(word)
    for i in range(length):
        for j in range(i + 1, length + 1):
            yield(word[i: j])


def getAllSubstrings(word):
    length = len(word)
    return [word[i: j] for i in range(length) for j in range(i + 1, length + 1)]


def generateOneCharacterChangedWord(word):
    length = len(word)
    for idx in range(length):
        for o in range(ord('a'), ord('z') + 1):
            c = chr(o)
            if c != word[idx]:
                yield word[: idx] + c + word[idx + 1: ]
