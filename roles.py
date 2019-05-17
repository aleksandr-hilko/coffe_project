class Common:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class Manager(Common):
    def __init__(self, name, position="manager"):
        super().__init__(name, position)


class Salesman(Common):
    def __init__(self, name, position="salesman"):
        super().__init__(name, position)
