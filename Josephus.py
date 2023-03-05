import sys

class Link(object):
    # Constructor
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class CircularList(object):
    # Constructor
    def __init__ ( self ):
        self.first = None

    # Insert an element (value) in the list
    def insert ( self, data ):
        newLink = Link(data)
        if self.first == None:
            self.first = newLink
            self.first.next = self.first
        else:
            newLink.next = self.first.next
            self.first.next = newLink
            self.first = newLink

    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find ( self, data ):
        if self.data_in_lst(data):
            current = self.first.next
            while current.data != data:
                current = current.next
            return current
        else:
            return None

    def data_in_lst(self, data):
        # Tests if a given data value is in the list
        if self.first == None:
            return False
        start = self.first.data
        current = self.first
        while current.next.data != start:
            if current.data == data:
                return True
            current = current.next
        if current.data == data:
            return True
        return False
    
    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete ( self, data ):
        del_this = self.find(data)
        if del_this == None:
            return None
        previous = del_this.next
        # If there is only one element in the list, return None for the now empty list
        if previous.data == del_this.data:
            self.first = None
            return None
        while previous.next.data != del_this.data:
            previous = previous.next
        # if the first element in the list is deleted, change self.first
        if previous.next.data > del_this.next.data:
            self.first = previous
        previous.next = del_this.next
        return del_this
        
    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after ( self, start, n ):
        current = self.find(start)
        if current == None:
            return None
        for i in range(n-1):
            current = current.next
        self.delete(current.data)
        return current.data, current.next

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__ ( self ):
        if self.first == None:
            # Print an empty list
            return "[]"
        first = self.first.next.data
        lst = ''
        current = self.first.next
        while current.next.data != first:
            # iterate through list list starting with the value after self.first
            # add the value to the returned string and stop adding when a full loop is made
            lst =  lst + str(current.data) + ', '
            current = current.next
        return '[' + lst + str(self.first.data) + ']'

def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int (line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int (line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int (line)

    # create the circular linked list
    soldierCircle = CircularList()
    for i in range(1, num_soldiers+1):
        soldierCircle.insert(i)

    # find the starting link
    current_soldier = soldierCircle.find(start_count)

    # Do the eliminations and print which soldier gets eliminated each time
    for i in range(num_soldiers):
        x = soldierCircle.delete_after(current_soldier.data, elim_num)
        deltd_sold, current_soldier = x
        print(deltd_sold)
    
if __name__ == "__main__":
    main()
