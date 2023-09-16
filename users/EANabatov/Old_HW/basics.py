def perebor():
    result = []
    for i in range(1, 16):
        if i % 3 == 0:
            result.append(i)
            i += 1
        else:
            i += 1
    return result


def test_base_work():
    assert perebor() == [3, 6, 9, 12, 15]
        