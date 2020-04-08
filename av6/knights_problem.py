from constraint import *


def knights_attacking(k1, k2):
    if abs(k1[0] - k2[0]) == abs(k1[1] - k2[1]):
        return False
    return True


if __name__ == '__main__':

    problem = Problem()

    n = int(input())

    variables = range(0, n)

    domains = []
    for i in range(0, n):
        for j in range(0, n):
            domains.append((i, j))

    domains = [(row, col) for row in range(0, n) for col in range(0, n)]

    problem.addVariable(variables[0], [(0, 0)])
    problem.addVariable(variables[1], [(0, 1)])
    problem.addVariables(variables[2:], domains)

    for knight1 in variables:
        for knight2 in variables:
            if knight1 < knight2:
                problem.addConstraint(knights_attacking, (knight1, knight2))

    solution = problem.getSolutions()

    print(len(solution))
