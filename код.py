name = input("Оюутны нэр: ")
age = input("Нас: ")
score = input("Авсан дүн (0-100): ")

print("\n--- Оюутны Мэдээлэл ---")
print("Нэр:", name)
print("Төгсөхөд үлдсэн нас:", 22 - int(age))


if int(score) >= 60:
    print("Шалгалтын үр дүн: ТЭНЦСЭН 🥳")
else:
    print("Шалгалтын үр дүн: УНАСАН 😢")