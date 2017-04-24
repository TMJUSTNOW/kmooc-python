# -*- coding: utf-8 -*-
import math

def get_factorial_value(integer_value):
    return math.factorial(integer_value)

def is_positive_number(integer_str_value):
    # '''
    # Input:
    #   - integer_str_value : 숫자형태의 문자열 값
    # Output:
    #   - integer_str_value가 양수일 경우에는 True,
    #     integer로 변환이 안되거나, 0, 음수일 경우에는 flase
    # Examples:
    #   >>> import factorial_calculator as fc
    #   >>> fc.is_positive_number("100")
    #   True
    #   >>> fc.is_positive_number("0")
    #   False
    #   >>> fc.is_positive_number("-10")
    #   False
    #   >>> fc.is_positive_number("abc")
    #   False
    # '''
    try:
        # ===Modify codes below=============
        if integer_str_value.isdigit() == False:
            return False

        num = int(integer_str_value)
        if num == 0:
            return False
        elif num > 0:
            return True
        # ==================================
    except ValueError:
        return False


def main():
    user_input = 999
    # ===Modify codes below=============
    while True:
        user_input = input('Input a positive number : ')
        user_input_is_integer = is_positive_number(user_input)
        if user_input_is_integer == True:
            print(get_factorial_value(int(user_input)))
        elif user_input_is_integer == False and user_input is not '0':
            print('Input again, Please')
        elif user_input is '0':
            print('Thank you for using this program')
            break
    # ==================================

if __name__ == "__main__":
    main()
