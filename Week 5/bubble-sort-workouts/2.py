class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return f"{self.name}, Age: {self.age}, Score: {self.score}"


def bubbleSort(arr):
    length = len(arr)

    for i in range(length):
        for j in range(length - i - 1):
            if arr[j].score > arr[j + 1].score:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


students = [
    Student("Shibili cv", 20, 99),
    Student("Bob", 30, 89),
    Student("Lilly", 40, 85),
    Student("Roy", 25, 91),
    Student("Tim", 28, 81),
    Student("John", 31, 82)
]

bubbleSort(students)

for student in students:
    print(student)