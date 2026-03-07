class StudentScores:
    def __init__(self, scores):
        self.scores = scores

    def highest_last_two(self):
        try:
            last_two = [self.scores[-1], self.scores[-2]]
            return max(last_two)
        except IndexError:
            print("Not enough scores to find highest value")

s1 = StudentScores([50, 50, 60])
print("Highest score among last two is: ", + s1.highest_last_two())