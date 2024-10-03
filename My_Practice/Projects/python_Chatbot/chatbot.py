lista = [1, 2, 3, 4, 5, 6]


def reverse(param_list):
    for _ in param_list:
        return param_list[::-1]


lista_reversed = reverse(lista)
print(lista)
print(lista_reversed)