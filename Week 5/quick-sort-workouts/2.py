def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x.score <= pivot.score]
        greater = [x for x in arr[1:] if x.score > pivot.score]
        
        return quickSort(less) + [pivot] + quickSort(greater)
    

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return f"{self.name}, Age: {self.age}, Score: {self.score}"
    

students = [
    Student("Shibili cv", 20, 99),
    Student("Bob", 30, 89),
    Student("Lilly", 25, 79),
    Student("Baby", 34, 86),
    Student("Hary", 20, 83)
]

sorted_students = quickSort(students)

for student in sorted_students:
    print(student)
