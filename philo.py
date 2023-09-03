class Philo():
    def __init__(self):
        self.taken = [0, []]
        self.think = [0, []]
        self.eat = [0, []]
        self.sleep = [0, []]
        self.die = [0, []]

    def add_taken(self, message):
        self.taken[0] += 1
        self.taken[1].append(message)
    
    def add_think(self, message):
        self.think[0] += 1
        self.think[1].append(message)
    
    def add_eat(self, message):
        self.eat[0] += 1
        self.eat[1].append(message)
    
    def add_sleep(self, message):
        self.sleep[0] += 1
        self.sleep[1].append(message)

    def add_die(self, message):
        self.die[0] += 1
        self.die[1].append(message)
