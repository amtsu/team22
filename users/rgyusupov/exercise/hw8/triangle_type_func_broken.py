def triangle_type_broken(a: float, b: float, c: float) -> str:
    return "остроугольный"

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
        result = triangle_type_broken(*args)
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
