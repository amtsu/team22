#!/usr/local/bin/python
# coding: utf-8
"""
в этом файле пример создания собственного перечислимого типа в питоне
так как встроенного механизма нет, перечислимые типы создаются как наследники класса
Enum из модуля enum
"""
import enum


class MyOwnCoolHttpStatus(enum.Enum):
    """
    создаю свои собственные крутые именованные статусы
    вот этот класс и определяет аналог перечислимого типа
    для работы с именованными константами этого достаточно
    для математических операций нужно определить пару методов,
    про это чуть позже доделаю.
    """

    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    PROXY_AUTHENTICATION_REQUIRED = 407
    REQUEST_TIMEOUT = 408
    CONFLICT = 409
    GONE = 410
    # все мне надоело, хватит


# ==============================================================================
def fake_http_responce(code: int) -> int:
    """
    выдает заданный ей код http запроса
    """
    return code


# ==============================================================================
def react_on_given_http_error_code(code: int) -> None:
    """
    функция. получает на вход ошибку http в виде числа и как-то на нее реагирует
    """
    found = False
    for item in MyOwnCoolHttpStatus:
        if item.value == code:
            print(f"данный код: {item.name}")
            found = True
    if not found:
        print("неизвестный код")


# ===============================================================================
def send_error_code_to_client(code: MyOwnCoolHttpStatus) -> None:
    """
    макет функции, отправляющей клиенту код ошибки
    конечно она никому ничего не отправляет,
    просто печатает его на экран
    """
    print(f"Посылаю {code} со значением {code.value} клиенту...")


# ==============================================================================
def main():
    """
    пример работы с перечислимым типом
    """
    print("Пример работы с перечислимым типом")
    resp = fake_http_responce(401)
    #  я хотел мэтч, но его завезли только в 3.10
    #    match resp:
    #        case MyOwnCoolHTTPStatus.bad_request :
    #            print("случился bad request")
    #        case MyOwnCoolHTTPStatu.unautorized :
    #            print("случился unautorized ")
    if resp == MyOwnCoolHttpStatus.BAD_REQUEST.value:
        print("случился bad request")
    if resp == MyOwnCoolHttpStatus.UNAUTHORIZED.value:
        print("случился unautorized")
    # ----------------------------------
    react_on_given_http_error_code(400)
    react_on_given_http_error_code(401)
    react_on_given_http_error_code(404)
    react_on_given_http_error_code(410)
    react_on_given_http_error_code(10)
    # ---------------------------------
    # send_error_code_to_client(400) # плохо читается, что за 400? 400 чего?
    send_error_code_to_client(MyOwnCoolHttpStatus.BAD_REQUEST)  # значительно лучше
    # send_error_code_to_client(407) # точно 407? что это значит, забыл ...
    send_error_code_to_client(
        MyOwnCoolHttpStatus.PROXY_AUTHENTICATION_REQUIRED  # без доков понятно что это
    )


# ===============================================================================
if __name__ == "__main__":
    main()
