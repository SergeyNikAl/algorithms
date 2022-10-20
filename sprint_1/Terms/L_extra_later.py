def get_excessive_letter(shorter: str, longer: str) -> str:
    for i in shorter:
        if i in longer:
            longer = longer.replace(i, '', 1)
    return longer


if __name__ == '__main__':
    print(get_excessive_letter(input().strip(), input().strip()))
