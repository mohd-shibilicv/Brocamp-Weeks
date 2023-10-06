def selectionSort(arr):
    size = len(arr)

    for i in range(size):
        min_index = i

        for j in range(i + 1, size):
            if arr[j].score < arr[min_index].score:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return f"{self.name}, Age: {self.age}, Score: {self.score}"
    

students = [
    Student("Shibili cv", 20, 99),
    Student("Bob", 31, 89),
    Student("Mark", 35, 82),
    Student("Lilly", 24, 79),
    Student("John", 24, 93)
]

selectionSort(students)

for student in students:
    print(student)
