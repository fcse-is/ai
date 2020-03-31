from searching_framework import Problem, breadth_first_graph_search


class Hanoi(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = {}
        tower = list(state)
        num_tower = len(tower)

        for i in range(num_tower):
            if len(tower[i]) == 0:
                continue
            top_block = tower[i][-1]
            for j in range(num_tower):
                if i == j:
                    continue
                tower_size2 = len(tower[j])
                if tower_size2 > 0:
                    tower_top = tower[j][-1]
                else:
                    tower_top = -1
                if top_block <= tower_top or tower_size2 == 0:
                    new_state = list(state)
                    new_state[j] = new_state[j] + new_state[i][-1:]
                    new_state[i] = new_state[i][:-1]
                    new_state = tuple(new_state)
                    successors[f'MOVE TOP BLOCK FROM PILLAR {i + 1} TO PILLAR {j + 1}'] = new_state
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == "__main__":
    s = input()
    initial_towers = tuple([tuple(map(int, x.split(','))) if x != '' else () for x in s.split(';')])
    s = input()
    goal_towers = tuple([tuple(map(int, x.split(','))) if x != '' else () for x in s.split(';')])
    """
    3,2,1;;
    ;;3,2,1
    """
    hanoi = Hanoi(initial_towers, goal_towers)
    result = breadth_first_graph_search(hanoi)
    p = result.solution()
    print(f'Number of action {len(p)}')
    print(p)
