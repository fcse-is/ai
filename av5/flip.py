from searching_framework.utils import Problem
from searching_framework.uninformed_search import breadth_first_graph_search


class Flip(Problem):
    def __init__(self, n, initial, goal=None):
        super().__init__(initial, goal)
        self.n = n

    def successor(self, state):
        successor = dict()

        for i in range(self.n):
            for j in range(self.n):
                list_state = [list(s) for s in state]
                list_state[i][j] = 0 if list_state[i][j] == 1 else 1
                if i > 0:
                    list_state[i - 1][j] = 0 if list_state[i - 1][j] == 1 else 1
                if i < self.n - 1:
                    list_state[i + 1][j] = 0 if list_state[i + 1][j] == 1 else 1
                if j > 0:
                    list_state[i][j - 1] = 0 if list_state[i][j - 1] == 1 else 1
                if j < self.n - 1:
                    list_state[i][j + 1] = 0 if list_state[i][j + 1] == 1 else 1
                successor[f'x: {i}, y: {j}'] = tuple([tuple(s) for s in list_state])

        return successor

    def goal_test(self, state):
        return sum([item for row in state for item in row]) == self.n * self.n

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    '''
    3
    0, 0, 0, 1, 0, 0, 1, 1, 0
    '''
    n = int(input())
    fields = list(map(int, input().split(',')))
    initial_state = [tuple(fields[i: i + n]) for i in range(0, len(fields), n)]

    flip = Flip(n, tuple(initial_state))

    result = breadth_first_graph_search(flip)
    print(result.solution())
