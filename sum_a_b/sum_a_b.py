def main(a, b):
    return a + b


if __name__ == '__main__':
    with open('input.txt') as f_input:
        a = int(f_input.readline())
        b = int(f_input.readline())
    result = main(a, b)

    with open('output.txt', 'w') as f_output:
        f_output.write(str(result))
