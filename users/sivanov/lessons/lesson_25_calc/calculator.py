<<<<<<< HEAD
<<<<<<< HEAD
"""
файл с описанием класса калькулятор для вычисления простых бинарных операторов
https://stackoverflow.com/questions/15197673/using-pythons-eval-vs-ast-literal-eval
    тут есть готовый более универсального вычислителя, блин,
    обидно, искал инфу как работает нашел готовое решение посередине поисков
=======
"""
файл с описанием класса калькулятор для вычисления простых бинарных операторов
>>>>>>> прогнал через линтер
"""
import ast
import operator


<<<<<<< HEAD
=======
import ast, operator
>>>>>>> первая ревизия калькулятора, до тестов
=======
>>>>>>> прогнал через линтер
class Calculator:
    """
    Класс калькулятор, инициализируется строкой с простым выражением типа
    const operator const, где const - любое числовое выражение,
<<<<<<< HEAD
    а operator это одна из операций : сложение, вычитание,
    деление или умножение
    """

=======
    а operator это одна из операций : сложение, вычитание, деление или умножение
    https://stackoverflow.com/questions/15197673/using-pythons-eval-vs-ast-literal-eval
    тут есть готовый более универсального вычислителя, блин,
    обидно, искал инфу как работает нашел готовое решение посередине поисков
    """
<<<<<<< HEAD
>>>>>>> первая ревизия калькулятора, до тестов
=======

>>>>>>> прогнал через линтер
    def __init__(self):
        """
        инициализация
        создаем списки необходимых операций
        """
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> прогнал через линтер
        self.__bin_ops = {  # операции с двумя параметрами
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
        }
<<<<<<< HEAD
        self.__un_ops = {  # операции с одним параметром
            ast.USub: operator.neg,
            ast.UAdd: operator.pos,
        }
=======
        self.__bin_ops = { # операции с двумя параметрами
            ast.Add  : operator.add,
            ast.Sub  : operator.sub,
            ast.Mult : operator.mul,
            ast.Div  : operator.truediv,
            }
        self.un_ops = { # операции с одним параметром
            ast.USub : operator.neg,
            ast.UAdd : operator.pos,
            }
>>>>>>> первая ревизия калькулятора, до тестов
=======
        self.un_ops = {  # операции с одним параметром
            ast.USub: operator.neg,
            ast.UAdd: operator.pos,
        }
>>>>>>> прогнал через линтер

    def __call__(self, operation):
        """
        функция, делающая проверку корректности строки на входе и ее выполнение
        """
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> прогнал через линтер
        value = ast.parse(operation, mode="eval")
        assert isinstance(value.body, (ast.BinOp))  # ожидаем бинарный операнд
        assert isinstance(
            value.body.left, (ast.Constant, ast.UnaryOp)
        )  # проверяем левый аргумент
        assert isinstance(
            value.body.right, (ast.Constant, ast.UnaryOp)
        )  # проверяем правый аргумент
        assert isinstance(
            value.body.op, tuple(self.__bin_ops)
        )  # проверяем корректность операнда
        if isinstance(value.body.left, ast.UnaryOp):
            assert isinstance(
                value.body.left.operand, ast.Constant
            )  # корректность левого аргумента
<<<<<<< HEAD
            left = self.__un_ops[type(value.body.left.op)](
                value.body.left.operand.value
            )
        else:
            left = value.body.left.value
        if isinstance(value.body.right, ast.UnaryOp):
            assert isinstance(
                value.body.right.operand, ast.Constant
            )  # корректность правого аргумента
            right = self.__un_ops[type(value.body.right.op)](
                value.body.right.operand.value
            )
        else:
            right = value.body.right.value
        return self.__bin_ops[type(value.body.op)](
            left, right
        )  # пытаемся вычислить результат

    def __repr__(self):
        return "Класс калькулятор, вычисляет значения бинарных операций"


if __name__ == "__main__":
    do_calc = Calculator()
    print(f"результат выполнения (1-4) = {do_calc('1-4')}")
=======
        value = ast.parse(operation, mode = 'eval')
        assert isinstance(value.body,(ast.BinOp)) # ожидаем бинарный операнд
        assert isinstance(value.body.left,(ast.Constant, ast.UnaryOp)) #проверяем левый аргумент
        assert isinstance(value.body.right,(ast.Constant, ast.UnaryOp)) #проверяем правый аргумент
        assert isinstance(value.body.op, tuple(self.__bin_ops)) # проверяем корректность операнда
        if (isinstance(value.body.left,ast.UnaryOp)):
            assert(isinstance(value.body.left.operand, ast.Constant)) # проверяем корректность левого аргумента
            self.__left = self.un_ops[type(value.body.left.op)](value.body.left.operand.value)
=======
            left = self.un_ops[type(value.body.left.op)](value.body.left.operand.value)
>>>>>>> прогнал через линтер
        else:
            left = value.body.left.value
        if isinstance(value.body.right, ast.UnaryOp):
            assert isinstance(
                value.body.right.operand, ast.Constant
            )  # корректность правого аргумента
            right = self.un_ops[type(value.body.right.op)](
                value.body.right.operand.value
            )
        else:
            right = value.body.right.value
        return self.__bin_ops[type(value.body.op)](
            left, right
        )  # пытаемся вычислить результат

    def __repr__(self):
        return "Класс калькулятор, инициализируется строкой с простым выражением"


if __name__ == "__main__":
<<<<<<< HEAD
   do_calc = Calculator()
   print(f"результат выполнения (1-4) = {do_calc('1-4')}")
>>>>>>> первая ревизия калькулятора, до тестов
=======
    do_calc = Calculator()
    print(f"результат выполнения (1-4) = {do_calc('1-4')}")
>>>>>>> прогнал через линтер
