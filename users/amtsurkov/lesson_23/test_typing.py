# def calculate_sum(price: int, count: int) -> int:
# def calculate_sum(price, count) -> int:
def calculate_sum(price, count) -> str:
    """
    This method calculte sum for product
    """
    return price * count


final_price = calculate_sum(1000, 3)

# final_price_2  = calculate_sum(80, 4)
final_price_2 = calculate_sum("Moloko", 4)


def test_2(long_string: str):
    """
    Test
    """
    print(long_string)

def test_2():
    """
    Test
    """
    print('dddd')



test_2(calculate_sum("Moloko", 2))

test_2(final_price)

test_2(final_price_2)

print(final_price)

print(final_price_2)
