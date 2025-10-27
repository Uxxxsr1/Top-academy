student = {
    'name': 'Anna',
    'age': 25,
    'well': 4
}
print(student['name'])
student['city'] = 'London'
print(student['city'])
student['age'] = 26
print(student['age'])
student['grade'] = 'A'
print(student.get('grade'))
print(student.keys())
print(student.values())

coordinates = (10,20,30)
x,y,z= coordinates
print(x,y,z)    
data = [1,2,3,4,5,6]
firstEl, *mid, lastEl = data
print(firstEl, lastEl, mid)
numbers = [1,2,3]
#a,b,c = numbers
#def sums(a,b,c):
    #total = a*b*c
    #print(f'Multipluy: {total}')
#sums()
def description(**parametrs):
    for key, item in parametrs.items():
        print(f'{key.capitalize()}: {item}')
description(name='Ivan',age=26,job='developer',city='Moscow')