n = int(input("Enter a number: \n"))

last_digit = n %10
second_last_digit = (n // 10) % 10
remaining_number = n //100
result = remaining_number*100 + last_digit* 10 +second_last_digit
print("exchanging the last two digit:" ,result)