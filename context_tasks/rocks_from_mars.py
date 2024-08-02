def get_quantity_orders(
        orders_quantity: int,
        orders: list[int],
        rocks_quantity: int,
        offers: list[int]
):
    count = 0
    offers.sort()
    orders.sort()
    i = 0
    j = 0

    while i < orders_quantity and j < rocks_quantity:
        if offers[j] >= orders[i]:
            count += 1
            i += 1
        j += 1
    return count


if __name__ == '__main__':
    with open('input.txt') as file_input:
        orders_quantity = int(file_input.readline().rstrip())
        orders = file_input.readline().rstrip().rsplit()
        rocks_quantity = int(file_input.readline().rstrip())
        offers = file_input.readline().rstrip().rsplit()

    orders = [int(x) for x in orders]
    offers = [int(x) for x in offers]

    result = get_quantity_orders(
        orders_quantity=orders_quantity,
        orders=orders,
        rocks_quantity=rocks_quantity,
        offers=offers
    )

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
