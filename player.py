"""Player data."""
class Player:
    def __init__(self, name="Customer"):
        self.name = name
        self.total_score = 0
        self.rounds_played = 0

    def record_score(self, score):
        self.total_score += score
        self.rounds_played += 1
