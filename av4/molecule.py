from searching_framework.utils import Problem
from searching_framework.informed_search import astar_search

# List of obstacles
obstacles = [(0, 1), (1, 1), (1, 3), (2, 5), (3, 1), (3, 6), (4, 2),
             (5, 6), (6, 1), (6, 2), (6, 3), (7, 3), (7, 6), (8, 5)]


# Function for moving atom up
def move_atom_up(atom1, atom2, atom3):
    """Moving an atom up

    :param atom1: atom that needs to be moved up
    :type atom1: tuple(int, int)
    :param atom2: second atom that is static
    :type atom2: tuple(int, int)
    :param atom3: third atom that is static
    :type atom3: tuple(int, int)
    :return: the new position of the moving atom
    :rtype: tuple(int, int)
    """
    while 7 > atom1[1] and atom1 not in obstacles and atom1 not in [atom2, atom3]:
        y = atom1[1]
        y = y + 1
        atom1 = atom1[0], y
    pos_new = atom1[0], atom1[1] - 1
    return pos_new


def move_atom_down(atom1, atom2, atom3):
    """Moving an atom down

    :param atom1: atom that needs to be moved down
    :type atom1: tuple(int, int)
    :param atom2: second atom that is static
    :type atom2: tuple(int, int)
    :param atom3: third atom that is static
    :type atom3: tuple(int, int)
    :return: the new position of the moving atom
    :rtype: tuple(int, int)
    """
    while atom1[1] > -1 and atom1 not in obstacles and atom1 not in [atom2, atom3]:
        y = atom1[1]
        y = y - 1
        atom1 = atom1[0], y
    pos_new = atom1[0], atom1[1] + 1
    return pos_new


def move_atom_right(atom1, atom2, atom3):
    """Moving an atom right

    :param atom1: atom that needs to be moved right
    :type atom1: tuple(int, int)
    :param atom2: second atom that is static
    :type atom2: tuple(int, int)
    :param atom3: third atom that is static
    :type atom3: tuple(int, int)
    :return: the new position of the moving atom
    :rtype: tuple(int, int)
    """
    while 9 > atom1[0] and atom1 not in obstacles and atom1 not in [atom2, atom3]:
        x = atom1[0]
        x = x + 1
        atom1 = x, atom1[1]
    pos_new = atom1[0] - 1, atom1[1]
    return pos_new


def move_atom_left(atom1, atom2, atom3):
    """Moving an atom left

    :param atom1: atom that needs to be moved left
    :type atom1: tuple(int, int)
    :param atom2: second atom that is static
    :type atom2: tuple(int, int)
    :param atom3: third atom that is static
    :type atom3: tuple(int, int)
    :return: the new position of the moving atom
    :rtype: tuple(int, int)
    """
    while atom1[0] > -1 and atom1 not in obstacles and atom1 not in [atom2, atom3]:
        x = atom1[0]
        x = x - 1
        atom1 = x, atom1[1]
    pos_new = atom1[0] + 1, atom1[1]
    return pos_new


class Molecule(Problem):
    def __init__(self, initial):
        super().__init__(initial, None)

    def goal_test(self, state):
        h1_x = state[0]
        h1_y = state[1]
        o_x = state[2]
        o_y = state[3]
        h2_x = state[4]
        h2_y = state[5]
        return h1_y == o_y and o_y == h2_y and \
               h1_x == o_x - 1 and o_x == h2_x - 1

    def successor(self, state):
        successors = dict()
        h1 = state[0], state[1]
        o = state[2], state[3]
        h2 = state[4], state[5]

        # Up H1
        h1_new = move_atom_up(h1, o, h2)
        state_new = h1_new + o + h2
        if state_new != state:
            successors['UpH1'] = state_new
        # Down H1
        h1_new = move_atom_down(h1, o, h2)
        state_new = h1_new + o + h2
        if state_new != state:
            successors['DownH1'] = state_new
        # Left H1
        h1_new = move_atom_left(h1, o, h2)
        state_new = h1_new + o + h2
        if state_new != state:
            successors['LeftH1'] = state_new
        # Right H1
        h1_new = move_atom_right(h1, o, h2)
        state_new = h1_new + o + h2
        if state_new != state:
            successors['RightH1'] = state_new

        # Up O
        o_new = move_atom_up(o, h1, h2)
        state_new = h1 + o_new + h2
        if state_new != state:
            successors['UpO'] = state_new
        # Down O
        o_new = move_atom_down(o, h1, h2)
        state_new = h1 + o_new + h2
        if state_new != state:
            successors['DownO'] = state_new
        # Left O
        o_new = move_atom_left(o, h1, h2)
        state_new = h1 + o_new + h2
        if state_new != state:
            successors['LeftO'] = state_new
        # Right O
        o_new = move_atom_right(o, h1, h2)
        state_new = h1 + o_new + h2
        if state_new != state:
            successors['RightO'] = state_new

        # Up H2
        h2_new = move_atom_up(h2, o, h1)
        state_new = h1 + o + h2_new
        if state_new != state:
            successors['UpH2'] = state_new
        # Down H2
        h2_new = move_atom_down(h2, o, h1)
        state_new = h1 + o + h2_new
        if state_new != state:
            successors['DownH2'] = state_new
        # Left H2
        h2_new = move_atom_left(h2, o, h1)
        state_new = h1 + o + h2_new
        if state_new != state:
            successors['LeftH2'] = state_new
        # Right H2
        h2_new = move_atom_right(h2, o, h1)
        state_new = h1 + o + h2_new
        if state_new != state:
            successors['RightH2'] = state_new

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]

    def h(self, node):
        # Хевристичка функција која за секоја состојба пресметува минимален
        # број на турнувања на паровите од атоми за тие да се спојат
        state = node.state
        h1 = state[0], state[1]
        o = state[2], state[3]
        h2 = state[4], state[5]
        value = 0

        # проверка за позициите на H1 и O и потребниот број на чекори за да се спојат
        if h1[0] != o[0]:
            if h1[1] != (o[1] - 1):
                # ако атомот на водорот не е во иста редица и во колона веднаш до атомот
                # на кислород ни требаат најмалку 2 турнувања (turn down/up + left/right)
                # за да се спојат
                value += 2
            else:
                # ако атомот на водорот не е во иста редица, но е во колона веднаш до атомот
                # на кислород ни треба најмалку 1 турнувањe (turn up or down) за да се спојат
                value += 1
        else:  # h1[0] == o[0]
            if h1[1] > o[1]:
                # ако атомот на водорот е во иста редица, но во колона од десна страна на
                # атомот на кислород ни требаат најмалку 3 турнувања (turn 2 x down/up + left/right)
                # за да се спојат
                value += 3
            elif h1[1] < (o[1] - 1):
                # ако атомот на водорот е во иста редица, но во колона од лева страна на
                # атомот на кислород ни треба најмалку 1 турнување (turn right) за да се спојат
                value += 1

        # проверка за позициите на H2 и O и потребниот број на чекори за да се спојат
        if h2[0] != o[0]:
            if h2[1] != (o[1] + 1):
                # ако атомот на водорот не е во иста редица и во колона веднаш до атомот
                # на кислород ни требаат најмалку 2 турнувања (turn down/up + left/right)
                # за да се спојат
                value += 2
            else:
                # ако атомот на водорот не е во иста редица, но е во колона веднаш до атомот
                # на кислород ни треба најмалку 1 турнувањe (turn up or down) за да се спојат
                value += 1
        else:  # h2[0] == o[0]
            if h2[1] < o[1]:  # ако атомот на водорот е во иста редица, но во колона од лева страна на
                # атомот на кислород ни требаат најмалку 3 турнувања (turn 2 x down/up + left/right)
                # за да се спојат
                value += 3
            elif h2[1] > (o[1] + 1):
                # ако атомот на водорот е во иста редица, но во колона од десна страна на
                # атомот на кислород ни треба најмалку 1 турнување (turn left) за да се спојат
                value += 1

        if h1[0] == h2[0] and h1[0] != o[0]:
            # ако водородните атоми се во ист ред тогаш можеме да имаме само едно турнување на
            # атомот на кислород up/down (а претходно сме пресметале турнување на H1 и турнување на H2)
            value -= 1

        return value


if __name__ == '__main__':
    h1_atom_column = int(input())
    h1_atom_row = int(input())
    o_atom_column = int(input())
    o_atom_row = int(input())
    h2_atom_column = int(input())
    h2_atom_row = int(input())

    molecule = Molecule((h1_atom_column, h1_atom_row, o_atom_column,
                         o_atom_row, h2_atom_column, h2_atom_row))

    answer = astar_search(molecule)
    print(answer.solution())
