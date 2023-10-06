def insertionSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key.score < arr[j].score:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return f"{self.name}, Age: {self.age}, Score: {self.score}"
    

students = [
    Student("Shibili cv", 20, 99),
    Student("John", 23, 93),
    Student("Lilly", 26, 83),
    Student("Hary", 29, 73),
    Student("Bob", 32, 63)
]

insertionSort(students)

for student in students:
    print(student)
