def slsort(slist):
    n = len(slist)
    for i in range(n):
        minimum = i
        for j in range(i+1,n):
            if slist[j] < slist[minimum]:
                minimum = j
            slist[i],slist[minimum] = slist[minimum],slist[i]
            

li = [3,656,56,6,898]
a = slsort(li)
print(a)