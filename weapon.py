class Weapon():
    def __init__(self, wep_name, wep_range, complexity, speed, mobility, utility):
        self.wep_name = wep_name
        self.wep_range = wep_range
        self.complexity = complexity
        self.speed = speed
        self.mobility = mobility
        self.utility = utility
        self.match_count = 0
        self.array = [self.wep_range, self.complexity, self.speed, self.mobility, self.utility]

    def display(self):
        print(f"""
        Weapon: {self.wep_name}
        Range: {self.wep_range} Range
        Complexity: {self.complexity}
        Speed: {self.speed}
        Mobility: {self.mobility}
        Utility: {self.utility}

        """)