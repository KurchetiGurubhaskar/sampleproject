lst=[10,3,25,99,13,18,20,32,12]
print("list",lst)
def biggest(x):
    big=x[0]
    for i in x[1::]:
        if i > big:
            big=i
    return big
#calling
b=biggest(lst)
print("biggest",b)
