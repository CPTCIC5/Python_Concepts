#x,y=int(input()),int(input())
"""
if x < y:
    print('x is less then y')
elif x > y:
    print('x is greater then y')
#elif x==y:
else:
    print('eQUAL')
"""

"""
if x>y or x<y:
    print('not equal')
else:
    print('equal')
"""


"""
if x==y:
    print('equal')
else:
    print('not equal')
"""


"""
score= int(input('Score: '))

if score >=90 and score <=100:
    print("Grade: A")

elif score >=80 and score <=90:
    print("Grade :B")

elif score >=70 and score <=80:
    print('Grade :C')

elif score >=60 and score <=70:
    print("Grade D")

else:
    print('Fail')
"""

"""
student_percentage=int(input('Percentage'))
grade = "Fail"
print(grade)
if student_percentage > 60:
    grade = "First Class"
    print(grade)
elif student_percentage > 50:
    grade = "Second Class"
    print(grade)
elif student_percentage > 35 and student_percentage < 50:
    grade = "Third Class"
    print(grade)
else:
    grade = "Fail"
    print(grade)
"""


"""
x= int(input('whats x'))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
"""


"""
def main():
    x=int(input('whats x'))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
"""


"""
i=0
while i != 3:
    print('while true ka alt.')
"""


"""
i=3
while i!=0:
    print('xyz')
    i-=1
"""

'''
for i in range(3):
    print(i)
'''

"""
xyz='aryan'
for a in range(len(xyz)):
    print(a,xyz[a])
"""


students = ['aryan','darius','4v']
"""
for student in range(len(students)):
    print(student,students[student])
"""
address=['nai basti','chadni chauk','gb road']

x1=dict(zip(students,address))

for i in x1:
    print(i,x1[i])