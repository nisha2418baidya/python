number = int(input("Enter a number: "))
last_digit = number % 10
second_last_digit = number // 10 % 10
print("Sum of last two digits:", second_last_digit+last_digit)