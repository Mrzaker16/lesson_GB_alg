# Задание 5.


class StackClass:
    def __init__(self):
        self.elems = [[],[],[],[],[]]

    def push_in(self, el):
        for i in range(0, len(self.elems) - 1, 1):
            if len(self.elems[i]) < 5:
                self.elems[i].append(el)
                break

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

class Stack:
    def __init__(self):
        self.stack = []
        self.max = None

    def push(self, item):
        self.stack.append(item)
        if len(self.stack) == 1 or item > self.max:
            self.max = item

if __name__ == '__main__':
    stack_1 = StackClass()
    i = 0
    while i < 20:
        stack_1.push_in(1+i)
        i += 1

    print(stack_1.elems)