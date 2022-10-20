def bracket(count, result='', left=0, right=0):
    if count == left and count == right:
        print(result)
    else:
        if left < count:
            bracket(count, result + '(', left + 1, right)
        if right < left:
            bracket(count, result + ')', left, right + 1)


if __name__ == '__main__':
    bracket(int(input()))