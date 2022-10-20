from typing import List, Tuple


def get_longest_word(line: List[str]) -> Tuple[str, int]:
    line.sort(key=len, reverse=True)
    return line[0], len(line[0])


input()
print(*get_longest_word(input().strip().split()), sep='\n')