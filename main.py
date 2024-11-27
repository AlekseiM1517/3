s = [(1, 2), (4, 7), (1, 0), (13, None)]

for i in range(10):
    try:
        x, y = s[i]
        print(x / y)
    except IndexError:
        print('Мы за границей списка')
    except ZeroDivisionError as e:
        print('Поделили на 0')
    except Exception as e:
        print('Непредвиденная ошибка %s' % e)
    finally:
        print('Идем дальше')