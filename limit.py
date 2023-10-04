class Limit:
    def __init__(self, min_score, limit3, limit4, limit5):
        self.min_score = min_score
        self.limit3 = limit3
        self.limit4 = limit4
        self.limit5 = limit5

    def __str__(self):
        return f'{self.min_score} {self.limit3} {self.limit4} {self.limit5}'
    
    def get_min_score(self):
        return self.min_score
    
    def get_limit3(self):
        return self.limit3
    
    def get_limit4(self):
        return self.limit4
    
    def get_limit5(self):
        return self.limit5