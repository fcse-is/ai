from constraint import *

if __name__ == '__main__':
    problem = Problem()

    variables = range(0, 16)
    domain = range(1, 17)
    problem.addVariables(variables, domain)
    problem.addConstraint(AllDifferentConstraint(), variables)

    for row in range(4):
        problem.addConstraint(ExactSumConstraint(34), [row * 4 + i for i in range(4)])

    for col in range(4):
        problem.addConstraint(ExactSumConstraint(34), [col + 4 * i for i in range(4)])

    problem.addConstraint(ExactSumConstraint(34), range(0, 16, 5))
    problem.addConstraint(ExactSumConstraint(34), range(3, 13, 3))

    solution = problem.getSolution()

    print(solution)
