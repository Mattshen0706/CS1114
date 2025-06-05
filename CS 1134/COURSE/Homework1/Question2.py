# COMPREHENSIONS

lst=[10**n for n in range(6)]
print(lst)

lst=[n**2 + n for n in range(10)]
print(lst)

lst=[chr(n) for n in range(97,123)]
print(lst)

# VECTOR QUESTION

class Vector:
    def __init__(self, d):
        if type(d)==list:
            self.coords=d
        else:
            self.coords = [0]*d
    def __len__(self):
        return len(self.coords)
    def __getitem__(self, j):
        return self.coords[j]
    
    def __sub__(self,other):
        subtraction=[self.coords[n]-other.coords[n] for n in range(len(self.coords))]
        return subtraction

    def __neg__ (self):
        negativeversion=[self.coords[n]*-1 for n in range (len(self.coords))]
        return negativeversion
    
    def __mul__(self,factor):
        if type(factor)==int:
            multiplyversion=[self.coords[n]*factor for n in range(len(self.coords))]
            return multiplyversion
        elif type(factor)==list:
            multiplyversion=[self.coords[n]*factor[n] for n in range(len(self.coords))]
            return sum(multiplyversion)
        else:
            multiplyversion=[self.coords[n]*factor.coords[n] for n in range(len(self.coords))]
            return sum(multiplyversion)
    
    def __rmul__(self,factor):
        multiplyversion=[self.coords[n]*factor for n in range(len(self.coords))]
        return multiplyversion
    
    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        return self.coords == other.coords
    
    def __ne__(self, other):
        return not (self == other)
    
    def __str__(self):
        return self.coords
    
    def __repr__(self):
        return str(self)


# Question 5:

# Method 1: Quadratic time complexity O(n**2)

def two_sum(srt_lst,target):

    for i in range(0,len(srt_lst)):
        if target - srt_lst[i] in srt_lst:
            return (srt_lst.index(srt_lst[i]),srt_lst.index(target-srt_lst[i]))
        else:
            return None

def main():
    srt_lst=[-2, 7, 11, 15, 20, 21]
    print(two_sum(srt_lst,22))

# Method 2: Quadratic time complexity O(n**2)

def two_sum(srt_lst,target):
    subtractlist=[]
    for i in range(0,len(srt_lst)):
        subtraction=target-srt_lst[i]
        if srt_lst[i] in subtractlist:
            return (srt_lst.index(srt_lst[i]),srt_lst.index(target-srt_lst[i]))
        subtractlist.append(subtraction)
    return None

def main():
    srt_lst=[-2, 7, 11, 15, 20, 21]
    print(two_sum(srt_lst,22))

# Method 2: Linear time complexity O(n)

def two_sum(srt_lst,target):
    subtractdict={}
    for i,number in enumerate(srt_lst): #Learnt enumerate using online resources
        subtraction = target - number
        if subtraction in subtractdict:
            return (subtractdict[subtraction],i)
        subtractdict[number] = i
    return None


# def main():
#     srt_lst=[-2, 7, 11, 15, 20, 21]
#     print(two_sum(srt_lst,19))
    
# main()

# def main():
#     srt_lst=[-2, 7, 11, 15, 20, 21]
#     print(two_sum(srt_lst,22))

    
    
# Question 6:

# TIME COMPLEXITY: O(n)

def split_parity(lst):
    pointerL=0
    pointerR=len(lst)-1
    while pointerL<pointerR:
        if lst[pointerL]%2!=0:
            pointerL+=1
        elif lst[pointerR]%2==0:
            pointerR-=1
        else:
            lst[pointerL],lst[pointerR]=lst[pointerR],lst[pointerL]
    return lst

def main():
    lst=[1,24,28,234,834,2,4,3,2,78,9]
    print(split_parity(lst))

main()


# Question 7:


def e_approx(n):
    factoriallist=[1]
    sum=0
    for i in range(1,n+1):
        factoriallist.append(i*factoriallist[-1])
        sum+=1/factoriallist[-1]*i
    return sum 
        
    
def main():
    for n in range(100):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n ,"Approximation:",approx_str)
        
main()

