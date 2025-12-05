def filter_students_by_grade(students, threshold):
    """Фильтрует студентов по среднему баллу"""
    filtered_students = []
    for student in students:
        avg_grade = sum(student['marks']) / len(student['marks'])
        if avg_grade > threshold:
            filtered_students.append(student)
    return filtered_students

def print_students(students):
    """Выводит список студентов в форматированном виде"""
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), 
              student["surname"].ljust(10), 
              str(student["exams"]).ljust(30), 
              str(student["marks"]).ljust(20))

# Пример данных
groupmates = [
    {
        "name": "Алексей",
        "surname": "Иванов",
        "exams": ["Математика", "Физика"],
        "marks": [4, 5]
    },
    {
        "name": "Мария",
        "surname": "Петрова",
        "exams": ["История", "Литература"],
        "marks": [5, 5]
    },
    {
        "name": "Иван",
        "surname": "Сидоров",
        "exams": ["Химия", "Биология"],
        "marks": [3, 4]
    }
]

# Основная логика программы
try:
    threshold = float(input("Введите пороговый средний балл для фильтрации: "))
    filtered = filter_students_by_grade(groupmates, threshold)
    print(f"\nСтуденты со средним баллом выше {threshold}:")
    print_students(filtered)
except ValueError:
    print("Ошибка: Введите корректное число")