def get_min_transport_platforms(massive: list[int], limit: int) -> int:
    pass


if __name__ == '__main__':
    with open('input.txt') as file_input:
        massive = file_input.readline().rstrip()
        limit = file_input.readline().rstrip()

    values = [int(value) for value in massive]
    limit = int(limit)

    result = get_min_transport_platforms(values, limit)

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
