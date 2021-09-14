# 1: Add new student
# 2: Add new score for students
# 3: View students list

def inputProgram():
    validCommands = [1, 2, 3, 4]
    while True:
        prompt = int(input("Enter your program: "))
        if prompt in validCommands:
            return prompt
        print("Invalid command")

studentsList = []

def addNewStudent():
    print("Add new student")
    name = input("Enter student name: ")
    data = {
        "name": name,
        "score": 0
    }
    studentsList.append(data)
    print("Student has created.")

def showStudentList():
    print("Show student list")
    for student in studentsList:
        index = studentsList.index(student)
        print(index + 1, ': name =', student['name'], ', score =', student['score'])

def setScoreForStudent():
    print("Set score for student")
    searchName = input("Enter student name: ")
    filterCondition = lambda student: student['name'] == searchName
    filteredStudents = list(filter(filterCondition, studentsList))
    if len(filteredStudents) > 0:
        student = filteredStudents[0]
        index = studentsList.index(student)
        student['score'] = input('Enter score for student: ')
        studentsList[index] = student
    else:
        print("Student not found.")

while True:
    print("1: Add new student")
    print("2: Set score for each student")
    print("3: Show students list")
    print("4: Exit")

    programId = inputProgram()

    if programId == 1:
        addNewStudent()
    elif programId == 2:
        setScoreForStudent()
    elif programId == 3:
        showStudentList()
    elif programId == 4:
        exit()