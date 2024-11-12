# Исходные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество в отсортированный список для упорядочивания
student_list = sorted(students)

# Создаём пустой словарь для результатов
average_grades = {}

# Используем zip для объединения имён и оценок
for student, grade in zip(student_list, grades):
    # Вычисляем средний балл
    average_grade = sum(grade) / len(grade)
    # Добавляем в словарь
    average_grades[student] = average_grade

# Выводим итоговый словарь
print(average_grades)
