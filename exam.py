
class Exam:
    def __init__(self, name):
        self.score_partA = []
        self.score_partB = []
        self.student = name
        
    def __str__(self):
        return self.student+'\n'+str(self.score_partA)+str(self.score_partB)
    
    def get_student(self):
        return self.student
    
    def get_partA(self):
        return str(self.score_partA)
    
    def get_partB(self):
        return str(self.score_partB)
    
    def set_name(self, name):
        self.student = name
        
    def add_partA(self, score):
        self.score_partA.append(score)
        
    def add_partB(self, score):
        self.score_partB.append(score)
        
    def sum_partB(self):
        t = 0
        for s in self.score_partB:
            t += int(s)           
        return t
    
    
    def passed(self, min_score, limit3):
        score = [int(i) for i in self.score_partA]
        if sum(score) >= limit3:
            for i in score:
                if i >= min_score:
                    continue
                else:
                    return False
            return True
        else:
            return False
        
    def get_grade(self, min_score, limit3, limit4, limit5):
        if not self.passed(1, 21):
            return 0
        if sum([int(i) for i in self.score_partB]) >= limit5:
            return 5
        elif sum([int(i) for i in self.score_partB]) >= limit4:
            return 4
        else:
            return 3
        
if __name__ == '__main__':
    exam = Exam("Anon")
    exam.set_name("Eva Huss")
    exam.add_partA(7)
    exam.add_partA(8)
    exam.add_partA(1)
    exam.add_partA(2)
    exam.add_partA(3)
    exam.add_partA(5)
    exam.add_partB(7)
    exam.add_partB(8)
    print(exam)
    print('Student: ', exam.get_student())
    print('Result part A: ', exam.get_partA())
    print('Result part B: ', exam.get_partB())
    if exam.passed(1, 21):
        print(exam.get_student()+" has passed.")
    else:
        print(exam.get_student()+" has failed.")

    if exam.get_grade(2, 20, 7, 15) == 5:
        print("Passed, Grade 5")
    elif exam.get_grade(1,8, 12, 15) == 4:
        print("Passed, Grade 4")
    else:
        print("Passed, Grade 3")

# Sample print-out when executed:
#
# Eva Huss
# [7, 8, 1, 2, 3, 5][7, 5]
# Student:  Eva Huss
# Result part A:  [7, 8, 1, 2, 3, 5]
# Result part B:  [7, 5]
# Eva Huss has passed.
# Passed, Grade 4