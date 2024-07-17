def list_superset(list_set_1, list_set_2):
    result = []
    for value_1 in list_set_1:
        if value_1 in list_set_2:
            result.append(True)
        else:
            result.append(False)

    if len(list_set_1) == len(list_set_2) and False not in result:
        return 'Наборы равны.'
    elif len(list_set_1) != len(list_set_2) and False not in result:
        return f'Набор {list_set_2} - супермножество.'

    result = []
    for value_2 in list_set_2:
        if value_2 in list_set_1:
            result.append(True)
        else:
            result.append(False)

    if len(list_set_2) == len(list_set_1) and False not in result:
        return 'Наборы равны.'
    elif len(list_set_2) != len(list_set_1) and False not in result:
        return f'Набор {list_set_1} - супермножество.'

    return 'Супермножество не обнаружено.'

# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))
