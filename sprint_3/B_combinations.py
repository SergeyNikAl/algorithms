from typing import List, Union

SYMBOLS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def create_pairs(sequence: List[List[str]]) -> Union[List, List[str]]:
    if not sequence:
        return [[]]
    return [
        [symb_1] + symb_2 for symb_1 in sequence[0]
        for symb_2 in create_pairs(sequence[1:])
    ]


if __name__ == '__main__':
    sequence = list([SYMBOLS[number] for number in input()])
    result = create_pairs(sequence)
    print(*[''.join(pair) for pair in result])