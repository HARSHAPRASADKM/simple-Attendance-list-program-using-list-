list_of_students =['abhishek','arjun','chandrashekar','chethan','darshan','deependra','dhanaraj',
                   'Harsha','jeevan','karthik','karunakara',]
present_students=[]
absent_students =[]
i=0
def taking_attendance():


    for i in range(len(list_of_students)):		
        print(f"name of student = {list_of_students[i]}")
        attendance=input("if student is 'p' or 'a':")
        if attendance == 'p':
             present_students.append(list_of_students[i])
        else :
                absent_students.append(list_of_students[i])
print(f"name of student = {list_of_students[i]}")
attendance=input("if student is 'p' or 'a':").lower()
if attendance != "p" or attendance != "a":
    print("Please ,enter the valid character to indicate the present and absent ")
    exit(0)
taking_attendance()

print("the attented students are : ")
for j in range(len(present_students)):
    print(present_students[j])

for s in range(5):
    print("\n")
print("the absent students are : ")
for k in range(len(absent_students)):
    print(absent_students[k])
