#Q1
km=float(input("Enter kilometer: "))
miles=km*0.621371
print("Here is the the conversion of ",km," in miles ",miles)

#Q2
c=float(input("Enter Celcius Value: "))
f=c*33.8
print("The gives celcius value in farenheit scale is ",f,"degrees")

#Q3
import calendar
y=int(input("Enter year: "))
m=int(input("Enter month: "))
print(calendar.month(y,m))

#Q4
import cmath

a=7
b=9
c=5

qe=(b**2)-4*(a*c)

root1=(-b-cmath.sqrt(qe))/(2 * a)
root2=(-b+cmath.sqrt(qe))/(2 * a)

print("The roots are : ")
print(root1,root2)

#Q5
a=int(input("Enter 1st value: "))
b=int(input("Enter second value: "))
print("Values before swapping: ",a,b)
a,b=b,a
print("Values after swapping ",a,b)

