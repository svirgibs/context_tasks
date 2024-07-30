class Number:
    def __init__(self, value: int, in_pattern: bool = False):
        self.value = value
        self.in_pattern = in_pattern

    def __repr__(self):
        return repr(self.value)


def sort_by_pattern(
        numbers: list[int],
        pattern_values: list[int]
):
    numbers = [Number(x) for x in numbers]

    pattern_numbers = []
    for pattern_value in pattern_values:
        for number in numbers:
            if number.value == pattern_value:
                pattern_numbers.append(number.value)
                number.in_pattern = True

    numbers_not_in_pattern = []
    for number in numbers:
        if number.in_pattern is False:
            numbers_not_in_pattern.append(number.value)

    numbers_not_in_pattern.sort()

    return pattern_numbers + numbers_not_in_pattern


if __name__ == '__main__':
    with open('input.txt') as file_input:
        amount_numbers = int(file_input.readline().rstrip())
        numbers = file_input.readline().rstrip().rsplit(' ')
        len_pattern = int(file_input.readline().rstrip())
        pattern_values = file_input.readline().rstrip().rsplit(' ')

    numbers = [int(x) for x in numbers]
    pattern_values = [int(x) for x in pattern_values]

    result = sort_by_pattern(numbers, pattern_values)

    result = [str(x) for x in result]
    with open('output.txt', 'w') as file_output:
        file_output.write(' '.join(result))
