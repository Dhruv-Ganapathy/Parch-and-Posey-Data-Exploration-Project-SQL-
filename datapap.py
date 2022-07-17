#35 python coding questions

#1 program to reverse a number
'''a="277"
print(a[::-1])'''
#2 reversing a string using for loop
'''a="Hello World"
reverse=""
for i in a:
    reverse=i+reverse
print(reverse)'''

#3 to find number is armstrong number or not
num=int(input("Enter the number: "))
order=len(str(num))
sum=0
temp=num   #temp value keeps changing, so to compare sum with num we create temp
while(temp>0):  
    digit=temp%10 #to get last element of the number
    sum+=digit**order
    temp//=10   #to get absolute quotient of the number
if(sum==num):
    print("the number {} is an armstrong number".format(num))
else:
    print("the number {} is not an armstrong number".format(num))
#4 prime number
'''n=int(input())
if(n>0):
    for i in range(2,n+1):
        if(n%i==0):
            break
    if(i==n):
        print("the number is prime")
    else:
        print("the number is not prime")
else:
    print("enter a number greater than 1")'''
#5 cognizant interview question
'''l=list(map(int,input().split()))
a,b,c=0,0,0
for i in range(0,2):
    a+=l[i]
for i in range(2,4):
    b+=l[i]
for i in range(4,6):
    c+=l[i]
print(a,b,c)'''

#6 multiplicaton table
'''for i in range(1,11):
    print("2 x",i,"=",2*i)'''
#print([i*3 for i in range(1,11)]) #multiplication using list comprehension

#7 using zip function to multiply two lists
'''l1=[1,2,3]
l2=[4,5,6]
p=[a*b for a,b in zip(l1,l2)]  #zip lets us combine two lists
print(p)
'''
#8 factorial of a number using for loop and a fact variable
'''n=int(input())
fact=1
if(n>1):
    for i in range(1,n+1):
        fact=fact*i
print(fact)'''
#9 Python program to display all the prime numbers within an interval
'''l=int(input())
u=int(input())         #count=0
for num in range(l,u+1):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)'''# add count+=1 after this to see the count of prime number
                         # in this range
#10 to find sum of natural numbers
'''n=int(input())
sum=0
for i in range(n+1):
    sum+=i
print(sum)'''
#11 swapping first and last element in a list
'''l=[1,2,3,4]
temp=l[0]
l[0]=l[-1]
l[-1]=temp
print(l)'''
#12 taking input from users putting them in a list and finding average
n=int(input("enter how many number you want the average for: "))
l=[]
sum=0
for i in range(n):
    a=int(input())
    l.append(a)
for i in l:
    sum+=i
avg=sum/n
print(avg)
#13 swapping two numbers without using 3rd variable
a,b=int(input()),int(input())
print(a,b)
a=a-b
b=a+b
a=b-a
print(a,b)
#14 count the number of times vowels have been used in the string
# regex module - findall function
import re
x="hey there whatsup im using whatsapp and all other can go fuck yourself AEIOU"
count=0
y=re.findall("[aeiouAEIU]",x)
for i in y:
    count+=1
print(count)
#15 program to replace white space with a number
# using the regex module - sub functon
import re
x="hey there whatsup im using whatsapp and all other can go fuck yourself AEIOU"
count=0
y=re.sub("[ ]","9",x)
print(y)
#16 program to find count of alphabets, numbers and special charecters
#using regex module - findall function
import re
n=str(input())
a,b=0,0
x=re.findall("[a-z]",n)
for i in x:
    a+=1
y=re.findall("[0-9]",n)
for i in y:
    b+=1
z=len(n)-a-b
print(a)
print(b)
print(z)
#17 program to find names using startswith and endswith function
txt = """Aaron
Abner
Abraham
Ace
Adam
Adrian
Aesop
Alan
Alastair
Alex
Alexander
Alfie
Alfred
Alvaro
Anatole
Ander
Andrew
Angus
Anthony
Arnold
Arsenio
Asher
August
Axel
Aziz"""
count=0
y=txt.split()
for i in y:
    if(i.startswith("A") and (i.endswith("n"))):
        count+=1
print(count)
#18 program to reverse elements in a list
l=[1,2,3,4,5]
l.reverse()
print(l)
#19 print the square of elements in a list
numbers = [1, 2, 3, 4, 5, 6, 7]
l=[]
for i in numbers:
    l.append(i**2)
print(l)
#20 iterate two list simultaneously and print them in following order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)
#21 printing list without null element
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
res=list(filter(None,list1))
print(res)
#22 understanding multiple index position and appending new element
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)
#23 using extend to insert a sublist in a nested list
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list=["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)
#24 removing a particular elements of repeated occurances
list1 = [5, 20, 15, 20, 25, 50, 20]
for i in list1:
    if(i==20):
        list1.remove(20)
print(list1)
#25 using single line for loop to find square of list elements
list1 = [5, 20, 15, 20, 25, 50, 20]
p=[i**2 for i in list1]
print(p)
#26 find number of digits in sequence of numbers using while loop
a=75869
count=0
while(a!=0):
    a//=10
    count+=1
print(count)
#27 popping elements from one list and inserting them in another
l=[1,2,3,4,5]
m=[]
for i in range(len(l)):
    a=l.pop()
    m.insert(i,a) #can insert elements in list l also
print(m)
#28 to find if number is a palindrome without using built in functions
n=int(input("enter a number: "))
m=str(n)
n=""
for i in m:
    n=i+n
if(n==m):
    print("the number is a palindrome")
else:
    print("the number is not a palindrome")





