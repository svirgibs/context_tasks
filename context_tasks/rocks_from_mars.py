class Rocks:
    def __init__(self, weight: int, free: bool = True):
        self.weight = weight
        self.free = free

    def __repr__(self):
        return repr(self.weight)


def get_quantity_orders(
        min_weight_list: list[int],
        rocks_list: list[int]
):
    count = 0

    min_weight_list = sorted(min_weight_list, reverse=True)

    rocks_list = sorted(rocks_list, reverse=True)
    rocks_list = [Rocks(x) for x in rocks_list]

    for min_weight in min_weight_list:
        for rock in rocks_list:
            if min_weight <= rock.weight and rock.free:
                count += 1
                rock.free = False
                break
    return count


if __name__ == '__main__':
    with open('input.txt') as file_input:
        orders_quantity = int(file_input.readline().rstrip())
        min_weight_list = file_input.readline().rstrip().rsplit()
        rocks_quantity = int(file_input.readline().rstrip())
        rocks_list = file_input.readline().rstrip().rsplit()

    min_weight_list = [int(x) for x in min_weight_list]
    rocks_list = [int(x) for x in rocks_list]

    result = get_quantity_orders(
        min_weight_list=min_weight_list,
        rocks_list=rocks_list
    )

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
