FirstName = str(input("Имя: "))
SecondName = str(input("Фамилия: "))
Group = str(input("Группа: "))
City = str(input("Город: "))
Age = int(input("Возраст (в полных годах, 1-120): "))
Subject = str(input("Введите название предмета: "))
Hours = float(input("Введите количество часов подготовки в неделю: "))
fullname = f"{FirstName}{SecondName}"
Hours4 = Hours * 4
Age4 = Age + 4
daily = Hours /7
print("         Карточка студента")
print("Полное имя:",FirstName,SecondName)
print("")
print("Город:",City)
print("Группа:",Group)
print("Возраст:",Age)
print("Возраст через 4 года",Age4)
print("Любимый предмет:",Subject)
print(f"Часов подготовки в неделю: {Hours:.2f}" )
print(f"Часов за 4 недели:{Hours4:.2f}" )
print(f"Среднее в день: {daily:.2f}" )