'''
클래스에 학생의 이름을 입력하면
해당 학생이 얻은 3과목의 평균점수에 따라 A~F까지 출력하세요
'''
class Grade:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def addMarks(self, mark):
        self.marks.append(mark)

    def avg(self):
        return sum(self.marks) / len(self.marks)


    @staticmethod
    def main():
        student = Grade(input("학생이름 입력 : "))
        for subject in ['국어', '영어', '수학'] :
            student.addMarks(int(input(subject + '점수 입력 : ')))
        avg = student.avg()
        print(f'{student.name}의 과목 평균은 {int(avg)}이다.')

if __name__ == '__main__':
    Grade.main()