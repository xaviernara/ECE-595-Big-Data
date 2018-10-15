# Collaberated with Preston Porter and Javior Campos in this program

file = open('records.txt')

def displayGrades(grades,students):
    print('\nThe grades for each student are:\n')
    print('Student: ece595 ece547 ece354')
    
    letterGrade = ''
     
    for i in range(len(students)): # Length of the lists. Same as len(grades)
        for k in range(3):
            if k == 0:
                letterGrade = 'ece 595: '
            elif k == 1:
                letterGrade = letterGrade + 'ece 547: '
        
            else: 
                letterGrade = letterGrade + 'ece 354: '
                
            if int(grades[i][k]) >= 90:
                letterGrade = letterGrade + 'A\n'
            elif int(grades[i][k]) >= 80:
                letterGrade = letterGrade + 'B\n'
            elif int(grades[i][k]) >= 70:
                letterGrade = letterGrade + 'C\n'
            elif int(grades[i][k]) >= 60:
                letterGrade = letterGrade + 'D\n'
            else: 
                letterGrade = letterGrade + 'F\n'
        
        print(students[i],":")
        print(letterGrade )
        letterGrade = ''
    
def highestScore(grades,students):
    print('\nThe highest score in each subject are: ')            

    # Stores the highest score and the corresponding index 
    highest595 = [0,0]
    highest547 = [0,0]
    highest354 = [0,0]
    
    #displays the highest grade and student per class
    for i in range(len(students)):
        if grades[i][0] > highest595[0]:
            highest595[0] = grades[i][0];
            highest595[1] = i
        if grades[i][1] > highest547[0]:
            highest547[0] = grades[i][1]
            highest547[1] = i 
        if grades[i][2] > highest354[0]:
            highest354[0] = grades[i][2]
            highest354[1] = i
    
    print(students[highest595[1]], ':', highest595[0])
    print(students[highest547[1]], ':', highest547[0])
    print(students[highest354[1]], ':', highest354[0])
    print('\n')
    
def displayGPA(grades,students):
    print('\nThe GPA for each student is: ')

    credits = [] # Saves the credits earned in each subject for each student
    
    for i in range(len(students)):
        list1 = [] # Used to store the credits earned for each student
        for k in range(3):
            if grades[i][k] >= 90:
                list1.append(4)
            elif int(grades[i][k]) >= 80:
                list1.append(3)
            elif int(grades[i][k]) >= 70:
                list1.append(2)
            elif int(grades[i][k]) >= 60:
                list1.append(1)
            else:
                list1.append(0)
                
        credits.append(list1) # Appends list1 in credits
    
    
    gpa = [] # Used to store the GPA for each student
    for i in range(len(grades)):
         score = ((3*credits[i][0] + 3*credits[i][1] + 3*credits[i][2] )/ 9) # Calculates the GPA 
         score = round(score,2) # Rounds to 2 decimal places
         gpa.append(score) # Adds gpa to each list
    
    # Prints each student with their GPA
    for a,b in zip(students,gpa): 
        print(a,':',b)


decision = 0
students = []
grades = []

line = file.readline()  # Skip the first line of the file "student,ece595,ece547,ece354"

for line in file.readlines():
    val = line.strip()
    words = val.split()
    for word in words:
        a,b,c,d = word.split(',') 
        
        b,c,d = int(b),int(c),int(d)
        
        students.append(a)
        grades.append([b,c,d])


# User interaction
        
while True:
    print('\n\nInput: Action')
    print('-----------------------------------------------------------')
    print('    1: Display the grades for each student')
    print('    2: Display the highest score and scorer in each subject')
    print('    3: Display the GPA of each student')
    print('Other: Exit program')
    print('-----------------------------------------------------------')
    
    decision = input('Enter an input to display information: ')
   
    if decision.isdigit():
        decision = int(decision)
        if decision == 1:  
            displayGrades(grades,students)
        elif decision == 2:
            highestScore(grades,students)
        elif decision == 3:
            displayGPA(grades,students)
        else:
            break
    else:
        break
    
