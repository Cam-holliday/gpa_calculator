def grade_check(grade):
    if(grade == 'A' or grade == 'a'):
        return 'a'
    elif(grade == 'A-' or grade == 'a-'):
        return 'a-'
    elif(grade == 'B+' or grade == 'b+'):
        return 'b+'
    elif(grade == 'B' or grade == 'b'):
        return 'b'
    elif(grade == 'B-' or grade == 'b-'):
        return 'b-'
    elif(grade == 'C+' or grade == 'c+'):
        return 'c+'
    elif(grade == 'C' or grade == 'c'):
        return 'c'
    elif(grade == 'C-' or grade == 'c-'):
        return 'c-'
    elif(grade == 'D+' or grade == 'd+'):
        return 'd+'
    elif (grade == 'D' or grade == 'd'):
        return 'd'
    elif (grade == 'D-' or grade == 'd-'):
        return 'd-'
    else:
        return 'big fat failure'

def credit_and_grade_math(cred, gpa):
     avg_gpa = gpa/cred
     total = avg_gpa/cred
     return avg_gpa

        
    

def letter_to_gpa(test):
    if(test == 'A' or test == 'a'):
        return 4.0
    elif(test == 'A-' or test == 'a-'):
        return 3.7
    elif(test == 'B+' or test == 'b+'):
        return 3.3
    elif(test == 'B' or test == 'b'):
        return 3.0
    elif(test == 'B-' or test == 'b-'):
        return 2.7
    elif(test == 'C+' or test == 'c+'):
        return 2.3
    elif(test == 'C' or test == 'c'):
        return 2.0
    elif(test == 'C-' or test == 'c-'):
        return 1.7
    elif(test == 'D+' or test == 'd+'):
        return 1.3
    elif (test == 'D' or test == 'd'):
        return 1.0
    elif (test == 'D-' or test == 'd-'):
        return 0.7
    else:
        return  0
        


first_last_total = []
total_avg_gpa = []
total_subjects = []
working_gpa = []
number_subjects = []
first_last_title = []
all_names = {}
i = True
while i == True:
    try:
        number_of_students = int(input('how many students do you have: '))
        if number_of_students % 1 == 0 and number_of_students > 0:
            i = False
        else:
            print('Oops, something went wrong. Try again')
    except:
        print('Oops, something went wrong. Try again')

#this starts the loop and asks how many times they want the loop to run
for i in range(int(number_of_students)):
    first_name_and_last = input('Enter the full name of student # ' + str(i + 1) + ': ')
    first_last_total.append(first_name_and_last)
    title_name = first_name_and_last.title()
    first_last_title.append(title_name)
#this asks how many subjects they have to
    
    i = True
    while i == True:
        try:
            number_of_subjects = int(input('please enter the number of subjects ' + title_name + ' has: '))
            if number_of_subjects % 1 == 0  and number_of_subjects > 0:
                number_subjects.append(number_of_subjects)
                i = False
            else:
                print('Oops, something went wrong. Try again')
        except:
            print('Oops, something went wrong. Try again')
            
#this begins asking for credits and grade         
    total_credits = 0
    total_gpa_score = 0
#this loop loops as many times as subjects you have
    
    for i in range(number_of_subjects):
        subjects = input('Enter the course name for subject # ' + str(i + 1 ) + ': ')
        title_course = subjects.title()
        total_subjects.append(subjects)
#the rest of this is all the math and questions for your given subject
        
        i = True
        while i == True:
            try:
                credits_subject = int(input('please enter how many credits ' + title_course + ' is worth: '))
                if credits_subject <= 2 and credits_subject >= 1 and credits_subject % 1 == 0:
                    i = False
                else:
                    print('Oops, something went wrong. Try again')
            except:
                print('Oops, something went wrong. Try again')
        
        i = True
        while i == True:
            grade = input('Please enter the letter grade for ' + title_course + ': ')
            grade_lower = grade.lower()
            if grade_lower == grade_check(grade_lower):
                temp_letter_to_gpa = letter_to_gpa(grade)
                working_gpa.append(temp_letter_to_gpa)
                i = False
            else:
                print('Oops, something went wrong. Try again')
        
        total_credits += credits_subject
        letter_to_grade_score = letter_to_gpa(grade)
        total_gpa_score += letter_to_grade_score * credits_subject
        
    total_avg_gpa.append(credit_and_grade_math(total_credits, total_gpa_score))



gpa_and_name = zip(total_avg_gpa, first_last_total)
working_gpa_and_subjects = zip(working_gpa, total_subjects)




print(list(working_gpa_and_subjects))
print(list(gpa_and_name))
print(working_gpa)
print(first_last_total)
print(total_avg_gpa)
print(total_subjects)
print(number_subjects)


for i in range(len(total_avg_gpa)):
    sentence = '{} received a total avgerage gpa of  {} gpa'.format(first_last_title[i], round(total_avg_gpa[i], 2))
    print(sentence)