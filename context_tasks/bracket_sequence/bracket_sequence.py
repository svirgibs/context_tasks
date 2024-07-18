def is_correct_bracket_seq(check_string: str) -> bool:
    if len(check_string) == 0:
        return True
    if len(check_string) % 2:
        return False

    correct = {
        ']': '[',
        '}': '{',
        ')': '('
    }

    list_tmp = []

    for i in check_string:
        if i in correct.values():
            list_tmp.append(i)
            continue
        if len(list_tmp) and correct[i] == list_tmp[-1]:
            list_tmp.pop()
            continue
        return False

    if len(list_tmp) == 0:
        return True

    return False


if __name__ == '__main__':
    with open('input.txt') as file_input:
        str_line = file_input.readline().rstrip()

    result = is_correct_bracket_seq(str_line)

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
