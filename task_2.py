def get_most_populars():
    courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

    mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]


# Добавьте сюда ваш код из Задачи 1
    all_list = []
    for m in mentors:
        all_list += m
    all_name_list = []
    for name in all_list:
        all_name_list += name.split()
    name_list = all_name_list[::2]
    a = sorted(set(name_list))
    # Уникальные имена будут в unique_names
    unique_names = a

    # Подсчитайте встречаемость каждого имени через list.count()
    popular = []
    for name in unique_names:
        popular.append([name, name_list.count(name)])
    popular.sort(key=lambda x:x[1], reverse=True)
    top_3 = popular[:3]
    # print(top_3)
    final = ''
    for name_2, freq in top_3:
        abc = (f"{''.join(name_2)}: {''.join(str(freq))} раз(а), ")
        final += abc
    print(final[:-2])
    return final[:-2]

if __name__ == '__main__':
    get_most_populars()