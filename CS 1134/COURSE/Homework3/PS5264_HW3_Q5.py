def split_by_sign(lst,low,high):
    if low==high:
        return
    else:
        if lst[low]<0:
            split_by_sign(lst,low+1,high)
        else:
            lst[low],lst[high]=lst[high],lst[low]
            split_by_sign(lst,low,high-1)

list=[1,2,3,4,-2,3,-8,20,-439,-24,-34,2,4,5,-34,34,-4]
split_by_sign(list,0,len(list)-1)
print(list)

