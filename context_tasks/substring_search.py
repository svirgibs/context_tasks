def substring_search(target_string: str) -> int:
    max_string = str()
    count = 0
    max_count = 0
    left_pointer = 0
    right_pointer = len(target_string) - 1

    while left_pointer <= right_pointer:
        if target_string[left_pointer] not in max_string:
            max_string += target_string[left_pointer]
            count += 1
        else:
            max_string = max_string[max_string.index(target_string[left_pointer]) + 1:] + target_string[left_pointer]
            count = len(max_string)

        if count > max_count:
            max_count = count

        left_pointer += 1

    return max_count


if __name__ == '__main__':
    with open('input.txt') as file_input:
        target_string = file_input.readline().rstrip()

    result = substring_search(target_string)

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
