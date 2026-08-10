# Проект FitLife - MVP версия 1.0


def greeting():
    """Программа вежливо здоровается спрашивает имя и возраст"""
    name = get_name("Здравствуйте, как Вас зовут?\n")
    age = get_age("Сколько Вам лет?\n")
    return name, age


def get_name(prompt):
    while True:
        name = input(prompt).strip()
        if not name:
            print("Имя не может быть пустым. Пожалуйста, введите корректное имя.")
            continue
        return name


def get_age(prompt):
    while True:
        try:
            age = int(input(prompt))
            if age <= 0:
                print(
                    "Возраст должен быть положительным числом. Пожалуйста, попробуйте снова."
                )
                continue
            return age
        except ValueError:
            print("Пожалуйста, введите корректный возраст (целое число).")


def parameters():
    """Программа спрашивает вес и рост"""
    weight = get_weight("Напишите Ваш вес в кг (например, 72)\n")
    height = get_height("Напишите Ваш рост в метрах (например, 1.75)\n")
    return weight, height


def get_weight(prompt):
    while True:
        try:
            weight = int(input(prompt))
            if weight <= 0:
                print(
                    "Вес должен быть положительным числом. Пожалуйста, попробуйте снова."
                )
                continue
            return weight
        except ValueError:
            print("Пожалуйста, введите корректный вес (целое число).")


def get_height(prompt):
    while True:
        try:
            height = float(input(prompt))
            if height <= 0:
                print(
                    "Рост должен быть положительным числом. Пожалуйста, попробуйте снова."
                )
                continue
            return height
        except ValueError:
            print("Пожалуйста, введите корректный рост (например, 1.75).")


def calculate_bmi(user_weight, user_height):
    """Программа вычисляет Индекс массы тела (ИМТ)"""
    # Индекс массы тела, Округлить
    bmi = round(user_weight / (user_height**2), 1)
    return bmi


def calculate_water_needed(user_weight):
    """Прорамма вычисляет норму воды в литрах"""
    # Рассчитать норму воды в миллилитрах:
    ML_OF_WATER_PER_KG = 30
    water_ml = user_weight * ML_OF_WATER_PER_KG
    # Перевести в литры (делим на 1000мл), округлить:
    water_l = round(water_ml / 1000, 1)
    return water_l


def FitLife_MVP():
    name, age = greeting()
    weight, height = parameters()
    print(f"\n\n\nОтчет для пользователя: {name} ({age} г.)")
    print(f"Твой Индекс Массы Тела: {calculate_bmi(weight, height)}")
    print(f"Рекомендуемая норма воды: {calculate_water_needed(weight)} л. в день")
    print("\nРасчет окончен. Будьте здоровы!\n")


FitLife_MVP()
