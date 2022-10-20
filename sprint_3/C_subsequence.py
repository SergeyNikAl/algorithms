def definition_subsequence(subsequence, sequence):
    left = 0
    for letter in subsequence:
        try:
            right = sequence.index(letter, left)
        except:
            return False
        left = right + 1
    return True


if __name__ == '__main__':
    print(definition_subsequence(input(), input()))