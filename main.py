# Мельник Ігор - ДЗ 2.2. Необхідно "перевернути" 5-ти значне число
user_input = input("Введіть пʼятизначне ціле додатне число: ")  # Запит на ввід числа
number = int(user_input)
print("Число антипод таке:", end=' ')  # Число антипод
print(number % 10, end='')  # 5 цифра
print(number % 100 // 10, end='')  # 4 цифра
print(number % 1000 // 100, end='')  # 3 цифра
print(number % 10000 // 1000, end='')  # 2 цифра
print(number // 10000)  #1 цифра