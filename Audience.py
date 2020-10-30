class Audience:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = int(capacity)

    def __repr__(self):
        return f'{self.number}'
