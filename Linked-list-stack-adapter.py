from example_008_linked_list import LinkedList

class stack_adapter2:

    def __init__(self):
        self.list = LinkedList()

    def push(self, item):
        # stack is LIFO: insert new values to begining of list
        self.list.insertFirst(item)

    def pop(self):
        # stack pops the top element: return first link in list
        # and delete that link
        top = self.list.first.data
        self.list.deleteLink(top)
        return top        

    def peek(self):
        # return the first value in the linked list
        return self.list.first.data

if __name__ == "__main__":
    # testing
    l = stack_adapter2()
    l.push(10)
    l.push(20)
    print(l.list)
    print(l.peek())
    print(l.pop())
    l.push(30)
    l.push(100)
    print(l.list)
