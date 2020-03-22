def multiply_element(element, i, n):
    if i < n / 2:
        return element * 2
    else:
        return element * 3


if __name__ == '__main__':
    n = int(input())
    m = int(input())

    elements_matrix = []
    for i in range(0, n):
        elements_row = [int(element) for element in input().split(
            " ")]  # citame elementite kako string, go delime stringot po prazno mesto i sekoj element od listata go konvertirame vo int
        elements_matrix.append(elements_row)

    result_matrix = [[multiply_element(elements_matrix[i][j], i, n) for j in range(0, m)] for i in
                       range(0, n)]

    print(result_matrix)
