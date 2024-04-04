def triangle_type(a: float, b: float, c: float) -> str:
    """
    Функция, определяющая тип треугольника по длинам его сторон
    """
    result = "не треугольник"
    triangle_exist = (a < (b + c)) and (b < (a + c)) and (c < (a + b))
    if triangle_exist:
        sides = [a, b, c]
        sides.sort()
        acute_triangle = (sides[0] ** 2 + sides[1] ** 2) > sides[2] ** 2
        obtuse_triangle = (sides[0] ** 2 + sides[1] ** 2) < sides[2] ** 2
        right_triangle = abs((sides[0] ** 2 + sides[1] ** 2) - sides[2] ** 2) <= 0.01

        if acute_triangle:
            result = "остроугольный"
        elif obtuse_triangle:
            result = "тупоугольный"
        elif right_triangle:
            result = "прямоугольный"
    return result


# Тестовые случаи
positive_tests = [
    {"args": (3, 4, 5), "expected": "прямоугольный"},
    {"args": (5, 5, 6), "expected": "остроугольный"},
    {"args": (6, 4, 9), "expected": "тупоугольный"},
    {"args": (5, 5, 5), "expected": "остроугольный"},
    {"args": (5, 12, 13), "expected": "прямоугольный"},
]

negative_tests = [
    {"args": (-1, 2, 3), "expected": "не треугольник"},
    {"args": (0, 1, 2), "expected": "не треугольник"},
    {"args": (1, 2, 3), "expected": "не треугольник"},
]


def run_tests(tests):
    results = []
    for test in tests:
        args = test["args"]
        expected = test["expected"]
        result = triangle_type(*args)
        results.append({"args": args, "expected": expected, "result": result, "passed": result == expected})
    return results


positive_results = run_tests(positive_tests)
negative_results = run_tests(negative_tests)
all_results = positive_results + negative_results

# Вывод результатов
for (idx, test_result) in enumerate(all_results):
    args = test_result["args"]
    print(
        f"{idx+1}. Тест для аргументов {args}: Ожидаемый результат - '{test_result['expected']}', " +
        f"Полученный результат - '{test_result['result']}' - {'Прошел' if test_result['passed'] else 'Не прошел'}")

print(f"Пройдено {sum(test['passed'] for test in all_results)}/{len(all_results)}")
