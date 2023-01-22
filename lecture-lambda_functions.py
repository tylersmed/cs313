
a = 2
b = (lambda x: x ** 2) (a)
print(b)

a = [1, 2, 3, 4, 5]
b = list(map(lambda x : x ** 2, a))
print(b)
# list comprehension version of this code:
    # b = [item**2 for item in a]

my_functions = [lambda s: 'LOWER CASE: ' + s.lower(),
                lambda s: 'UPPER CASE: ' + s.upper(),
                lambda s: 'Head: ' + s[:5],
                lambda s: 'Tail: ' + s[-5:]
                ]

for i in range(len(my_functions)): 
    print(my_functions[i]('Hello World'))