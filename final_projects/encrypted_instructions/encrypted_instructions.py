# Номер посылки -

def get_decoding_instructions(encrypted_instructions: str) -> str:
    """Функция декодирует и возвращает инструкцию"""
    result = str()
    
    return result


if __name__ == '__main__':
    with open('input.txt') as file_input:
        encrypted_instructions = file_input.readline().rstrip()

    result = get_decoding_instructions(encrypted_instructions)

    print(result)
    # aaabcbc

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
