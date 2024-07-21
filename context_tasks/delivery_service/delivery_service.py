def get_min_transport_platforms(values: list[int], limit: int) -> int:
    count = total_weight = left_pointer = 0
    values.sort()
    right_pointer = len(values) - 1

    if len(values) == 1:
        count += 1
        return count

    while left_pointer <= right_pointer:
        if (values[right_pointer] == limit or
                values[right_pointer] + values[left_pointer] > limit):
            count += 1
            right_pointer -= 1
            continue

        if left_pointer == right_pointer:
            count += 1
            break

        total_weight += values[left_pointer] + values[right_pointer]

        if total_weight <= limit:
            count += 1
            total_weight = 0
        elif total_weight > limit:
            count += 2
            total_weight = 0

        left_pointer += 1
        right_pointer -= 1

    return count


if __name__ == '__main__':
    with open('input.txt') as file_input:
        massive = file_input.readline().rstrip().rsplit(' ')
        limit = file_input.readline().rstrip()

    massive = [int(value) for value in massive]
    limit = int(limit)

    result = get_min_transport_platforms(massive, limit)

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
