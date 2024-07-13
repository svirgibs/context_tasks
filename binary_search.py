wins = [1223125, 2128437, 2128500, 2741001, 4567687, 4567890, 7495938, 9314543]
strs = ['алгоритмы', 'будут', 'главным', 'доводом', 'профессионального', 'разработчика']


def find_element(sorted_numbers, element):
    """Находит индекс element в отсортированном списке sorted_numbers."""
    left = 0
    right = len(sorted_numbers)
    while left < right:
        mid = (left + right) // 2
        if element == sorted_numbers[mid]:
            return mid
        if element > sorted_numbers[mid]:
            left = mid + 1
        else:
            right = mid


for item in wins:
    print(find_element(wins, item))

for item in strs:
    print(find_element(strs, item))
