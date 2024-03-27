class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Teacher(Person):
    def __init__(self, name, age, gender, subjects_taught):
        super().__init__(name, age, gender)
        self.subjects_taught = subjects_taught

    def teach(self):
        print(f"{self.name} is teaching {', '.join(self.subjects_taught)}")


class Student(Person):
    def __init__(self, name, age, gender, course, group):
        super().__init__(name, age, gender)
        self.course = course
        self.group = group

    def study(self):
        print(f"{self.name} is studying in {self.group} of {self.course} course")


class Subject:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Academy:
    def __init__(self):
        self.teachers = []
        self.students = []
        self.subjects = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)



academy = Academy()

biology_teacher = Teacher("Danilo Petrovich", 35, "Male", ["Biology"])
geography_teacher = Teacher("Olena Dzuba", 40, "Female", ["Geography"])

student1 = Student("Alisa Owl", 20, "Female", "Environmental Science", "2347")
student2 = Student("Ivan Boyko", 22, "Male", "Environmental Science", "7890")

biology_subject = Subject("Biology", "Study of living organisms")
geography_subject = Subject("Geography", "Study of Earth's landscapes, environments, and the relationships between people and their environments")

academy.add_teacher(biology_teacher)
academy.add_teacher(geography_teacher)
academy.add_student(student1)
academy.add_student(student2)
academy.add_subject(biology_subject)
academy.add_subject(geography_subject)

for teacher in academy.teachers:
    teacher.teach()

for student in academy.students:
    student.study()
