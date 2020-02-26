operators = ['+', '-', '/', '//', '*', '**', '%']


def calculator(x, y, operator):
    if operator not in operators:
        return "Greshka"

    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "/":
        return x / y
    elif operator == "//":
        return x // y
    elif operator == "*":
        return x * y
    elif operator == "**":
        return x ** y
    elif operator == "%":
        return x % y


if __name__ == "__main__":
    x = float(input())
    operator = input()
    y = float(input())
    rez = calculator(x, y, operator)
    print("rezultat:", rez)
    # print(f"rezultat: {rez}")
    # print("rezultat: {} {}".format(rez, rez))
    # print("rezultat: %.2f %.2f" % (rez, rez))
