# Student Result Generator (Method Overloading Concept)
class Result:
    def calculate(self, m1, m2, m3=None):
        if m3 is None:
            total = m1 + m2
            print("Total Marks:", total)
            print("Average:", total / 2)
        else:
            total = m1 + m2 + m3
            print("Total Marks:", total)
            print("Average:", total / 3)

r = Result()

r.calculate(80, 90)
r.calculate(80, 90, 70)
