"""
Задание 6.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""

# Первая созданная для доски задач задача создаёт обе нужные очереди и список решённых задач.
# Удобнее было бы реализовать также интерфейс для работы с доской задач, но в момент когда я об этом подумал,
# это требовало бы переделать всю структуру классов, так что пришлось ограничиться ручной проверкой.

class Queue:

    def __init__(self):
        self.tasks = []

    def to_queue(self, task):
        self.tasks.insert(0, task)

    def from_queue(self):
        if len(self.tasks) != 0:
            return self.tasks.pop()
        else:
            print("Задач в очереди нет")

    def next_task_description(self):
        print(self.tasks[-1].description)

    def get_quantity(self):
        return len(self.tasks)

    def __str__(self):
        return str(list(map(str, self.tasks)))


class Task:

    def __init__(self, description, to_do=None, to_rework=None, done=None):
        if to_do is None:
            to_do = Queue()
            to_rework = Queue()
            done = []
        self.to_do = to_do
        self.to_rework = to_rework
        self.done = done
        self.to_do.to_queue(self)
        self.description = description

    def add_to_rework(self):
        self.to_rework.to_queue(self)

    def is_done(self):
        self.done.append(self)

    def __str__(self):
        return self.description


task = Task('задача 1')
to_do = task.to_do
to_rework = task.to_rework
done = task.done

task2 = Task('задача 2', to_do, to_rework, done)
print(to_do)
print(to_rework)

to_do.next_task_description()
to_do.from_queue().is_done()
to_do.from_queue().add_to_rework()
print(to_do)
print(to_rework)

to_rework.from_queue().is_done()
print(to_do)
print(to_rework)

