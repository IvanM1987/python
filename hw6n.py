# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.


# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class LessonType:
    def __init__(self, subject):
        self.whatever = subject


class Teacher(LessonType):
    def __init__(self, subject, name, grade):
        super().__init__(subject)
        self.grade = grade
        self.name = name

    def learning(self):
        return self.whatever


class Student:
    def __init__(self, grade, name, dad, mom):
        self.grade = grade
        self.name = name
        self.father = dad
        self.mother = mom

    def fio(self):
        a = self.name
        name_letter = list(a)
        b = self.father
        fathers_name_letter = list(b)
        return self.father.split(' ')[2] + ' ' + name_letter[0] + '.' + fathers_name_letter[0] + '.'


lessons = [LessonType('Русский'),
           LessonType('Математика'),
           LessonType('Физика'),
           LessonType('Рисование')
           ]
teachers = [Teacher('Русский', 'Надежда Михайловна', '6A, 6B, 7A'),
            Teacher('Математика', 'Александр Сергеевич', '6B, 7A, 7B'),
            Teacher('Физика', 'Олег Николаевич', '6A,7A,7B'),
            Teacher('Рисование', 'Ольга Павловна', '6B, 7A, 7B'),
            ]
students = [Student('6A', 'Олег', 'Петр Сергеевич Иванов', 'Мария Александровна Иванова'),
            Student('6B', 'Маша', 'Владимир Михайлович Сидоров', 'Ольга Сергеевна Сидорова'),
            Student('6B', 'Катя', 'Александр Сергеевич Пушкин', 'Александра Сергеевна Пушкина'),
            Student('7A', 'Миша', 'Глеб Борисович Медведев', 'Алла Николаевна Медведева'),
            Student('7A', 'Вася', 'Иван Александрович Бородач', 'Надежда Игоревна Бородач'),
            Student('7A', 'Даша', 'Михаил Владимирович Полевой', 'Римма Николаевна Полевая'),
            Student('7B', 'Оля', 'Артем Иванович Смирнов', 'Зоя Сергеевна Смирнова'),
            Student('7B', 'Виталик', 'Андрей Валерьевич Галкин', 'Елена Владимировна Галкина'),
            Student('7B', 'Петя', 'Тарас Семенович Бульба', 'Лера Павловна Бульба'),
            Student('7B', 'Оля', 'Василий Анатольевич Головачев', 'Лариса Прокофьевна Головачева')
            ]


# for num, Student in enumerate(students):
#     print(num, Student.grade)


# x = input('Учеников какого класса отфильтровать?\n'
#           '6A\n'
#           '6B\n'
#           '7A\n'
#           '7B\n')
# for Student in students:
#     if x == Student.grade:
#         print(Student.grade, Student.fio())


# x = input('Выберите имя ученика?\n'
#           'Олег\n'
#           'Маша\n'
#           'Катя\n'
#           'Миша\n'
#           'Вася\n'
#           'Даша\n'
#           'Оля\n'
#           'Виталик\n'
#           'Петя\n'
#           'Оля')
# for Student in students:
#     if x == Student.name:
#         a = Student.grade
#         for Teacher in teachers:
#             if a in Teacher.grade:
#                 print(Teacher.learning())

# x = input('Выберите имя ученика?\n'
#           'Олег\n'
#           'Маша\n'
#           'Катя\n'
#           'Миша\n'
#           'Вася\n'
#           'Даша\n'
#           'Оля\n'
#           'Виталик\n'
#           'Петя\n'
#           'Оля')
#
# for Student in students:
#     if x == Student.name:
#         print(Student.father, Student.mother)

x = input('Учителей какого класса отфильтровать?\n'
          '6A\n'
          '6B\n'
          '7A\n'
          '7B\n')
for Teacher in teachers:
    if x in Teacher.grade:
        print(Teacher.name)