def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'На улице идет дождь?'
    )
    a = input('Введите да или нет: ')
    if a == 'да':
        print(
            'Зонтик точно нужен!'
        )
    elif a == 'нет':
        print(
            'Зонтик лучше оставить дома'
        )
    else:
        print(
            'Введите только да или нет'
        )


def step2_no_umbrella():
    print(
        'Отлично, зонтик не нужен, вот мы и в баре. '
        'Хух, отлично посидели. Давайте попросим счет'
    )
    dish_name = input(
        'Введите название блюда: '
    )
    dish_count = int(input(
        'Введите количество порций. Укажите только число:  '
    ))
    dish_price = int(input(
        'Введите стоимость одной порции в рублях. Укажите только число: '
    ))
    total = int(input(
        'Введите номинал купюры в рублях, чтобы посчитать сдачу. Укажите только число: '
    ))
    print()
    print('Чек')
    print(f'{dish_name} - {dish_count} шт - {dish_price} руб/шт')
    print(f'Итого: {dish_count * dish_price} руб')
    print(f'Внесено: {dish_price} руб')
    print(f'Сдача: {total - dish_count * dish_price} руб')


if __name__ == '__main__':
    step1()
