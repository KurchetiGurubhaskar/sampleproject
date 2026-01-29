#accept the number from the user,
#findout the number from the given number is armstrong number are not
n=153
temp=n
s=0
while n!=0:
    r=n%10
    s=s+(r*r*r)
    n=n//10
print(s)
if s==temp:
    print("ARMSTRONG")
else:
    print("not")
