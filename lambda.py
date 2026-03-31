# lambda function - anonymous function
# - useful when you need a short function for a sort time.

def add(a,b):
    return a+b

# lambda version 
add = lambda a,b : a+b
print(add(5,3))

square = lambda a:a*a
print(square(6))

numbers = [1,2,3,4]

for num in numbers:
    print(num)

for i, num in enumerate(numbers):
    print(i,num)


# iterationg dict:
student = {"name":"Ram","age":20}

for key,value in student.items():
    print(key,value)

#sorted() function

nums = [5,2,9,1]
print(sorted(nums))
print(sorted(nums,reverse=True))

students = [("Ram", 20), ("Shyam", 18), ("Hari", 22)]
sorted_students = sorted(students,key=lambda x :x[1])
print(sorted_students)

# - filter()
# used to filter elements based on condition

# filter(function,iterable)
numbers = [1,2,3,4,5]
even_numbers = list(filter(lambda x:x%2 ==0,numbers))
print(even_numbers)

#map() function
# used to apply a function to all elements

# Syntax:
# map(function(iterable))

numbers = [1,2,3,4]
squared = list(map(lambda x : x**2,numbers))
print(squared)

#multiple iterables:
a = [1,2,3]
b = [4,5,6]
result = list(map(lambda x, y: x + y, a, b))
print(result)


# #Lambda with map()
# map() applies a function to every item in a list

numbers = [1,2,3,4,5]
result = list(map(lambda x: x*2,numbers))
print(result)

#lambda with filter()
numbers = [4,6,7,8,9]
even = list(filter(lambda x : x % 2 == 0, numbers))
print(even)


# Lambda with sorted()
students = [
    ("Ram",20),
    ("shyam",18),
    ("Hari",22)
]
sorted_students = sorted(students,key=lambda x : x[1])
print(sorted_students)

#convert to the upper case
names = ["ram","shyam","subekshya"]
upper_names = list(map(lambda x : x.upper(),names))
print(upper_names)


#nested lambda
multiply = lambda x: lambda y: x * y
result = multiply(5)(3)
print(result)

#Lambda Returning Multiple Values
calc = lambda x: (x, x**2, x**3)
print(calc(3))
