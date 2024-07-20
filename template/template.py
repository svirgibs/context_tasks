def main():
    pass


if __name__ == '__main__':
    with open('input.txt') as file_input:
        massive = file_input.readline().rstrip()

    result = main(massive)

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
