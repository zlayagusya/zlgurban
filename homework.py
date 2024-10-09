grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3],
          [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
dict_students = {}
names_students = list(students)
names_students.sort()
dict_students.update({names_students[0]: sum(grades[0]) / len(grades[0]),
                      names_students[1]: sum(grades[1]) / len(grades[1]),
                      names_students[2]: sum(grades[2]) / len(grades[2]),
                      names_students[3]: sum(grades[3]) / len(grades[3]),
                      names_students[4]: sum(grades[4]) / len(grades[4])})
print('Средние баллы учеников:', dict_students)