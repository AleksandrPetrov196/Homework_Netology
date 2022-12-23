class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def average(self):
        average_grades = sum(self.grades)/len(self.grades)
        return average_grades
    def rate_lecturer(self, lecturer, course, grade_l):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses \
           and course in lecturer.courses_attached:
            if course in lecturer.student_grades:
                lecturer.student_grades[course] += [grade_l]
            else:
                lecturer.student_grades[course] = [grade_l]
        else:
            return 'Ошибка'
    def __str__(self, name):
        some_student = f'Имя: {self.name} \nФамилия: {self.surname}\
\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\
\nЗавершенные курсы: {", ".join(self.finished_courses)}\
\nСредняя оценка за домашние задания: {Student.average}'
        return some_student

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.student_grades = {}
    def average(self):
        average_amount = sum(sum(self.student_grades.values(), [])\
                             / len(sum(self.student_grades.values(), [])))
        return average_amount
    def __str__(self, name):
        some_lecturer = f'Имя: {self.name} \nФамилия: {self.surname} \
\nСредняя оценка за проведение лекций: {self.average}'
        return some_lecturer


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
           and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self, name):
        some_reviewer = f'Имя: {self.name} \nФамилия: {self.surname}'
        return some_reviewer


best_student = Student('Ruoy', 'Eman', 'Man')
best_student.courses_in_progress += 'Python','Git'
best_student.finished_courses += ['Введение в программирование']
first_student = Student('Bill', 'Klinton', 'Man')
first_student.courses_in_progress += 'Python','Git'
second_student = Student('Margaret', 'Tetcher', 'Woman')
second_student.courses_in_progress += 'Python'
second_student.finished_courses += ['Git']

best_lecturer = Lecturer('Klava', 'Koka')
best_lecturer.courses_attached += 'Python','Git'
first_lecturer = Lecturer('Ben', 'Afflek')
first_lecturer.courses_attached += 'Python'
second_lecturer = Lecturer('Sergey', 'Bodrov')
second_lecturer.courses_attached += 'Git'

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python','Git']
first_reviewer = Reviewer('Petr', 'Yan')
first_reviewer.courses_attached += ['Python']
second_reviewer = Reviewer('Albert', 'Enshtein')
second_reviewer.courses_attached += ['Git']



best_student.rate_lecturer(best_lecturer, 'Git', 10)
first_student.rate_lecturer(best_lecturer, 'Git', 7)
second_student.rate_lecturer(best_lecturer, 'Git', 9)


cool_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 9)
second_reviewer.rate_hw(best_student, 'Python', 8)


print(best_student.grades)
print(best_lecturer.student_grades)




some_reviewer = cool_reviewer.__str__(cool_reviewer)
some_lecturer = best_lecturer.__str__(best_lecturer)
some_student = best_student.__str__(best_student)
print(some_reviewer)
print(some_lecturer)
print(some_student)


#student_grade_average = Student.average
#lecturer_grade_average = Lecturer.average 
#def comparison():
#    if student_grade_average < lecturer_grade_average:
#        print('У лектора оценка выше')
#    elif student_grade_average > lecturer_grade_average:
#        print('у студента оценка выше')
#    else:
#        print('Оценки одинаковые')
#comparison()

#for stud, grade in Student.grades:
#    print(stud)
#    for ingred in ingredient:  
#        print(ingred[0], ingred[1] * person, ingred[2])
ss = Student.grades()
print(ss)
