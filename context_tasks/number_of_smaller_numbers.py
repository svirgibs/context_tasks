def main(values: list) -> list:
    result = []
    for value_1 in values:
        count = 0
        for value_2 in values:
            if value_2 < value_1:
                count += 1
        result.append(count)
    return result


if __name__ == '__main__':
    with open('input.txt') as file_input:
        massive = file_input.readline().rstrip().rsplit(' ')

    values = [int(value) for value in massive]

    result = main(values)

    result = [str(value) for value in result]

    with open('output.txt', 'w') as file_output:
        file_output.write(' '.join(result))
