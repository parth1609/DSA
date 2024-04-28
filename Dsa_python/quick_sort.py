def Quick_sort(list1):
    if len(list1) <= 1:
        return list1
    else:
        pivot = list1[0]
        lft = [x for x in list1 if x < pivot]
        right = [ x for x in list1 if x>pivot]

        return Quick_sort(lft)+ [pivot]+ Quick_sort(right)

li = [5,69,8,9,7,45,56]
mylist = Quick_sort(li)
print(mylist)