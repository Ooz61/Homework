my_dict = {
    "Имя": "Стас",
    "Год рождения": 1995,
    "Профессия": "Программист",
    "Хобби": "Фантастика"
}

print(my_dict)
name = my_dict["Имя"]
print("Имя:", name)
print(my_dict.get("Возраст", "Не найдено"))

my_dict["Город рождения"] = "Москва"
my_dict["Наличие автомобиля"] = "Есть"

del my_dict["Профессия"]
print(my_dict)


my_set = {
 "Яблоко", 4, 1, 5,
 "Яблоко", 1, 4, 5,

}
print(my_set)

my_set.update(["Ананас"],
              ["5310"])

print(my_set)