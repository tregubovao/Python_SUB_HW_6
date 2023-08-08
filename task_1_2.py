# Часть 1
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY 
# и возвращает истину, если дата может существовать или ложь, если такая дата невозможна. 
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# И весь период действует григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.

# Часть 2
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import sys
import os
os.system('cls')

def date_valid_func(date: str) -> bool:
    MIN_LIMIT_YEAR = 1
    MAX_LIMIT_YEAR = 9999
    JANUARY, FEBRUARY = 1, 2
    MARCH, APRIL, MAY = 3, 4, 5
    JUNE, JULY, AUGUST = 6, 7, 8
    SEPTEMBER, OCTOBER, NOVEMBER = 9, 10, 11
    DECEMBER = 12
    DAYS_IN_FEB_LEAP_YEAR = 29
    DAYS_IN_FEB_REGULAR_YEAR = 28
    DAYS_IN_LONG_MONTH = 31
    DAYS_IN_SHORT_MONTH = 30
    FIRST_DAY_OF_ANY_MONTH = 1

    date_list = date.split('.')
    if len(date_list) == 3:
        if (len(date_list[0]) == len(date_list[1]) == 2 
            and len(date_list[2]) == 4):
            day, month, year = (int(date_list[0]), 
                                int(date_list[1]), 
                                int(date_list[2]))
            if MIN_LIMIT_YEAR <= year <= MAX_LIMIT_YEAR:        
                if (month == JANUARY or month == MARCH or month == MAY 
                    or month == JULY or month == AUGUST
                    or month == OCTOBER or month == DECEMBER):
                    if FIRST_DAY_OF_ANY_MONTH <= day <= DAYS_IN_LONG_MONTH:
                        return True
                    return False
                elif (month == APRIL or month == JUNE 
                        or month == SEPTEMBER or month == NOVEMBER):
                    if FIRST_DAY_OF_ANY_MONTH <= day <= DAYS_IN_SHORT_MONTH:
                        return True
                    return False
                elif (month == FEBRUARY):
                    if _leap_year(year) == True:
                        if FIRST_DAY_OF_ANY_MONTH <= day <= DAYS_IN_FEB_LEAP_YEAR:
                            return True
                        return False
                    else:
                        if FIRST_DAY_OF_ANY_MONTH <= day <= DAYS_IN_FEB_REGULAR_YEAR:
                            return True
                        return False
                return False
            return False
        print('Неверный формат. Перезапустите программу и повторите ввод.')
        return False
    print('Неверный формат. Перезапустите программу и повторите ввод.')
    return False
    
def _leap_year(year: int) -> bool:  # проверка года на високосность
    if (year % 4 == 0              
        and year % 100 != 0 
        or year % 400 == 0):
        return True
    return False
    
if __name__ == '__main__':
    # date = input('Введите дату в формате DD.MM.YYYY: ')    # запуск через IDE  
    # print(date_valid_func(date))

    date_from_console = sys.argv[1]
    print(date_valid_func(date_from_console))              # запуск через командную строку   
    
        