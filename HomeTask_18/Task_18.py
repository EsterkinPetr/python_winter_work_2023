class Task:
    def __init__(self, lesson, num):
        self.lesson = lesson
        self.task_num = num


class Teacher:
    def __init__(self, name):
        self.name = name
        self.for_check = 0
        self.checked = 0

    def __str__(self):
        return self.name

    def give_task(self, lesson, num):  #преподаватель задает задачу каждому из учеников
        task = Task(lesson, num)
        for i in Pupil.pupil_list:
            i.reciev_task.append((lesson, num))  # задача добавляется каждому ученику в список получ. задач
            print(f'Список полученных задач {i}:{i.reciev_task}')
        self.for_check += len(Pupil.pupil_list)

    def check_ok(self, lesson, num, pupil): # преподаватель проверил задачу у конкретного ученика, и она решена верно
        p = pupil
        p.ok_task.append((lesson, num))
        print(f'Список зачтенных задач {p}: {p.ok_task}')
        print(f'Список не зачтенных задач {p}: {p.mist_task}')
        self.checked += 1
        print(f'Преподаватель: {self.name}, задач на проверку: {self.for_check}, проверено задач: {self.checked}')

    def check_mist(self, lesson, num, pupil):   # преподаватель проверил задачу у конкретного ученика, и она решена  не верно
        p = pupil
        p.mist_task.append((lesson, num))
        print(f'Список зачтенных задач {p}: {p.ok_task}')
        print(f'Список не зачтенных задач {p}: {p.mist_task}')
        self.checked += 1
        print(f'Преподаватель: {self.name}, задач на проверку: {self.for_check}, проверено задач: {self.checked}')

class Pupil:
    pupil_list = []
    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name
        self.reciev_task = []
        self.mist_task = []
        self.ok_task = []
        Pupil.pupil_list.append(self)
        print(f'Список учеников:{str(Pupil.pupil_list)}')



i = Pupil('Иван')
s = Pupil('Семен')
f = Pupil('Федор')
mmz = Teacher('Михаил')
mmz.give_task(19, 1)
mmz.check_ok(19, 1, i)
mmz.check_mist(19, 1, s)
mmz.check_ok(19, 1, f)
mmz.give_task(19, 2)






