class StudentPerformance:
    def __init__(self, scores):
        self.scores = scores

    def score_difference(self):
        try:
            return self.scores[-1] - self.scores[0]
        except IndexError:
            print("No scores available to calculate difference")
            return None
        
s1 = StudentPerformance([])
diff1 = s1.score_difference()
diff1 is not None and print("Difference between last and first score is: ", diff1)