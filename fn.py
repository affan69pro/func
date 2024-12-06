def cal(len,sid):
    return len*sid

print("This will calculate the perimeter of your shape")
lenth=float(input("enter the length of sides: "))
numsid=int(input("now enter the number of sides: "))
ans=cal(lenth,numsid)
print("the perimeter is ",ans)