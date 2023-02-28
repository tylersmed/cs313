from example_006_stack import Stack

class queue_adapter:

    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def enqueue(self, item):
        # FOFO: enqueue should add to bottom of stack
        while not self.stack1.isEmpty():
            self.stack2.push(self.stack1.pop())
        self.stack1.push(item)
        while not self.stack2.isEmpty():
            self.stack1.push(self.stack2.pop())


    def dequeue(self):
        # Enqueue method arranges stack 1 in FOMO fassion
        # Therefore, remove top of stack
        self.stack1.pop()

if __name__ == "__main__":
    # testing
    queue = queue_adapter()
    queue.enqueue(60)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.stack1.__str__())
    queue.dequeue()
    queue.enqueue(50)
    queue.dequeue()
    print(queue.stack1.__str__())