import csv


def load_csv():
    """
    Загружает данные из CSV-файла 'Corp_Summary.csv'
    и возвращает их в виде списка словарей.
    """
    corp_summary = []
    with open('Corp_Summary.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            corp_summary.append(row)
    return corp_summary


def menu_func() -> None:
    """
    Выводит меню и обрабатывает выбор пользователя.
    """
    print("Меню")
    print("1. Вывести в понятном виде иерархию команд")
    print("2. Вывести сводный отчёт по департаментам")
    print("3. Сохранить сводный отчёт из предыдущего пункта в виде csv-файла")

    item = int(input(
        "Выберите необходимый пункт меню, введя цифру от 1 до 3: "
    ))
    if item == 1:
        point_1()
    elif item == 2:
        point_2()
    elif item == 3:
        point_3()
    else:
        print("Введите корректное число")


def point_1() -> None:
    """
    Выводит иерархию команд внутри департаментов.
    """
    data = load_csv()
    hierarchy: dict = {}
    i: dict
    for i in data:
        department = i['Департамент']
        unit = i['Отдел']
        if department not in hierarchy:
            hierarchy[department] = set()
        hierarchy[department].add(unit)
    print()
    print("Иерархия команд:")
    for deps, teams in hierarchy.items():
        print(f"Департамент: {deps}")
        for team in teams:
            print(f"  Команда: {team}")


def point_2() -> str:
    """
    Генерирует сводный отчет по департаментам и возвращает его в виде строки.

    Возвращает:
        str: Строка, содержащая сводный отчет.
    """
    data = load_csv()
    pivot = {}
    i: dict
    for i in data:
        department = i['Департамент']
        if department not in pivot:
            pivot[department] = {
                'count': 0,
                'min_salary': float('inf'),
                'max_salary': float('-inf'),
                'total_salary': 0,
            }
        pivot[department]['count'] += 1
        cash = int(i['Оклад'])
        pivot[department]['min_salary'] =\
            min(pivot[department]['min_salary'], cash)
        pivot[department]['max_salary'] =\
            max(pivot[department]['max_salary'], cash)
        pivot[department]['total_salary'] += cash
    result = ""
    result += "\nСводный отчет\n"
    for department, summary in pivot.items():
        average_salary = round((summary['total_salary'] / summary['count']))
        result += f" Департамент: {department}\n"
        result += f"  Количество сотрудников: {summary['count']}\n"
        result += (f"  Вилка зарплат: от {summary['min_salary']}"
                   f" до {summary['max_salary']}\n")
        result += f"  Средняя зарплата: {average_salary}\n"
    print(result)
    return result


def point_3() -> None:
    """
    Сохраняет сводный отчет в виде CSV-файла 'pivot_table.csv'.
    """
    pivot_table = point_2()
    with open('pivot_table.csv', 'w', newline='') as f:
        f.write(pivot_table)


if __name__ == '__main__':
    menu_func()
