class Weapon():
    def __init__(self, wep_name, wep_range, complexity, speed, mobility, utility):
        self.wep_name = wep_name
        self.wep_range = wep_range
        self.complexity = complexity
        self.speed = speed
        self.mobility = mobility
        self.utility = utility
        self.array = [self.wep_range, self.complexity, self.speed, self.mobility, self.utility]