# Month 1 Week 1 Day 2 - Arka Jain BCA AI prep 
# Goal :Use lists + loops + if-else for BCA marks logic 

# Basic 1: Lists - store 5 subjects marks 
subjects = ["Maths" , "Python", "English","Web dev", "AI Basics"]
marks = [85,92,78,88,95]

print("=" *40)
print("BCA SEM 1 MARKS CALCULATOR")
print ("=" * 40)

#Basic 2 : For loop - print each subject 
for i in range (len(subjects)):
    print (f"{subjects[i]}: {marks[i]}/100")

#Basic 3 : Calculate total using loop 
total=0
for mark in marks: 
    total=total+mark

max_marks=len(marks)*100
percentage = (total/max_marks)*100 

print("=" *40)
print (f"Total :{total}/{max_marks}")
print (f"Percentage: {percentage:.2f}%")

#Basic 4 : if-elif-else for Grade
if percentage >=90:
    grade ="A - top 1% Tier"
elif percentage >=75 :
    grade ="B - Good"
elif percentage >=60:
    grade= "C - Average"
elif percentage >=40:
    grade = "D - Pass"
else :
    grade = "F-Fail"

print (f"Grade: {grade}")
print("=" *40)
print (f"Days completed :2/90 = {2/90*100:.1f}%")