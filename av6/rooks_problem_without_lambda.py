from constraint import *


def rooks_attacking_constraint(rook1, rook2):
    if rook1[0] != rook2[0] and rook1[1] != rook2[1]:
        return True
    return False


if __name__ == '__main__':
    problem = Problem(RecursiveBacktrackingSolver())

    domain = [(i, j) for i in range(0, 8) for j in range(0, 8)]

    rooks = range(1, 9)

    problem.addVariables(rooks, domain)

    for rook1 in rooks:
        for rook2 in rooks:
            if rook1 < rook2:
                problem.addConstraint(rooks_attacking_constraint, (rook1, rook2))

    solution = problem.getSolution()
    print(solution)
