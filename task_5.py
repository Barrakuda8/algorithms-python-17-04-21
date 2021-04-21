"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""

# Реализована система стэков при которой после переполнения первого стэка создаётся новый.
# Каждый стэк кроме первого имеет информацию о своём предшественнике,
# и каждый стэк кроме крайнего имеет информацию о последователе.
# Таким образом если заканчиваются тарелки в крайнем стэке, они берутся из предшественника,
# И если в текущем стэке нет места, создаётся новый.
# Метод get_quantity возвращает количество тарелок во всех стэках цепи


class Plate:

    def __init__(self, color='white', shape='circle'):
        self.color = color
        self.shape = shape


class Stack:

    def __init__(self, size, previous=None):
        self.size = size
        self.previous = previous
        self.next = None
        self.plates = []

    def push_in(self, plate):
        if len(self.plates) < self.size:
            self.plates.append(plate)
        elif len(self.plates) >= self.size:
            if self.next is None:
                self.next = Stack(self.size, self)
            self.next.push_in(plate)

    def pop_out(self):
        if self.next is not None:
            if not self.next.is_empty():
                self.next.pop_out()
                return
        if not self.is_empty():
            return self.plates.pop()
        else:
            if self.previous is not None:
                self.previous.pop_out()
            else:
                print('Тарелки кончились')

    def is_empty(self):
        return self.plates == []

    def get_quantity_next(self, init_stack_quantity):
        if self.next is not None:
            return self.next.get_quantity_next(init_stack_quantity + len(self.next.plates))
        else:
            return init_stack_quantity

    def get_quantity(self):
        if self.previous is not None:
            self.previous.get_quantity()
        else:
            return self.get_quantity_next(len(self.plates))


stack = Stack(5)
for _ in range(6):
    stack.push_in(Plate())
    print(stack.get_quantity())
for _ in range(7):
    stack.pop_out()
    print(stack.get_quantity())

