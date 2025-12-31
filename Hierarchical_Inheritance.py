class Student:
    def student_info(self, name, roll):
        self.name = name
        self.roll = roll
        print("Name:", self.name)
        print("Roll No:", self.roll)

class Exam(Student):
    def exam_details(self, marks):
        self.marks = marks
        print("Marks:", self.marks)

class Sports(Student):
    def sports_details(self, game):
        self.game = game
        print("Sports:", self.game)
        
exam_student = Exam()
exam_student.student_info("Amit", 101)
exam_student.exam_details(85)
print()
sports_student = Sports()
sports_student.student_info("Riya", 102)
sports_student.sports_details("Cricket")
