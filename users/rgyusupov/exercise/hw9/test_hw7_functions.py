from hw7_functions import print_matrix, ten_times, print_haiku


def test_print_matrix(capsys):
    matrix1 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print_matrix(matrix1)
    captured = capsys.readouterr()
    assert captured.out == "1 2 3\n4 5 6\n7 8 9\n", "Ошибка в выводе матрицы matrix1"

    matrix2 = [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
    print_matrix(matrix2)
    captured = capsys.readouterr()
    assert captured.out == "1 2 3\n4 5 6\n7 8 9\n10 11 12\n", "Ошибка в выводе матрицы matrix2"


def test_print_matrix_empty(capsys):
    empty_matrix = []
    print_matrix(empty_matrix)
    captured = capsys.readouterr()
    assert captured.out == "", "Ошибка: вывод для пустой матрицы должен быть пустым"


def test_print_matrix_one_element(capsys):
    one_element_matrix = [[42]]
    print_matrix(one_element_matrix)
    captured = capsys.readouterr()
    assert captured.out == "42\n", "Ошибка: вывод для матрицы с одним элементом некорректен"


def test_ten_times(capsys):
    ten_times()
    captured = capsys.readouterr()
    expected_output = ''.join(f"Вызов номер {i}\n" for i in range(1, 11))
    assert captured.out == expected_output, "Функция ten_times не выполнила 10 вызовов"


def test_print_haiku(capsys):
    a_haiku = ["Всё глазел на них", "Сакуры цветы, пока", "Шею не свело"]
    print_haiku(a_haiku)
    captured = capsys.readouterr()
    expected_output = "Всё глазел на них\nСакуры цветы, пока\nШею не свело\n"
    assert captured.out == expected_output, "Ошибка в выводе стиха"

    print_haiku(a_haiku, transform=str.upper)
    captured = capsys.readouterr()
    expected_uppercase = "ВСЁ ГЛАЗЕЛ НА НИХ\nСАКУРЫ ЦВЕТЫ, ПОКА\nШЕЮ НЕ СВЕЛО\n"
    assert captured.out == expected_uppercase, "Ошибка в выводе стиха заглавными буквами"


def test_print_haiku_third_char(capsys):
    a_haiku = ["Всё глазел на них", "Сакуры цветы, пока", "Шею не свело"]
    print_haiku(a_haiku, transform=lambda x: x[::3])
    captured = capsys.readouterr()
    expected_third_char_output = "В алаи\nСу е,о\nШ  е\n"
    assert captured.out == expected_third_char_output, "Ошибка в выводе каждого третьего символа стиха"


def test_print_haiku_red(capsys):
    a_haiku = ["Всё глазел на них", "Сакуры цветы, пока", "Шею не свело"]
    print_haiku(a_haiku, transform=lambda x: f"\033[91m{x}\033[0m")
    captured = capsys.readouterr()
    expected_red_output = "\033[91mВсё глазел на них\033[0m\n\033[91mСакуры цветы, пока\033[0m\n\033[91mШею не свело\033[0m\n"
    assert captured.out == expected_red_output, "Ошибка в выводе стиха красным цветом"
