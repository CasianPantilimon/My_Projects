# exercitiul 1
def my_function1(param):
    if param <= 15:
        my_dict = {}
        for i in range(1, param + 1):
            my_dict[i] = sum(range(1, i + 1))
        return my_dict
    else:
        return "\nIntrodu un numar care sa fie egal sau mai mic cu 15!"

print(my_function1(15))


# exercitiul 2
tuple_exemple = (-1, 3, -2, 4, 0)


def my_function2(param):
    counter = 0
    for numar_pozitiv in param:
        if numar_pozitiv > 0:
            counter += 1
    return counter


print(my_function2(tuple_exemple))

# exercitiul 3
list_example = [5, 2, 9, 1, 5, 6]


def my_function3(param):
    alegere = int(input("Alege un prag de selectie/slicing point: "))
    lista_numere_mai_mici = []
    lista_numere_mai_mari_sau_egale = []
    for i in param:
        if i < alegere:
            lista_numere_mai_mici.append(i)
        else:
            lista_numere_mai_mari_sau_egale.append(i)
        tuplu_final = (lista_numere_mai_mici, lista_numere_mai_mari_sau_egale)
    return tuplu_final


print(my_function3(list_example))
