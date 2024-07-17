def main():
    pass


if __name__ == '__main__':
    with open('input.txt') as file_input:
        a = int(file_input.readline())
        b = int(file_input.readline())
    result = main()

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
