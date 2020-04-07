from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    domain = []
    for i in range(0, 8):
        domain.append(i)

    rooks = range(0, 8)

    problem.addVariables(rooks, domain)

    for rook1 in rooks:
        for rook2 in rooks:
            if rook1 < rook2:
                problem.addConstraint(lambda r1, r2: r1 != r2, (rook1, rook2))

    solution = problem.getSolution()
    print(solution)