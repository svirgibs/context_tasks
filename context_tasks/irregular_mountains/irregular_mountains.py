def valid_mountain_array(height_array):
    height_increase = True

    if len(height_array) < 3:
        return False

    if height_array[-1] > height_array[-2] or height_array[0] > height_array[-1]:
        return False

    for index, value in enumerate(height_array):
        if index == 0:
            continue
        if value > height_array[index - 1] and height_increase:
            continue
        elif value == height_array[index - 1]:
            return False
        elif value > height_array[index - 1] and height_increase is False:
            return False
        else:
            if value < height_array[index - 1]:
                height_increase = False
                continue
    return True


if __name__ == '__main__':
    with open('input.txt') as file_input:
        massive = file_input.readline().rstrip().rsplit(' ')

    values = [int(value) for value in massive]
    result = valid_mountain_array(values)

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
