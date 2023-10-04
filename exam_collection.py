import exam_reader

class Exam_collection:
    def __init__(self):
        self.the_collection =[]
        er = exam_reader.Exam_reader()
        exa = er.next()
        while exa != None:
            self.the_collection.append(exa
)
            exa = er.next()
            
        
        
    def print_grade_list(self, min_grade, limit3, limit4, limit5):
        print('Grade-list: ')
        print(f'Limits: 3: 4: 5: \n', '       ',limit3, limit4, limit5)
        print("Minimum score per prolem on part A for passing grade: " + str(min_grade))
        print("Name\tGrade\t Score A\t\t Score B")
        for exa in self.the_collection:
            print(exa.get_student(),end='')
            print(str('\t'+str(exa.get_grade(min_grade, limit3, limit4, limit5))),end='')
            print('\t',(exa.get_partA()),'\t',(exa.get_partB()))
            
    def print_statistics(self, min_grade, limit3, limit4, limit5):
        grade = []
        for exa in self.the_collection:
            grade.append(exa.get_grade(min_grade, limit3, limit4, limit5))
        print('U: 3: 4: 5:')
        print(f'{grade.count(0)}  {grade.count(3)}  {grade.count(4)}  {grade.count(5)}')
            

if __name__ == '__main__':
    ex_collection = Exam_collection()
    ex_collection.print_grade_list(2, 20, 7, 15)
    ex_collection.print_statistics(2, 20, 7, 15)         

# Sample print-out when executed:
#
# Grade-list: 
# Limits : 3: 4: 5: 
#          20 7 15
# Minimum score per prolem on part A for passing grade: 2
# Name    Grade    Score A                 Score B
# Olle    3        ['7', '3', '4', '2', '5', '10']         ['0', '1', '2', '3']
# Anna    4        ['2', '2', '3', '5', '7', '9']          ['7', '3', '2', '1']
# Emma    0        ['4', '3', '1', '2', '4', '3']          ['4', '1', '2', '1']
# Harald  0        ['1', '2', '1', '1', '1', '5']          ['0', '1', '1', '0']
# Torsten 5        ['7', '7', '7', '5', '4', '2']          ['7', '7', '7', '7']

# Statistics
# U: 3: 4: 5:
# 2  1  1  1