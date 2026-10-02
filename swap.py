first_room = input("Первая аудитория: ")
second_room = input("Вторая аудитория: ")
print(f"\nДо обмена: Первая аудитория = {first_room}, Вторая аудитория = {second_room}")
temp = first_room
first_room = second_room
second_room = temp
print(f"После обмена: Первая аудитория = {first_room}, Вторая аудитория = {second_room}")