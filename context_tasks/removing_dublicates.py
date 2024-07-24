def main(target_list):
    result_list = []
    cuts = []
    result_list.append(target_list[0])
    for value in target_list[1:]:
        if value not in result_list:
            result_list.append(value)
        elif value in result_list:
            cuts.append('_')
    result_list += cuts
    return result_list


if __name__ == '__main__':
    with open('input.txt') as f_input:
        list_len = int(f_input.readline())
        target_list = list(f_input.readline().rstrip().split())
    result = main(target_list)

    with open('output.txt', 'w') as f_output:
        f_output.write(str(' '.join(result)))
