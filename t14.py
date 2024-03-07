class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Course:
    def __init__(self, course_name, course_teacher):
        self.course_name = course_name
        self.course_teacher = course_teacher
        self.students = []

    def add(self, new_student):
        if len(self.students) < 5:
            self.students.append(new_student)
            print(f"{new_student.name} {self.course_name} kursiga qo'shildi.")
        else:
            print(f"{self.course_name} kursida bo'sh o'rin yo'q.")

    def delete(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"{student.name} {self.course_name} kursidan o'chirildi.")
        else:
            print(f"{student.name} {self.course_name} kursida topilmadi.")

    def info_course(self):
        print(f"{self.course_name} kursining o'qituvchisi {self.course_teacher}.\n\
{self.course_name} kursidagi talabalar:")
        for student in self.students:
            print(f"{student.name}, {student.age} yosh")

math_course = Course("Math", "John Doe")
science_course = Course("Science", "Jane Smith")

student1 = Student("Ali", 20)
student2 = Student("Vali", 22)
student3 = Student("Soli", 21)
student4 = Student("Nomi", 23)
student5 = Student("Dori", 24)

math_course.add(student1)
math_course.add(student2)
math_course.add(student3)
math_course.add(student4)
math_course.add(student5)

science_course.add(student1)
science_course.add(student2)
science_course.add(student3)
science_course.add(student4)
science_course.add(student5)

math_course.delete(student1)
science_course.delete(student2)

math_course.info_course()
science_course.info_course()
