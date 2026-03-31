# numbers = [1, 2, 3, 4]

# # result = list(map(lambda x: x * 2, numbers))
# # print(result)


# # for x in numbers:
# #     result.append(x * 2)
# # print(result)



# # multiply(5)(3)

# nums = [1,2,3,4,5]
# square = map(lambda x : x **2,nums)
# print(list(square))

# nums = [1,2,3,4,5]
# square = filter(lambda x : x >3,nums)
# print(list(square))


# students = [
#     ("Ram", 80),
#     ("Shyam", 50),
#     ("Hari", 90)
# ]
# short = list(map(lambda x : x[0].upper(),students))
# print(short)

# marks = sorted(map(lambda x:( x[0], x[1]), students))
# print(marks)


# coords = [(27.7, 85.3), (28.2, 83.9), (29.0, 80.0)]

# filtered_cordinate = list(map(lambda x : x[0]>28,coords))
# print(filtered_cordinate)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello my name is {self.name} and I am {self.age } years old")

    def hobby(self):
        print(f"i loove dancing {self.name}")

p1 = Person("SUbekshya",23)
p2 = Person("Lokesh",25)
p1.hobby()
p1.greet()
p2.greet()

#class and the instance variable . class variable is constant for the class and instance variable is the current object
class Student :
    school = "ABC High School"

    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

s2 = Student("Bob", "B")
print(s2.name,s2.grade)


# #encaplulation  protection the secert data
# class Bank:
#     def __init__(self,balance):
#         self.__balance = balance

#     def deposit(self,amount):
#         self.__balance += amount

#     def withdraw(self,amount):
#         if amount <= self.__balance:
#            self.__balance -= amount

#         else:
#             print("Insuffcient funds")

#     def show_balance(self):
#         print("balance",self.__balance)

#     deposit("subu",100)



    #inheritance - 

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
            print(" Dog barks")

class Cat(Animal):
        def speak(self):
            print("cat meons")

d = Dog()
c = Cat()
d.speak()
c.speak()




def make_sound(animal):
     animal.speak()

make_sound(d)
make_sound(c)

class Bird:
    def speak(self):
        print("Bird chirps")

make_sound(Bird())