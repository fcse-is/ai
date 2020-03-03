class Agent:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Position: ({self.x}, {self.y})'

    def move(self):
        pass

class LeftAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x -= 1

class RightAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x += 1

class UpAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y += 1


class DownAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y -= 1


if __name__ == '__main__':
    la = LeftAgent(3, 4)
    print(la)
    for i in range(5):
        la.move()
        print(f'Step: {i}, {la}')

    ra = RightAgent(-2, 3)
    print(ra)
    for i in range(5):
        ra.move()
        print(f'Step: {i}, {ra}')

    ua = UpAgent(-2, -3)
    print(ua)
    for i in range(5):
        ua.move()
        print(f'Step: {i}, {ua}')

    da = DownAgent(2, 3)
    print(da)
    for i in range(5):
        da.move()
        print(f'Step: {i}, {da}')
