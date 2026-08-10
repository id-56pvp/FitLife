# Проект FitLife - MVP версия 1.0


def get_name(prompt):
    """Проверяет что имя - не пустое"""
    while True:
        name = input(prompt).strip()
        if not name:
            print("Имя не может быть пустым. "
                  "Исправьте ошибку :)")
            continue
        return name


def get_age(prompt):
    """Проверяет что возраст - целое положительное число"""
    while True:
        try:
            age = int(input(prompt))
            if age <= 0:
                print("Возраст должен быть положительным числом. "
                      "Исправьте ошибку :)")
                continue
            return age
        except ValueError:
            print("Пожалуйста, введите корректный возраст (целое число)")


def get_weight(prompt):
    """Проверяет что вес - целое положительное число c точкой или без"""
    while True:
        try:
            weight = float(input(prompt))
            if weight <= 0:
                print("Вес должен быть положительным числом. "
                      "Исправьте ошибку :)")
                continue
            return weight
        except ValueError:
            print("Пожалуйста, введите корректный вес (например, 72.5)")


def get_height(prompt):
    """Проверяет что рост - положительное число с точкой или без"""
    while True:
        try:
            height = float(input(prompt))
            if height <= 0:
                print("Рост должен быть положительным числом. "
                      "Исправьте ошибку :)")
                continue
            return height
        except ValueError:
            print("Пожалуйста, введите корректный рост (например, 1.75)")


def calculate_bmi(user_weight, user_height):
    """Программа вычисляет Индекс массы тела (ИМТ)"""
    return user_weight / (user_height**2)


def calculate_water_needed(user_weight):
    """Программа вычисляет норму воды в литрах"""
    L_OF_WATER_PER_KG = 30 / 1000  # 0.03 л воды на кг веса в день
    return user_weight * L_OF_WATER_PER_KG


def fit_life():
    """Программа"""
    # Собираем данные пользователя
    name = get_name("Здравствуйте, как Вас зовут?\n")
    age = get_age("Сколько Вам лет?\n")
    weight = get_weight("Напишите Ваш вес в кг (например, 72)\n")
    height = get_height("Напишите Ваш рост в метрах (например, 1.75)\n")

    # Рассчитываем показатели пользователя
    bmi = calculate_bmi(weight, height)
    water_needed = calculate_water_needed(weight)

    # Выводим отчет пользователю
    print(f"\n{'=' * 40}")  # Pretty Print для читаемости
    print(f"Отчет для пользователя: {name} ({age} г.)")
    print(f"Твой Индекс Массы Тела: {bmi:.1f}")
    print(f"Рекомендуемая норма воды: {water_needed:.1f} л. в день")
    print(f"{'=' * 40}")    # Pretty Print для читаемости
    print("Расчет окончен. Будьте здоровы! @FitLife\n")


fit_life()
