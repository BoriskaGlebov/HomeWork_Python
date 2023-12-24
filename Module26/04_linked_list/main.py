print('Задача 4. Односвязный список')


class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, val):
        n = self
        end = LinkedList(val)
        while n.next:
            # print(n.data)
            n = n.next
        n.next = end

    def get(self, num):
        n = self
        count = 0
        while n.next:
            if num == count:
                print(n.data)
                return
            n = n.next
            count += 1
            if n.next is None and count == num:
                print(n.data)
                return
        else:
            raise ValueError

    def out_gen(self):
        n = self
        # print(n.data, end=' ')
        while n.next:
            out = n.data
            yield out
            n = n.next
            if n.next is None:
                yield n.data
        print()

    def out_print(self):
        n = self
        # print(n.data, end=' ')
        while n.next:
            print(n.data, end=' ')
            n = n.next
            if n.next is None:
                print(n.data, end=' ')
        print()

    def remove(self, num):
        n = self
        count = 0
        next_obj = None
        while n.next:
            if count == num:
                next_obj = n.next
                break
            n = n.next
            count += 1
        count = 0
        n = self
        while n.next:
            if count == num - 1:
                n.next = next_obj
                break
            n = n.next
            count += 1
        else:
            raise ValueError


d = LinkedList(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.append(6)
d.append(7)
d.append(8)
d.append(9)
d.append(10)

for el in d.out_gen():
    print(el, end=' ')
d.out_print()
d.get(5)
d.remove(3)
d.out_print()
d.remove(8)
d.out_print()
