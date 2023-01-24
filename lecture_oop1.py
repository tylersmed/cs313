
class Car:
    
    def __init__(self, my_speed, mpg):
        self.speed = my_speed
        self.mpg = mpg

    def range(self, ammount_fuel):
        return self.mpg * ammount_fuel

    def run(self, current_speed):
        self.speed  = current_speed
        print("Car is running with " + str(self.speed) + " speed")

    def __str__(self):
        return "This car has " + str(self.mpg) + " MPG"

######################################################################

# Initialization of an object

#m_corolla = Car(0, 43)
#print(m_corolla.mpg)
#m_corolla.run(50)
#range = m_corolla.range(20)
#print("Range is " + str(range))
#print(m_corolla.__str__())

######################################################################

# Object orientied features:

    #Inheritance: Organization of abstractions according to some order
        # (e.g. complexity, responsibility, etc.)
        # ex haveing class Car and below that class Truck(Car)
    
    # Polymorphism

    # Encapsulation

    # Abstraction: 
        # Hiding the implementation complexity.
        # Offering computation services over Application
            # Programing Interfaces (API).