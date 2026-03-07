class StudentMarks:
    def __init__(self, marks):
        self.marks = marks

    def last_three_avg(self):
        try:
            # Access last three using negative indexing
            last_three = [self.marks[-1], self.marks[-2], self.marks[-3]]
            return sum(last_three) / 3
        except IndexError:
            print("Not enough marks to calculate average")

s1 = StudentMarks([50, 60, 70, 80])
print(s1.last_three_avg())
