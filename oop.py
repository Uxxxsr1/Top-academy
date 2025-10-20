class Stack:
    def __init__(self):
        self.__stackList = []

    # Метод push что то положить
    def push(self, val):
        self.__stackList.append(val)

    # Метод pop что то забрать
    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val
# Создаем стек
stack_obj0 = Stack()

# Добавляем элементы в наш стек
stack_obj0.push(5)
stack_obj0.push(7)
stack_obj0.push(0)

# Выводим и доставем элементы по очереди, с конца
print(stack_obj0.pop())
print(stack_obj0.pop())
print(stack_obj0.pop())