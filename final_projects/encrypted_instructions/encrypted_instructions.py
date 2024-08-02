"""ID посылки - 116586096"""

from string import digits


def get_decoding_instructions(encrypted: str) -> str:
    """Функция декодирует и возвращает строку с инструкцией."""
    commands: list = []
    repeat: str = str()
    current_command: str = str()

    for char in encrypted:
        if char in digits:
            repeat += char
        elif char == '[':
            commands.append((current_command, repeat))
            current_command = str()
            repeat = str()
        elif char == ']':
            last_command, last_repeat = commands.pop()
            current_command = last_command + current_command * int(last_repeat)
        else:
            current_command += char
    return current_command


if __name__ == '__main__':
    with open('input.txt') as file_input:
        encrypted_instructions = file_input.readline().rstrip()

    result = get_decoding_instructions(encrypted_instructions)

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
