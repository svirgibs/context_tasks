"""Рабочее решение задачи на Яндекс Контесте: 116278138"""


def get_min_transport_platforms(values: list[int], limit: int) -> int:
    platform_count = left_pointer = 0
    values.sort()
    right_pointer = len(values) - 1

    while left_pointer <= right_pointer:
        total_weight = values[left_pointer] + values[right_pointer]
        if total_weight <= limit:
            left_pointer += 1
        platform_count += 1
        right_pointer -= 1
    return platform_count


if __name__ == '__main__':
    """Запуск функции расчета минимального числа платформ."""

    with open('input.txt') as file_input:
        massive = file_input.readline().rstrip().rsplit(' ')
        limit = file_input.readline().rstrip()

    massive = [int(value) for value in massive]
    limit = int(limit)

    result = get_min_transport_platforms(massive, limit)

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
