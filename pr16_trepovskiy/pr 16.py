pages_num = int(input('Введіть кількість сторінок: '))


def check_input(m, n):
    if m % n != 0:
        print(f'Неправильна кількість сторінок для {n}-сторінкового зошита.')
        new_m = int(input('Введіть кількість сторінок: '))
        check_input(new_m, n)
    elif m > 1280:
        print('Кількість сторінок не може бути більше ніж 1280.')
        new_m = int(input('Введіть кількість сторінок: '))
        check_input(new_m, n)


def tuples_creator(active):
    def create_tuple(func):
        def creator(**kwargs):
            if active:
                list_from_func = func(pages_num)
                tuples_from_func = []
                tuples_from_one_notebook = []
                for i in list_from_func:
                    for k in range(int(len(i)/4)):
                        tuples_from_one_notebook.append(tuple(i[k:k+4]))
                tuples_from_func.append(tuples_from_one_notebook)
                print(tuples_from_func)
                return tuples_from_func
            else:
                print(func(pages_num, **kwargs))
                return func
        return creator()
    return create_tuple


@tuples_creator(active=False)
def pages(num_pages, pages_in_notebook=16):

    check_input(num_pages, pages_in_notebook)

    list_of_notebooks = []
    one_notebook_list = []

    for i in range(1, int(num_pages/pages_in_notebook + 1)):
        for j, k in zip(range(pages_in_notebook, 0, -1), range(1, pages_in_notebook)):
            while j not in one_notebook_list and k not in one_notebook_list:
                if j % 2 != 0:
                    one_notebook_list.append(k)
                    one_notebook_list.append(j)
                if j % 2 == 0:
                    one_notebook_list.append(j)
                    one_notebook_list.append(k)
        list_of_notebooks.append([l*i for l in one_notebook_list])

    return list_of_notebooks

