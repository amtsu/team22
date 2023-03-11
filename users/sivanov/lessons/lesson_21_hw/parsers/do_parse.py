"""
Модуль, демонстрирующий работу с парсером
Вытащил из main`a модуля getdatafrom, чтобы было понятно где что поменялось при коммитах
"""
import os
from getdatafrom import CreateProductInfo
def main():
    """
    пример загрузки информации со см
    """
#---------------------------------------------------------------------------
    # создаем список парсеров
    pi_list = []
    pi_list.append(CreateProductInfo(os.getcwd()+'/json/smara1.json'))
    pi_list.append(CreateProductInfo(os.getcwd()+'/json/smara2.json'))
    pi_list.append(CreateProductInfo(os.getcwd()+'/json/uley1.json'))
    pi_list.append(CreateProductInfo(os.getcwd()+'/json/uley2.json'))
    #pi_list.append(CreateProductInfo(os.getcwd()+'/json/smstr1.json')) #403
    #pi_list.append(CreateProductInfo(os.getcwd()+'/json/smstr2.json')) #403
    pi_list.append(CreateProductInfo(os.getcwd()+'/json/220v1.json'))
    pi_list.append(CreateProductInfo(os.getcwd()+'/json/220v2.json'))
    #pi_list.append(CreateProductInfo(os.getcwd()+'/json/ctlnk1.json'))# не отдает цены
    #pi_list.append(CreateProductInfo(os.getcwd()+'/json/metrocc1.json'))# 403
    pi_list.append(CreateProductInfo(os.getcwd()+'/json/tkturin1.json'))
    pi_list.append(CreateProductInfo(os.getcwd()+'/json/tkturin2.json'))
    pi_list.append(CreateProductInfo(os.getcwd()+'/json/trsprt1.json'))
#---------------------------------------------------------------------------
    # парсим
    for product_info in pi_list:
        product_info.load()
        print(product_info.get())
#===============================================================================================
if __name__ == '__main__':
    main()
    