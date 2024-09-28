# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
user_input = input("Введіть чотирьохзначне ціле додатне число: ")  # Запит на ввід числа
#print(type(user_input))  # <class 'str'>
# print(user_input / 2)  # TypeError
number = int(user_input)
print("Вивід цифр числа по рядках:")  # Число
print(number // 1000)  #1 цифра
print(number % 1000 // 100)  # 2 цифра
print(number % 100 // 10)  # 3 цифра
print(number % 10)  # 4 цифра
#https://github.com/Melnyk70/Lesson2_2.git
