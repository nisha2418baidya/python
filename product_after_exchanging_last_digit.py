


def swap_last_digits_and_multiply(num1, num2):
    last_digit1 = num1 % 10
    last_digit2 = num2 % 10
    
    num1_without_last_digit = num1 // 10
    num2_without_last_digit = num2 // 10
    
    new_num1 = num1_without_last_digit * 10 + last_digit2
    new_num2 = num2_without_last_digit * 10 + last_digit1
    
    result = new_num1 * new_num2
    return result


    print(result)



