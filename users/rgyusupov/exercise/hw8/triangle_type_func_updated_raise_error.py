def triangle_type(a, b, c):
    # Проверка на положительность сторон
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Все стороны треугольника должны быть положительными")

    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return "не треугольник"
    elif sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
        return "прямоугольный"
    elif sides[2] ** 2 < sides[0] ** 2 + sides[1] ** 2:
        return "остроугольный"
    else:
        return "тупоугольный"


# Тестовые случаи
positive_tests = [
    {"args": (3, 4, 5), "expected": "прямоугольный"},
    {"args": (5, 5, 6), "expected": "остроугольный"},
    {"args": (6, 4, 9), "expected": "тупоугольный"},
    {"args": (5, 5, 5), "expected": "остроугольный"},
    {"args": (5, 12, 13), "expected": "прямоугольный"},
]

negative_tests = [
    {"args": (1, 2, 3), "expected": "не треугольник"},
]

error_tests = [
    {"args": (-1, 2, 3), "expected": "Все стороны треугольника должны быть положительными", "error": ValueError},
    {"args": (0, 1, 2), "expected": "Все стороны треугольника должны быть положительными", "error": ValueError},
]


def run_tests(tests):
    results = []
    for test in tests:
        args = test["args"]
        expected = test["expected"]
        try:
            result = triangle_type(*args)
            results.append({"args": args, "expected": expected, "result": result,
                            "passed": result == expected and ("error" not in test)})
        except Exception as e:
            results.append({"args": args, "expected": expected, "result": str(e),
                            "passed": str(e) == expected and ("error" in test and test["error"] == type(e))})
    return results


positive_results = run_tests(positive_tests)
negative_results = run_tests(negative_tests)
error_results = run_tests(error_tests)
all_results = positive_results + negative_results + error_results

# Вывод результатов
for (idx, test_result) in enumerate(all_results):
    args = test_result["args"]
    print(
        f"{idx + 1}. Тест для аргументов {args}: Ожидаемый результат - '{test_result['expected']}', " +
        f"Полученный результат - '{test_result['result']}' - {'Прошел' if test_result['passed'] else 'Не прошел'}")

print(f"Пройдено {sum(test['passed'] for test in all_results)}/{len(all_results)}")
