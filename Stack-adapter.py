from example_007_queue import Queue

class stack_adapter:

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        # Stacks are LIFO: add newest value to front of queue
        while not self.queue1.isEmpty():
            self.queue2.enqueue(self.queue1.dequeue())
        self.queue1.enqueue(item)
        while not self.queue2.isEmpty():
            self.queue1.enqueue(self.queue2.dequeue())

    def pop(self):
        # queue arranged in LIFO fashion by push method
        # first element of queue is the top of the stack
        return self.queue1.dequeue()

    def peek(self):
        # First element of queue is top of stack
        # view first element of queue
        return self.queue1.queue[0]


if __name__ == "__main__":
    # testing
    s = stack_adapter()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.queue1.__str__())
    print(s.pop())
    print(s.queue1.__str__())
    print(s.peek())
    print(s.queue1.__str__())