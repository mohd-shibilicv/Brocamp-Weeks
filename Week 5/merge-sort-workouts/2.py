def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:1]
    right = arr[1:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i].score < right[j].score:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
        
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return f"{self.name}, Age: {self.age}, Score: {self.score}"
    

students = [
    Student("Shibili cv", 20, 99),
    Student("Bob", 30, 88),
    Student("Lilly", 24, 84),
    Student("Rose", 26, 80),
    Student("Hary", 32, 76)
]

mergeSort(students)

for student in students:
    print(student)
