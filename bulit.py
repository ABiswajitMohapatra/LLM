arr=[1,5,6,7,12,18,3,0]
largest=second=float('-intf')
for num in arr:
    if num>largest:
        second=largest
        largest=num
    elif largest > num > second:
        second=num
print(second)