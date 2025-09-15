def insertion_sort(array):
    if array[0] > array[1]:
        array[0], array[1] = array[1], array[0]
    for i in range(2, len(array)):
        valor_indice_vago = array[i]
        indice_vago = i
        for j in range(i-1, -1, -1):
            troca = False
            if array[j] > valor_indice_vago:
                array[indice_vago], indice_vago = array[j], indice_vago - 1
                troca = True
            if troca:
                array[j] = valor_indice_vago
    return array

def test_insertion_sort():
    tests = [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Lista já ordenada
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Lista em ordem decrescente
        ([4, 2, 4, 3, 2], [2, 2, 3, 4, 4]),  # Lista com elementos repetidos
        ([-3, -1, -2, -5, -4], [-5, -4, -3, -2, -1]),  # Lista com números negativos
        ([-1, 3, -2, 2, 0], [-2, -1, 0, 2, 3]),       # Lista com números mistos
        ([1000, 500, 100, 50, 10], [10, 50, 100, 500, 1000]),  # Lista com números grandes
        ([1.1, 2.2, 0.5, 3.3, 1.0], [0.5, 1.0, 1.1, 2.2, 3.3]),  # Lista com números flutuantes
        ([7, 7, 7, 7, 7], [7, 7, 7, 7, 7])  # Lista com valores iguais
    ]

    for i, (input_array, expected) in enumerate(tests):
        result = insertion_sort(input_array)
        if result == expected:
            print(f"Teste {i + 1}: Passou")
        else:
            print(f"Teste {i + 1}: Falhou - Esperado {expected}, mas obteve {result}")

test_insertion_sort()
# [8,7,4]
# [7,8,XXXX] apos primeiro IFF
# valor_indice_vago = 4
# indice_vago = 2
# if 8 > 4
# indice_vago = 1
# [7,8,8]
# if 7 > 4
# indice_vago = 0, array[1] = 7
# [7,7,8]





