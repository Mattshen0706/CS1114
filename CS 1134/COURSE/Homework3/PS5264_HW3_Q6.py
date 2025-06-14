# nested_lst=[[1,2],3,[4,[5,[6,[7],8]]]]

def flat_list(nest_lst,low,high):
    result=[]
    def flat_helper(nest_lst,low,high):
        for i in range(low,high):
            if type(nest_lst[i])==int:
                result.append(nest_lst[i])
            else:
                flat_helper(nest_lst[i],low=0,high=len(nest_lst[i]))
    flat_helper(nest_lst,low,high+1)
    return result

nested_lst=[[1,2],3,[4,[5,[6,[7],8]]]]
print(flat_list(nested_lst,0,2))

# iterate through every element within the list until it can not further iterate, how do you do that ?

# e,se
