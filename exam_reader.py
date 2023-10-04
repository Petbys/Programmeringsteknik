# 2015-03-19 KLASSEN ÄR GIVEN
import exam

class Exam_reader:
    def __init__(self):
        self.ind = 0
        self.names = ['Olle', 'Anna', 'Emma', 'Harald', 'Torsten']
        # These should be strings
        self.partA = [['7', '3', '4', '2', '5', '10'], ['2', '2', '3', '5', '7', '9'], ['4', '3', '1', '2', '4', '3'], ['1', '2', '1', '1', '1', '5'], ['7', '7', '7', '5', '4', '2']]
        self.partB = [['0', '1', '2', '3'], ['7', '3', '2', '1'], ['4', '1', '2', '1'], ['0', '1', '1', '0'], ['7', '7', '7', '7']]

    def next(self):
        if self.ind >= len(self.names):
            return None
        ex = exam.Exam(self.names[self.ind])
        for v in self.partA[self.ind]:
            ex.add_partA(v)
        for v in self.partB[self.ind]:
            ex.add_partB(v)
        self.ind += 1
        return ex

if __name__ == '__main__':
    er = Exam_reader()
    exa = er.next()
    while exa != None:
        print(exa)
        exa = er.next()

# Sample print-out when executed:
#
# Olle
# ['7', '3', '4', '2', '5', '10']['0', '1', '2', '3']
# Anna
# ['2', '2', '3', '5', '7', '9']['7', '3', '2', '1']
# Emma
# ['4', '3', '1', '2', '4', '3']['4', '1', '2', '1']
# Harald
# ['1', '2', '1', '1', '1', '5']['0', '1', '1', '0']
# Torsten
# ['7', '7', '7', '5', '4', '2']['7', '7', '7', '7']