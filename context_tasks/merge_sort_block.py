def merge_sort_block(n: int, massive: list[int]) -> int:
    blocks = 0
    max_value = -1
    for i in range(n):
        max_value = max(max_value, massive[i])
        if max_value == i:
            blocks += 1

    return blocks


if __name__ == '__main__':
    with open('input.txt') as file_input:
        n = int(file_input.readline().rstrip())
        massive = file_input.readline().rstrip().rsplit()

    massive = [int(x) for x in massive]

    result = merge_sort_block(n, massive)

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
