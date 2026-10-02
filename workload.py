subject1 = input("Название первого предмета: ")
lessons1 = int(input("Количество занятий по первому предмету в неделю: "))
duration1 = int(input("Продолжительность одного занятия по первому предмету в минутах: "))
subject2 = input("Название второго предмета: ")
lessons2 = int(input("Количество занятий по второму предмету в неделю: "))
duration2 = int(input("Продолжительность одного занятия по второму предмету в минутах: "))
aviablehours = float(input("Доступное время на неделю (часов): "))
time1 = lessons1 * duration1
time2 = lessons2 * duration2
totalminutes = time1 + time2
totalhours = totalminutes / 60
aviableminutes = aviablehours * 60
freeminutes = aviablehours -totalminutes
freehours = freeminutes / 60
fourweeksminutes = totalminutes * 4
print("       Учебная нагрузка")
print(f"{subject1}: {time1} мин/нед")
print(f"{subject2}: {time2} мин/нед")
print(f"Общая нагрузка:   {totalminutes} мин = {totalhours:.2f} ч")
print(f"Свободное время:    {freehours:.2f} ч")
print(f"Нагрузка за 4 недели: {fourweeksminutes} мин = {fourweeksminutes / 60:2f} ч ")
