# Номер посылки -

from string import digits, ascii_letters


def get_decoding_instructions(encrypted: str) -> str:
    """Функция декодирует и возвращает инструкцию"""
    result = str()
    repeat = str()
    repeat_in_bracket = str()
    commands = str()
    in_bracket = False
    brackets = ['[', ']']

    for char in encrypted:
        if char in digits and not in_bracket:
            repeat += char
            continue
        elif char in digits and in_bracket:
            repeat_in_bracket += char
        elif char in brackets:
            if char == brackets[1]:
                in_bracket = False
                result += commands * int(repeat)
                commands = str()
                repeat = str()
            else:
                in_bracket = True
        elif char in ascii_letters and in_bracket:
            commands += char
        elif char in ascii_letters and not in_bracket:
            result += char

    return result


if __name__ == '__main__':
    with open('input.txt') as file_input:
        encrypted_instructions = file_input.readline().rstrip()

    result = get_decoding_instructions(encrypted_instructions)

    print(result)
    # aaabcbc

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
