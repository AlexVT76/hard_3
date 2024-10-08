summa_all = 0
def calculate_structure_sum(*data_structure):

    for element in data_structure:
        global summa_all
        if isinstance(element, int):
            summa_all += element
        elif isinstance(element, str):
            summa_all += len(element)
        elif isinstance(element, list):
            calculate_structure_sum(*element)
        elif isinstance(element, tuple):
            calculate_structure_sum(*element)
        elif isinstance(element, set):
            calculate_structure_sum(*element)
        elif isinstance(element, dict):
            for i in element:
                key = (i, element[i])
                calculate_structure_sum(*key)
    return(summa_all)

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
