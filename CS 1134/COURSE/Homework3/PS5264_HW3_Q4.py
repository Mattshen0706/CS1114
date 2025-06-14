# 4 
# a)

def count_lowercase(s, low, high):
    if low==high:
        return 0
    else:
        if s[low].islower():
            return 1 + count_lowercase(s,low+1,high)
        else:
            return count_lowercase(s,low+1,high)


# b)


def is_number_of_lowercase_evencount_lowercase(s, low, high):
    
    def count_lowercase(s, low, high):
        if low==high:
            return 0
        else:
            if s[low].islower():
                return 1 + count_lowercase(s,low+1,high)
            else:
                return count_lowercase(s,low+1,high)
    sum=count_lowercase(s,low,high)

    if sum %2==0:
        return True
    return False

