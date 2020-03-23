from searching_framework.utils import Problem
from searching_framework.informed_search import astar_search


def update_obstacle_position(position):
    x, y, direction = position
    if (y == 0 and direction == -1) or (y == 5 and direction == 1):
        direction = direction * (-1)
    y_new = y + direction
    position_new = x, y_new, direction
    return position_new


def check_collision(man, obstacle1, obstacle2):
    return man != obstacle1[:2] and man != obstacle2[:2]


class Explorer(Problem):

    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def goal_test(self, state):
        g = self.goal
        return state[0] == g[0] and state[1] == g[1]

    def successor(self, state):
        successors = dict()
        x = state[0]
        y = state[1]
        obstacle_1 = (state[2], state[3], state[4])
        obstacle_2 = (state[5], state[6], state[7])

        obstacle_1_new = update_obstacle_position(obstacle_1)
        obstacle_2_new = update_obstacle_position(obstacle_2)

        # Right
        if x < 7:
            x_new = x + 1
            y_new = y
            man = x_new, y_new
            if check_collision(man, obstacle_1_new, obstacle_2_new):
                state_new = (x_new, y_new, obstacle_1_new[0], obstacle_1_new[1], obstacle_1_new[2],
                             obstacle_2_new[0], obstacle_2_new[1], obstacle_2_new[2])

                successors['Right'] = state_new

        # Left
        if x > 0:
            x_new = x - 1
            y_new = y
            man = x_new, y_new
            if check_collision(man, obstacle_1_new, obstacle_2_new):
                state_new = (x_new, y_new, obstacle_1_new[0], obstacle_1_new[1], obstacle_1_new[2],
                             obstacle_2_new[0], obstacle_2_new[1], obstacle_2_new[2])

                successors['Left'] = state_new

        # Up
        if y < 5:
            x_new = x
            y_new = y + 1
            man = x_new, y_new
            if check_collision(man, obstacle_1_new, obstacle_2_new):
                state_new = (x_new, y_new, obstacle_1_new[0], obstacle_1_new[1], obstacle_1_new[2],
                             obstacle_2_new[0], obstacle_2_new[1], obstacle_2_new[2])

                successors['Up'] = state_new

        # Down
        if y > 0:
            x_new = x
            y_new = y - 1
            man = x_new, y_new
            if check_collision(man, obstacle_1_new, obstacle_2_new):
                state_new = (x_new, y_new, obstacle_1_new[0], obstacle_1_new[1], obstacle_1_new[2],
                             obstacle_2_new[0], obstacle_2_new[1], obstacle_2_new[2])

                successors['Down'] = state_new

        return successors

    def h(self, node):
        x = node.state[0]
        y = node.state[1]
        x1 = self.goal[0]
        y1 = self.goal[1]
        return abs(x - x1) + abs(y - y1)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]


if __name__ == '__main__':
    man_x = int(input())
    man_y = int(input())
    house_x = int(input())
    house_y = int(input())

    house = [house_x, house_y]
    explorer = Explorer((man_x, man_y, 2, 5, -1, 5, 0, 1), house)

    answer = astar_search(explorer)
    print(answer.solution())
