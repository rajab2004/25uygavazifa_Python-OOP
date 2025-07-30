class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"{self.name}, {self.age} yosh")

students = [
    Student("Ali", 14),
    Student("Laylo", 15),
    Student("Aziz", 17),
    Student("Sardor", 13),
    Student("Jasur", 16)
]

oldest = students[0]
for s in students:
    if s.age > oldest.age:
        oldest = s

print("Eng katta talaba:")
oldest.show_info()