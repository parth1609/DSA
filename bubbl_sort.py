def bubble_sort(data_list):
    for i in range(1,len(data_list)-1):
        for j in range(len(data_list)-i):
            if data_list[j] > data_list[j+1]:
                data_list[j],data_list[j+1] = data_list[j+1],data_list[j]
            

def modfied_bubble_sort(data_list):
    flag = False
    for i in range(1,len(data_list)-1):
        flag = False
        for j in range(len(data_list)-i):
            if data_list[j] > data_list[j+1]:
                data_list[j],data_list[j+1] = data_list[j+1],data_list[j]
                flag = True
        if flag == False:
                break

        



l = [54,89,6,35,12,566]
modfied_bubble_sort(l)
print(l)