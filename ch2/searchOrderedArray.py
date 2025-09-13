def linear_search(array, target):
        for index, value in enumerate(array):
            if value == target:
                return index
        return None

def binary_search(array, target):
    intervalo_inicial = 0
    intervalo_final = len(array) - 1
    while intervalo_inicial <= intervalo_final:
        index_meio = (intervalo_final + intervalo_inicial) // 2
        valor_meio = array[index_meio]
        if target == valor_meio:
            return index_meio
        elif target < valor_meio:
            intervalo_final = index_meio - 1
        elif target > valor_meio:
            intervalo_inicial = index_meio + 1

    return None




print(linear_search([1,2,3,4,5], 1))
print(linear_search([1,2,3,4,5], 5))
print(linear_search([3,17,75,80,202],22))
print(binary_search([1,2,3,4,5], 1))
print(binary_search([1,2,3,4,5], 5))
print(binary_search([3,17,75,80,202],22))



