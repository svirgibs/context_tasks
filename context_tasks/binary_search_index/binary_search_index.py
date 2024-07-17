def get_index(values: list[int], current_value: int) -> int:
    values.sort()
    left = 0
    right = len(values)

    while left < right:
        mid = (left + right) // 2
        values[mid] = values[mid]
        if current_value == values[mid]:
            for i, x in enumerate(values[:mid]):
                if x == current_value:
                    return i
            return mid
        if current_value > values[mid]:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == '__main__':
    with open('input.txt') as f_input:
        massive = f_input.readline().rstrip().rsplit(' ')
        target = f_input.readline().rstrip()

    values = [int(value) for value in massive]
    target = int(target)

    result = get_index(values, target)

    print(result)
    with open('output.txt', 'w') as f_output:
        f_output.write(str(result))
