def main(generation):
    if generation in (0, 1):
        return 1
    return main(generation - 1) + main(generation - 2)


if __name__ == '__main__':
    with open('input.txt') as file_input:
        number = int(file_input.readline().rstrip())

    result = main(number)

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
