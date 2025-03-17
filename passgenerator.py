import string
import random

s1=string.ascii_lowercase
#print(s1)
s2=string.ascii_uppercase
#print(s2)
s3=string.punctuation
#print(s3)
s4=string.digits
#print(s4)
s=[]
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
#print(s)
random.shuffle(s)
x=int(input("ENTER THE LENGTH OF THE PASSWORD: "))
a="".join(s[0:x])
print("PASSWORD GENERATED IS:  ",a)
#without shuffle :
#a="".join(random.choices(s,x))
