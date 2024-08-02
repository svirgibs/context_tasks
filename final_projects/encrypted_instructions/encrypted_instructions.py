"""ID посылки - 116588291"""

from string import digits


def get_decoding_instructions(encrypted: str) -> str:
    """Функция декодирует и возвращает строку с инструкцией."""
    commands: list = []
    repeats: list = []
    current_command: str = str()

    for char in encrypted:
        if char in digits:
            repeats.append(char)
        elif char == '[':
            commands.append((current_command, repeats))
            current_command = str()
            repeats = []
        elif char == ']':
            last_command, last_repeats = commands.pop()
            current_command = last_command + current_command * int(''.join(last_repeats))
        else:
            current_command += char
    return current_command


if __name__ == '__main__':
    with open('input.txt') as file_input:
        encrypted_instructions = file_input.readline().rstrip()

    result = get_decoding_instructions(encrypted_instructions)

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
