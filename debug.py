# Фрагмент А
# first = "2"
# second = "3"
# print(first+second)
# причина ошибки - строковый тип данных
# исправленная версия:
first = int("2")
second = int("3")
print(first+second)
# тип данных изменён на integer

# Фрагмент Б
# age = input("Возраст: ")
# (age + 1)
# причина ошибки - неправильный тип данных
# исправленная версия:
age = int(input("Возраст: "))
print(age + 1)
# тип данных изменён на integer

# Фрагмент В
#first = 4
#second = 7
#third = 10
#average = first+second+third /3
#print(average)
# Ошибка в неправильном прироритете операций
# Исправленная версия:
first = 4
second = 7
third = 10
average = (first + second + third)/3
print(average)
# Изменён приоритет операций (по математическим правилам)